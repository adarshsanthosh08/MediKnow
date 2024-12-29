from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import google.generativeai as genai
import json
import re
from Medical.config import API_KEY

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You can now log in')
            return render(request, 'login.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:
                # Debugging
                print("Form is valid")

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                # Authenticate the user
                user = authenticate(username=username, password=password)

                # Debugging
                print("User authenticated:", user)

                if user is not None:
                    # Successful login
                    login(request, user)
                    return redirect('index')
                else:
                    # Invalid username/password combination
                    print("Invalid credentials")
                    messages.error(request, "Invalid username or password.")
                    return render(request, 'login.html', {'form': form})

            except Exception as e:
                # Catch any unexpected errors and log them
                print(f"An error occurred: {e}")
                messages.error(request, "An unexpected error occurred. Please try again later.")
                return render(request, 'login.html', {'form': form})

        else:
            # Form is invalid
            messages.error(request, "Please enter a valid username and password.")
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

    
# nlp = spacy.load(r'C:\Users\admroot\Desktop\NER\StagMinds_NER\NER_Model\ner')



@login_required
def index(request):
    return render(request, 'index.html')


genai.configure(api_key=API_KEY)

def clean_response(response):
    # Remove the 'Raw response: ```json' and '```' parts if they exist
    response = response.replace('Raw response: ```json', '').replace('```', '').strip()

    # Remove unnecessary characters and replace 'null' with ''
    response = response.replace('null', '""')
    response = response.replace('JSON', '')
    response = response.replace('json', '')

    # Handle newline characters within JSON strings
    response = re.sub(r'\\n', ' ', response)
    response = re.sub(r'\s+', ' ', response).strip()

    return response

def get_gemini_response(input_text):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="""Extract the following details from the text:
        - CATEGORY - category of the drug
        - DIM - dosage limit
        - MEDICAL_NAME - if given
        - PACK - if given
        - STRENGTH - if given
        - DESCRIPTION - a detailed description about the medicine in a paragraph, including:
        * General usage and therapeutic indications (e.g., what the drug is used for).
        * Recommended dosage and administration guidelines.
        * Possible side effects and contraindications.
        * Any known drug interactions or precautions.
        * Variants (e.g., different strengths, forms like tablets, injections, etc.).
        * How the drug works (e.g., mechanism of action).
        * Storage and handling information.
        * Any other relevant information that might be useful for a user or healthcare professional.
        
        Provide the results strictly in the format as:
        [
            {"text": "value", "label": "CATEGORY"},
            {"text": "value", "label": "DIM"},
            ...........
        ]
        Don't add ''json at the end or the beginning
        """
    )
    
    response = model.generate_content([input_text])
    print(response)
    
    # Clean the response if it contains unwanted string like '''json or ''' at the end
    cleaned_response = response.text.strip()
    
    # Remove leading '''json or any unwanted wrapping from the response
    if cleaned_response.startswith("'''json"):
        cleaned_response = cleaned_response[len("'''json"):].strip()
    
    # If the response ends with ''' or similar, remove it
    if cleaned_response.endswith("'''"):
        cleaned_response = cleaned_response[:-3].strip()

    # Parse the cleaned response
    try:
        extracted_entities = json.loads(cleaned_response)

        print(extracted_entities)
        return extracted_entities
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response from Gemini: {cleaned_response}") from e




@login_required
def extract(request):
    rawtext = ""
    extracted_entities = []
    html_result = ""
    if request.method == "POST":
        rawtext = request.POST.get("rawtext", "")

        print("raw_text is:" ,rawtext)

        # Get the Gemini response
        try:
            extracted_entities = get_gemini_response(rawtext)
        except ValueError as e:
            return render(request, "results.html", {
                "rawtext": rawtext,
                "error": f"Error processing text: {e}",
            })

        # Generate HTML result
        if extracted_entities:
            html_result = f"<h3>Extracted Entities:</h3><ul>"
            for entity in extracted_entities:
                html_result += f"<li><strong>{entity['label']}:</strong> {entity['text']}</li>"
            html_result += "</ul>"

        # Save analysis to the database
        analysis = Post(user_name=request.user, rawtext=rawtext, result=json.dumps(extracted_entities))
        analysis.save()

    return render(request, "results.html", {
        "rawtext": rawtext,
        "result": html_result,
        "entities": extracted_entities,
    })



@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

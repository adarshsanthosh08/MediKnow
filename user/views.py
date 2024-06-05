from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
import spacy
from spacy import displacy
from .models import Post

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to 'index' instead of 'login'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
nlp = spacy.load(r'C:\Users\admroot\Desktop\rithul\NER_Model\model-best-version 1')



@login_required
def index(request):
    return render(request, 'index.html')



@login_required
def extract(request):
    rawtext = ""
    result = ""
    if request.method == "POST":
        rawtext = request.POST.get('rawtext', '')
        doc = nlp(rawtext)
        
        # Extract entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        html = displacy.render(doc, style='ent')
        result = html

        # Save analysis to the database
        analysis = Post(user_name=request.user, rawtext=rawtext, result=str(entities))
        analysis.save()
        
    return render(request, 'results.html', {'rawtext': rawtext, 'result': result})



@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

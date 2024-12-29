# MediKnow: Empowering You with Accurate Medical Knowledge

#### Video Demo: [Demo Url](https://www.youtube.com/watch?v=XHP4gbbZhRE)

#### Description:

**MediKnow** is an advanced medical knowledge platform designed to provide users with accurate and comprehensive information about medications. Using **Gemini's latest generation AI model**, MediKnow can accurately extract entities from the medicine names entered by the user and provide detailed descriptions, usage, and other relevant information in an easy-to-understand format. The platform's **stylish and user-friendly interface** ensures convenience while offering precise results for medical inquiries.

This project was built using **Django**, leveraging the power of the Gemini AI model to process and provide insights into various medical substances. Whether you're looking for drug usage, strength, dosage, or other relevant medical details, **MediKnow** can assist you with its intelligent entity extraction.

### Key Features:

- **Entity Extraction**: Utilizes Gemini's AI to identify medical entities, such as the medicine name, category, strength, packaging, and usage.
- **Detailed Information**: For every medicine, the platform provides an accurate description, usage guidelines, and any other relevant medical data.
- **User-Friendly UI**: The interface is designed with the user's convenience in mind, making it easy to navigate and obtain the necessary information quickly.
- **Real-Time Interaction**: Users can enter a medicine name, and the system will fetch the relevant information almost instantly.

### Project Structure:

The **MediKnow** project is divided into two main directories:

1. **`medical/`**: This is the main Django project directory. It contains the core Django project settings, including configurations for the app, database, URLs, and other backend-related features.

   - **`settings.py`**: Contains all project-level settings, such as database configuration, middleware, templates, static files, etc.
   - **`urls.py`**: Contains URL routing configurations for the entire Django project.
   - **`wsgi.py`**: For deployment purposes, serves as the entry point for the WSGI server.

2. **`user/`**: This directory handles all aspects related to user interaction, such as displaying the UI, handling user requests, and managing the logic behind the medical data queries.

   - **`models.py`**: Contains the models for storing user information, medical queries, and other application-specific data.
   - **`views.py`**: Contains views responsible for processing user input, interacting with the Gemini AI model, and displaying results on the front end.
   - **`templates/`**: Contains HTML files for the user interface, designed with an aesthetically pleasing and modern look.
   - **`static/`**: Houses CSS and JavaScript files that contribute to the visual design and interactivity of the platform.

### How to Set Up:

To set up the environment for **MediKnow**, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/adarshsanthosh08/MediKnow.git
    ```

2. Navigate to the project directory:
    ```bash
    cd project
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/macOS
    env\Scripts\activate  # For Windows
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

Now, you can visit `http://localhost:8000/` in your browser to interact with the **MediKnow** platform.

### Usage:

Once the server is running, users can:

1. Enter a **medicine name** into the provided input field.
2. The **Gemini AI** will process the name, extract relevant entities, and return a detailed description, usage instructions, and other information about the medication.
3. The interface is designed to be intuitive, with clear and concise results.

### Example:

- **Medicine Name**: "Aspirin"
- **Extracted Entities**:
  - **Category**: Analgesic
  - **Strength**: 500 mg
  - **Usage**: Used for pain relief and to reduce inflammation.
  - **Pack**: 30 tablets

The AI will return an accurate summary of this information along with any additional relevant details.

### Screenshots:

Here, you can add screenshots of the project to demonstrate the UI.

### Requirements:

- Python 3.8+
- Django 3.x or above
- Gemini AI (or any other required APIs for the AI model)

### Markup Sheet:

Here is a sample markup sheet for uploading medicine names along with their expected entities:

| Medicine Name | Category      | Strength | Pack          | Usage                       |
|---------------|---------------|----------|---------------|-----------------------------|
| Aspirin       | Analgesic     | 500 mg   | 30 tablets    | Pain relief, inflammation   |
| Amoxicillin   | Antibiotic    | 250 mg   | 10 capsules   | Bacterial infection treatment |
| Paracetamol   | Analgesic     | 500 mg   | 20 tablets    | Pain relief, fever reduction |

---

Feel free to explore the **MediKnow** platform and get the accurate medical knowledge you need with ease!

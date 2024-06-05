## Custom NER for Medical Data Using SpaCy

This repository contains a custom Named Entity Recognition (NER) system tailored for medical data using SpaCy. The NER model is trained to identify specific entities relevant to the medical domain, such as diseases, treatments, symptoms, and more.

### Description

Named Entity Recognition (NER) is a crucial task in natural language processing (NLP), particularly in the medical field, where accurately identifying entities can aid in tasks like information extraction, document summarization, and question answering. This custom NER model is trained on medical data to accurately recognize and classify various entities present in medical texts.

### Installation

To set up the environment for this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

5. Make database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Replace the path to the custom NER model in the `views.py` file located in the `user` folder with the path to your trained NER model.

### Usage

Once the environment is set up, you can run the Django development server:

```bash
python manage.py runserver

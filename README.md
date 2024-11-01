## Getting Started

To set up and run this project locally, follow these steps:

1. **create virtual environment and activate the virual environment**

2. **Navigate to the Project Directory**

   ```bash
   cd Zone_Sparks_backend

3. **run this command to install required dependence**

    ```bash
    pip install -r requirements.txt

4. **run migration amd migrate command**

    ```bash
    python manage.py makemigrations

    python manage.py migrate


5. **Create a superuser to run this command**

    ```bash
    python manage.py createsuperuser

6. **Run this command to run development server**

    ```bash
    python manage.py runserver

## Getting Started

To set up and run this project locally, follow these steps:

1. **create virtual environment and activate the virtual environment**

2. **Navigate to the Project Directory**

   ```bash
   cd Zone_Sparks_backend

3. **run this command to install required dependence**

    ```bash
    pip install -r requirements.txt

4. **run migration and migrate command**

    ```bash
    python manage.py makemigrations

    python manage.py migrate


5. **run this command to create a superuser**

    ```bash
    python manage.py createsuperuser

6. **run this command to start development server**

    ```bash
    python manage.py runserver

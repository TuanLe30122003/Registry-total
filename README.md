# Registry-total

Installation guide
---------
open terminal in project root (powershell)
1. Install python 3.8.5
2. Create virtual environment
    ```bash
    python -m venv pyenv
    ```
3. Activate virtual environment and install Django
    ```bash
    pyenv/scripts/activate.ps1
    py -m pip install Django
    ```

Run
---------
Run server
    ```bash
    cd backend
    python manage.py runserver
    ```
    
Addtional
---------
superuser for admin
    username: admin
    password: int3306

Development guide
---------
1. Create new app
    ```bash
    python manage.py startapp <app_name>
    ```
2. After create new model
    ```bash
    python manage.py makemigrations <app_name>
    python manage.py migrate <app_name>
    ```
    add to admin.py register
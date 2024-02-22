
# Django Project

## Description
SearchSmartly is a data processing project that aims to import Point of Interest (PoI) data from various sources, including CSV, JSON, and XML files, into a database. The imported data can be easily browsed through the web using the Django Admin Panel. This README provides essential information on how to set up, use, and contribute to the project.

## Prerequisites
- Python 3.12 or newer
- pip (Python package installer)
- PostgreSQL

## Setting Up the Environment
1. **Install Python 3.10+**: Ensure Python 3.12 or newer is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment**:
   ```
   python3.12 -m venv venv
   source venv/bin/activate
   ```

3. **Install Requirements**:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

1. **Create Postgres User** Note: It will ask you for the password for the new user search_smartly after confirmation you have to give the password of postgres user (Use any other user of your choice instead postgres).
   ```
   createuser -U postgres -P search_smartly
   psql -U postgres -c "ALTER USER search_smartly WITH SUPERUSER;"
   ```
   
2. **Create a Database for your Django app.** Note: It will ask password you set for the search_smartly user in the last command.
   ```
   createdb search_smartlya -U search_smartly -W 
   ```
   

3. **Migrate the Database**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Super User for Django Admin.** Note: after running the command set the username and password for you to access django admin.
   ```
   python manage.py createsuperuser
   ```   

5. **Run the Development Server** Note: Open a web browser and navigate to `http://127.0.0.1:8000/admin` to see your project running
   ```
   python manage.py runserver
   ```

## Additional Notes

**To parse files you can use this command**
```
python manage.py import_pois <filePath>
python manage.py import_pois <filePath> <filePath>
```

### 1. Clone the Repository
```
git clone https://github.com/Aman147181/sql_injection.git
cd sql_injection
```
### 2. Create and Activate Virtual Environment 
```
pip install virtualenv
virtualenv pythonenv
pythonenv/scripts/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Database setup
By default it uses sqlite in which sql injection is not possible. we can use postgres locally or by cloud

### 5. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 6. Create Superuser (For Admin Panel)
```
python manage.py createsuperuser
```
Follow the prompts to set up a superuser.

### 7. Run the Development Server
```
python manage.py runserver
```
The project will be available at
```
http://127.0.0.1:8000/
```

### 8. create dummy data
there is dummy.csv file here which you can import and load to database using admin page

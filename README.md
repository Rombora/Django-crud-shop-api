# crud-shop-api
A simple django api implementing CRUD

Product model:
- name
- description
- price
- category

Category model:
- name

Views:
- list of all products
- details of each product
- add new product
- edit existing product
- delete existing product

- list of all categories
- details of each category
- add new category
- edit existing category
- delete existing category



## Getting started

This project is written in Python 3, and works on any platform 


- Clone the repository using Git

Run the following in a virtual environment

`python -m venv venv`
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```






The application can now be accessed through http://127.0.0.1:8000 in the browser


The user is prompted to login.
The application has an existing superuser account which can be used to login.
Use the following credentials:

  username: admin

  password: admin

One can also register a user from the signup page. Although the registered user will lack superuser priviledges.


You can create a custom supeuser from the command-line by running
```
python manage.py createsuperuser
```

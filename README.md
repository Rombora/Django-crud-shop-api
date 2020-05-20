# CRUD
## Django Shop API
This is a simple django API implementing the four basic functions of persistent storage, Create, Read, Update and Delete (CRUD).

Product model:
* name
* description
* price
* category

Category model:
* name

Views:
* list of all products
* details of each product
* add new product
* edit existing product
* delete existing product

* list of all categories
* details of each category
* add new category
* edit existing category
* delete existing category



## Getting started

This project is written in Python 3, and works on any platform .


- Clone the repository using Git

Run the following in to create a virtual environment.

```bash
$ python -m venv env
$ source env/bin/activate
```
Install the required modules for the project.

```bash
$ pip install -r requirements.txt
```
To propagate changes in model, run:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Start the server using
```
$ python manage.py runserver
```






The application can now be accessed through http://127.0.0.1:8000 in the browser


The user is prompted to login.
The application has an existing superuser account which can be used during login.
Use the following credentials:

  **username: admin**

  **password: admin**

A user can be registered from the signup page. This user will lack superuser privileges, for security purposes.

A custom supeuser can be created from the command-line by running
```bash
$ python manage.py createsuperuser
```

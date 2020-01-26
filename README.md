# Simple-Flashcards
### Description
This is a simple flashcards app to help you learn languages, prepare for exams, etc. The unlogged user can show all decks and learn their flashcards but only logged in user can manage their decks and cards.

### Features
Here is a list of its main features:
- Register and login mode
- showing and updating your Profile also with adding your image as a avatar and showing other users profiles
- creating, updating and deleting decks with title and description of the deck
- creating, updating and deleting flashcard and showing them as set of all flashcards in specific deck
- learning flashcards mode where you can display one side of flashcard and clicking on it you can see its translation
- possibility to learn of random flashcards or one after the other 
- showing all decks of logged in user in the sidebar
- searching specific deck or card

### Technologies
- Python 3.7
- Django 2.2
- Django Crispy Forms
- SQLite
- Bootstrap 4
- jQuery
- HTML
- AWS S3


### Installation

##### Clone repository

To run the app yourself, you will need to clone the repository, decide upon a directory where you want to place it and in terminal run the following command:
```sh
$ git clone https://github.com/eRafaell/simple-flashcards.git
```

##### Virtual environment installation

Next you should create virtual environment. Virtualenv is a tool used to create an isolated Python environment. The virtualenv package is required to create virtual environments. You can install it with pip:
```sh
$ pip install virtualenv
```

##### Virtual environment creation

To create a virtual environment, decide upon a directory where you have the project, and run the venv module as a script with the directory path:
```sh
$ python -m venv env
```
This will create env directory, which is the name of virtual environment, if it does not exist, and also create directories inside it.

##### Virtual environment activation

After created a virtual environment, you may activate it:

On Windows, run:
```sh
$ env\Scripts\activate.bat
```
On Unix or MacOS, run:
```sh
$ source env/bin/activate
```

##### Modules installation

Next you can install all required modules:
```sh
$ pip install -r requirements.txt
```

##### Save changes in database

To make changes into your database schema (adding a field, deleting a model, etc.) create initial migrations for each and every app
```sh
$ python manage.py makemigrations 
```
and to apply the change to your data:
```sh
$ python manage.py migrate
```

##### Create a media folder
In the main folder flashcards create a subfolder with name media (it should be at the same level as manage.py file) and paste into that subfolder some picture called default.png as the default avatar

##### Create an administrator

Next you need to create a user who can login to the admin site:
```sh
$ python manage.py createsuperuser
```
Then you have to enter your desired username, optional email and password

And finally you can start your local server

##### Run server

```sh
$ python manage.py runserver
```
now you can browse the website locally at http://localhost:8000/ or http://127.0.0.1:8000


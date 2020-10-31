# Product-Management
A repository which helps a user to manage product and its categories

### Install a Python virtualenv using pip
    $ sudo pip install virtualenv

### Create virtualenv
    $ virtualenv venv 
    
To activate a virtual environment:

    $ source ./venv/bin/activate

### Install dependencies
    $ pip install -r requirements.txt
    $ npm install

### Create superuser

    $ ./manage.py createsuperuser

### Create tables

    $ ./manage.py migrate
    
### Finally, Run the server

    $ ./manage.py runserver

# Todo-App | Django and PostgreSQL

A CRUD where you can create To-do tasks which are saved in a PostgreSQL database.

To run the project you just need to create a virtual environment, install the necessary dependencies. With the following commands.

```
- virtualenv venv
- source venv/bin/activate
- pip install django
- pip install psycopg2
```

Then you need to start postgresql in your computer. In Linux you need to use the following command.

```
- sudo service postgresql start
```

After that you will need to change the configuration of the PostgreSQL database in settings.py, in line 77:

```
DATABASES = {
    # PostgreSQL connection database 🐘
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tasksdb',
        'USER': 'postgres',
        'PASSWORD': 'YourPassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

You have to create a new database called 'tasksdb' and add your PostgreSQL password to the settings.py file.

And finally, run the server.

```
- python3 manage.py runserver
```


## Table of contents
1. [List tasks](#tasks)
2. [Edit task form](#edit)
3. [PostgreSQL](#sql)

### List tasks <a name="tasks"></a>

### Edit task form <a name="edit"></a>

### PostgreSQL<a name="sql"></a>


#### My Socials
<a href="https://www.linkedin.com/in/salmeron-alvarado/"><img align="left" src="https://raw.githubusercontent.com/yushi1007/yushi1007/main/images/linkedin.svg" alt="Salmeron | LinkedIn" width="24px"/></a>


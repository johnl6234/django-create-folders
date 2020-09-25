### Create django folders

this file creates templates and static folders inside the app folder.

### Usage

Place file in project directory, modify 

```
projectName = {PROJECT_NAME} # change to your project name
app_name = {APP_NAME} # change to your app name
 ```

run file

### File structure after

```
projectName/
    manage.py
    create_django_folders.py_
    db.sqlite3
    projectName/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app_name/
        migrations/
            __init__.py
        templates/
            app_name/
                base.html
                index.html
        static/
            app_name/
                CSS/
                    styles.css
                IMG/
                JS/
                    script.js
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
```
#### Settings.py

```
"""
Django settings for djangoTest project.

Generated by 'django-admin startproject' using Django 3.1.

 /......../
"""
import os  #..... Added
from pathlib import Path

 /......../

# Application definition

INSTALLED_APPS = [
    'app_name', #..... added
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

 /......../

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  #..... Added
    ]
```

#### projectName/urls.py

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('testApp.urls')),
    path('admin/', admin.site.urls),
    ]
```
#### app_name/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   ]

```

#### app_name/views.py

```
from django.shortcuts  import render

def index(request):
    return render(request,'testApp/index.html')
```

#### templates/app_name/base.html

```
{% load static %}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="{% static 'styles.css' %}">
    </head>
<body>
{% block content %}{% endblock %}
</body>
</html>
```

#### template/app_name/index.html

```
{% extends 'testApp/base.html'%}

{% block content %}

Hello, World!

{% endblock %}
```
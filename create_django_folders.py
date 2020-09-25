
# place file in project directory

import os

projectName = {PROJECT_NAME} # change to your project name
app_name = {APP_NAME} # change to your app name

os.chdir(app_name)

# create templates folder
templates = './templates'
if not os.path.exists(templates):
    os.mkdir(templates)
    os.chdir(templates)
    if not os.path.exists(app_name):
        os.mkdir(app_name)
    # create base/index html files
    os.chdir(app_name)
    with open('base.html','x') as base:
        base.write('''{% load static %}\n\n<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <meta charset="UTF-8">\n        <meta name="viewport" content="width=device-width, initial-scale=1">\n        <link rel="stylesheet" href="{% static 'styles.css' %}">\n    </head>\n<body>\n{% block content %}{% endblock %}\n</body>\n</html>''')
        base.close()

    with open('index.html','x') as index:
        index.write("{% extends '" + app_name + "/base.html'%}\n\n{% block content %}\n\nHello, World!\n\n{% endblock %}")
        index.close()

os.chdir('../')
os.chdir('../')

# create static folder and css/js files
static = './static'
if not os.path.exists(static):
    os.mkdir(static)
    os.chdir(static)
    if not os.path.exists(app_name):
        os.mkdir(app_name)
        os.chdir(app_name)
        os.mkdir('./CSS')
        os.chdir('./CSS')
        css = open('styles.css', 'x')
        css.close()
        os.chdir('../')
        os.mkdir('./JS')
        os.chdir('./JS')
        js = open('script.js', 'x')
        js.close()
        os.chdir('../')
        os.mkdir('./IMG')
        os.chdir('../')

# create urls.py
os.chdir('../')
urls = open('urls.py','x')
urls.write("from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path('', views.index, name='index'),\n   ]")
urls.close()

# amend views.py
with open('views.py', 'w') as myfile:
    myfile.write("from django.shortcuts  import render\n\ndef index(request):\n    return render(request,'" + app_name + "/index.html')")
    myfile.close()

# amend project urls
os.chdir('../')
os.chdir(projectName)
with open('urls.py', 'w') as projectUrls:
    projectUrls.write("from django.contrib import admin\nfrom django.urls import path,include\n\nurlpatterns = [\n    path('', include('" + app_name + ".urls')),\n    path('admin/', admin.site.urls),\n    ]")

# m0odify settings.py
f = open("settings.py", "r")
contents = f.readlines()
f.close()
contents.insert(11,"import os")
contents.insert(34, "    '"+app_name+"',\n")
f = open("settings.py", "w")
contents = "".join(contents)
f.write(contents)
f.close()

f = open("settings.py", "a")
f.write("\nSTATICFILES_DIRS = [\n    os.path.join(BASE_DIR, 'static')\n    ]")
f.close()
import os, time

# PROGRAM FOR CREATING FLASK ALL-FILES

root = os.getcwd()

# FILE INFORMATION [APP, MODELS,

# [app.py] File
basic_app = """ 
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

# YOUR APPLICATION
app = Flask(__name__)

# YOUR DATABASE [SQLITE3]
db = SQLAlchemy(app)
db_file = 'database.db'

# FLASK CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_USERNAME'] = 'admin'
app.config['SQLALCHEMY_PASSWORD'] = 'admin'
app.config['SESSION_COOKIE_NAME'] = 'C00KIE1337'

# SECRET KEY [ CHANGE ]
app.secret_key = 'CHANGE.THIS.ASAP'

# AWS
app.config['AWS_SECRET_KEY'] = 'YOUR.KEY.HERE'
app.config['AWS_KEY_ID'] = 'KEY.ID.HERE'

# BASIC ROUTE TO INDEX/INDEX.HTML
@app.route('/')
def index():
    return render_template('index/index.html')

# BASIC ROUTE TO ADMIN/ADMIN.HTML
@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

if __name__ == '__main__':
    app.run(debug=True)
"""

# [models.py] File
basic_model = """ 

"""

def base_html(filename):
    os.system(f'fsutil file createnew {filename} 2000')
    file = os.getcwd() + "\\" + filename
    print(file)
    f = open(file, 'a')
    f.write("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">
    
    <!-- basic navbar [DELETE IF NOT USEFUL] -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">MyTemplate</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample07" aria-controls="navbarsExample07" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarsExample07">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="/">Index</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/admin">Admin</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Another</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="https://example.com" id="dropdown07" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown</a>
              <div class="dropdown-menu" aria-labelledby="dropdown07">
                <a class="dropdown-item" href="#">Put</a>
                <a class="dropdown-item" href="#">Links</a>
                <a class="dropdown-item" href="#">Here</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-md-0">
            <input class="form-control" type="text" placeholder="search" aria-label="Search">
          </form>
        </div>
      </div>
    </nav>
    
    <!-- Block Head -->
    {% block head %} 
    <!-- title tag is inside the 'block head' in child html's -->
    {% endblock %}
    
  </head>
  <body>
    {% block body %} 
    <!-- title tag is inside the 'block head' in child html's -->
    
    
        {% block content %}
        
        {% endblock %}
    
    {% endblock %}
    
        
        
    <div class="container">
    <!-- DELETE BELOW THIS -->
    
        <br>
        <h1> If you can read this, you are up to go!</h1>
        <br>
        <h4> I hope this save you some time! </h4>
        <br>
        <h4> If you like this, please follow me on github <a style="color: red; text-decoration: none;" href="https://github.com/ngeorgj">@ngeorgj</a></h4>
        <br>
        <h4> In case of bugs, compliments or comments email to <b>ngj.netrunner@gmail.com</b></h4>
        
    <!-- END DELETE HERE -->
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='js/custom.js') }}">
  </body>
</html>    
    """)
    f.close()
    print(f'[{filename}] CREATED.')

def html_inherits_base(filename):
    os.system(f'fsutil file createnew {filename} 2000')
    file = os.getcwd() + "\\" + filename
    f = open(file, 'a')
    f.write("""
{% extends './base.html' %}

{% block head %}
<title>Inherits from 'base.html'</title>
{% endblock %}

{% block body %}
{% endblock %}
    """)

def line(what):
    os.system(f'{what}')


def new_folder(folder_name):
    os.system(f'mkdir {folder_name}')
    print(f'[{folder_name}/] CREATED.')

def change_directory(dir_name=""):
    os.chdir(root + '\\' + dir_name)


def go_root():
    line('cd ' + root)


def new_file(name, size):
    line(f'fsutil file createnew {name} {size}')


def create_py(filename, content):
    new_file(filename, 5000)
    file = os.getcwd() + "\\" + filename
    f = open(file, 'a')
    f.write(content)
    f.close()
    print(f'[{filename}] CREATED.')


# Create Templates and Static Folders
new_folder('templates')
new_folder('static')

# TEMPLATES
change_directory('templates')
base_html('base.html')
new_folder('index')
new_folder('admin')
change_directory('templates/index')
html_inherits_base('index.html')
change_directory('templates')
change_directory('templates/admin')
html_inherits_base('admin.html')
change_directory()
print('TEMPLATES FOLDER [OK]')

# STATIC
change_directory('static')
new_folder('css')
new_folder('js')
change_directory('static/css')
new_file('custom.css', 1000)
change_directory('static/js')
new_file('custom.js', 1000)
change_directory()  # Goes back to Root
print('STATIC FOLDER [OK]')

# CREATE DATABASE
new_file('database.db', 8000)
print('[database.db] CREATED.')

# CREATE THE 'APP.PY' FILE
create_py('app.py', basic_app)

# CREATE THE 'MODELS.PY' FILE
create_py('models.py', basic_model)

print("""
    YOUR FOLDER STRUCTURE IS THE FOLLOWING:
    
    MAIN_FOLDER/
     | > templates/
     |   > index/
     |             index.html
     |   > admin/
     |             admin.html
     |   base.html
     | > static/
     |   > css/
     |             custom.css
     |   > js/
     |             custom.js
     app.py
     models.py
     database.db
""")

# ASKS USER IF IT WANTS TO TEST
choice = input('     START TEST SERVER [Y/N]? > ')

if choice == 'Y' or 'y':
    print("     Starting Test Server... [if response is 'not found' press 'F5']")
    time.sleep(1)
    line('start http://127.0.0.1:5000')
    line('app.py')
else:
    print("     Terminating setup. Now you can open the folder with your IDE and edit it!")
    time.sleep(3)
    pass





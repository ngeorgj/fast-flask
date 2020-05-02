# ==================================================================================================================== #
# FAST FLASK                                  This is an minified application creator for flask applications.
# Flask Minified App Generator                It will allow you to gain time on your flask projects that uses
# Please follow me on GitHub: @ngeorgj        The basic starting code, it does everything for you!
# ==================================================================================================================== #

import os
import time
import sys

available_os = {
    'AIX': 'aix',
    'Linux': 'linux',
    'Windows': 'win32',
    'macOS': 'darwin'}


class FastFlask:
    """
    FAST FLASK SCRIPT
    Flask made easy (yes, more than it already is).

    The script basically runs a bunch of programs to create all files and folders you need to a basic
    Flask application to run smoothly.

    It will create an project structure like this:

    [root]
    |     [templates]
    |     |       [index]
    |     |       |      index.html
    |     |       |
    |     |       [admin]
    |     |       |      admin.html
    |     |       |
    |     |       base.html
    |     |
    |     [static]
    |     |       [css]
    |     |       |      custom.css
    |     |       |
    |     |       [js]
    |     |       |      custom.js
    |     |       |
    |     app.py
    |     models.py
    |     database.db
    |

    It's under development so it's really minified right now [May 08, 2020] but it will get better soon!

    Hope you like it!

    """
    # [app.py]
    f_app = """
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

    # [models.py]
    f_models = """

        """

    def __init__(self):
        self.os = ""
        self.root = ""
        self.get_os()

    def get_os(self):
        if sys.platform.startswith('aix'):
            self.os = available_os['AIX']
        elif sys.platform.startswith('linux'):
            self.os = available_os['Linux']
        elif sys.platform.startswith('win32'):
            self.os = available_os['Windows']
        elif sys.platform.startswith('darwin'):
            self.os = available_os['macOS']
        self.root = os.getcwd()
        print("My OS is: " + self.os)

    # HTML Basics
    def base_html(self, filename):
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
    <!-- DELETE BELOW THIS LINE-->

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

    def html_inherits_base(self, filename):
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

    # Command Line
    def line(self, what):
        os.system(f'{what}')

    def create_folder(self, folder_name):
        os.system(f'mkdir {folder_name}')
        print(f'[{folder_name}/] CREATED.')

    def go_to_folder(self, dir_name=""):
        """
        Leaving go_to_folder(empty) will lead to root dir

        :param dir_name: directory you want to move
        """
        os.chdir(self.root + '\\' + dir_name)

    # Go to Root Directory
    def root_dir(self):
        self.line('cd ' + self.root)

    # File Creation
    def new_file(self, name, size):
        self.line(f'fsutil file createnew {name} {size}')

    def create_py(self, filename, content):
        self.new_file(filename, 5000)
        file = os.getcwd() + "\\" + filename
        f = open(file, 'a')
        f.write(content)
        f.close()

    # Test Server
    def test_server(self):
        # ASKS USER IF IT WANTS TO TEST
        os.system('cls')
        print(" Flask Minified Project Created Successfully\n")
        choice = input(' Do you want to run the server for testing purposes [y/n]? > ')

        yes = ['yes', 'YES', 'Yes', 'y', 'ye']
        no = ['no', 'NO', 'No', ]

        if choice in yes:
            print("     Starting Test Server... [if response is 'not found' press 'F5']")
            time.sleep(1)
            os.system('cls')
            self.line('start http://127.0.0.1:5000')
            self.line('app.py')

        elif choice in no:
            print("     Terminating setup. Now you can open the folder with your IDE and edit it!")
            time.sleep(3)
            pass

        else:
            pass

    # Directory & File Creation
    def create_root(self):
        """
        Application goes

        [root]
          +  [Templates]
          +  [Static]
          +  app.py
          +  models.py
          +  database.db

        """
        self.create_folder('templates')
        self.create_folder('static')
        self.new_file('database.db', 8000)
        self.create_py('app.py', self.f_app)
        self.create_py('models.py', self.f_models)

    def create_templates(self):
        """
        Template Folder Files

        [root]
          +  [Templates]
            +  [index]
                        index.html
            +  [admin]
                        admin.html
            +  base.html

        """
        self.go_to_folder('templates')
        self.base_html('base.html')
        self.create_folder('index')
        self.create_folder('admin')
        self.go_to_folder('templates/index')
        self.html_inherits_base('index.html')
        self.go_to_folder('templates')
        self.go_to_folder('templates/admin')
        self.html_inherits_base('admin.html')
        self.go_to_folder()

    def create_static(self):
        """
        Static Folder Files

        [root]
          +  [Static]
            +  [css]
                        custom.css
            +  [js]
                        custom.js

        """
        self.go_to_folder('static')
        self.create_folder('css')
        self.create_folder('js')
        self.go_to_folder('static/css')
        self.new_file('custom.css', 1000)
        self.go_to_folder('static/js')
        self.new_file('custom.js', 1000)
        self.go_to_folder()  # Goes back to Root


# Running FastFlask()

fastflask = FastFlask()

fastflask.create_root()
fastflask.create_templates()
fastflask.create_static()
fastflask.test_server()

# End


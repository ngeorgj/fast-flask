# ==================================================================================================================== #
# FAST FLASK                                  This is an minified application creator for flask applications.
# Flask Minified App Generator                It will allow you to gain time on your flask projects that uses
# Please follow me on GitHub: @ngeorgj        The basic starting code, it does everything for you!
# ==================================================================================================================== #

import os
import time
import sys
import urllib.request

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
    |     |       [auth]
    |     |       |      login.html
    |     |       |      register.html
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
    f_app = """ #
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
    
# BASIC ROUTE TO AUTH/LOGIN.HTML
@app.route('/login')
def login():
    return render_template('auth/login.html')

# BASIC ROUTE TO AUTH/REGISTER.HTML
@app.route('/register')
def register():
    return render_template('auth/register.html')
    
if __name__ == '__main__':
    app.run(debug=True)
        """

    # [models.py]
    f_models = """

        """

    # HTML
    login_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Login Form</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- Custom CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/auth.css') }}">
    
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> 

</head>
<body>
<div class="login-form">
    <form action="/login" method="post">
        <h2 class="text-center">Log in</h2>       
        <div class="form-group">
            <input name="username" type="text" class="form-control" placeholder="Username" required="required">
        </div>
        <div class="form-group">
            <input name="password" type="password" class="form-control" placeholder="Password" required="required">
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block">Log in</button>
        </div>
        <div class="clearfix">
            <label class="pull-left checkbox-inline"><input type="checkbox"> Remember me</label>
            <a href="#" class="pull-right">Forgot Password?</a>
        </div>        
    </form>
    <p class="text-center"><a href="/register">Create Account</a></p>
</div>
</body>
</html>  
    """

    register_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Register Form</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- Custom CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/auth.css') }}">
    
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> 

</head>
<body>
<div class="login-form">
    <form action="/register" method="post">
        <h2 class="text-center">Register</h2>       
        <div class="form-group">
            <input name="username" type="text" class="form-control" placeholder="Username" required="required">
        </div>
        <div class="form-group">
            <input name="email" type="email" class="form-control" placeholder="Email" required="required">
        </div>
        <div class="form-group">
            <input name="password" type="password" class="form-control" placeholder="Password" required="required">
        </div>
        <div class="form-group">
            <input name="confirm_password" type="password" class="form-control" placeholder="Confirm Password" required="required">
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block">Sign up</button>
        </div>      
    </form>
    <p class="text-center"><a href="/login">Already registered? Clich here to Login.</a></p>
</div>
</body>
</html>  
    """

    # CSS
    auth_css = """.login-form {
    width: 340px;
    margin: 50px auto;
}
.login-form form {
    margin-bottom: 15px;
    background: #f7f7f7;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    padding: 30px;
}
.login-form h2 {
    margin: 0 0 15px;
}
.form-control, .btn {
    min-height: 38px;
    border-radius: 2px;
}
.btn {        
    font-size: 15px;
    font-weight: bold;
}       
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
        <a class="navbar-brand" href="/">FastFlask</a>
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
              <a class="nav-link dropdown-toggle" href="https://example.com" id="dropdown07" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">DropMenu</a>
              <div class="dropdown-menu" aria-labelledby="dropdown07">
                <a class="dropdown-item" href="#">Put</a>
                <a class="dropdown-item" href="#">Links</a>
                <a class="dropdown-item" href="#">Here</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-md-0">
            <a href="/login" type="button" class="btn btn-warning">Login</a>
            <a href="/register" type="button" class="btn btn-info" style="margin-left: 10px;">Register</a>
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
    <div class="jumbotron">
      <h1 class="display-4">If you can read this, you are up to go!</h1>
      <p class="lead">I hope this save you some time! </p>
      <hr class="my-4">
      <p>If you like this, please follow me on github <a style="color: red; text-decoration: none;" href="https://github.com/ngeorgj">@ngeorgj</a></p>
      <p>In case of bugs, compliments or comments email to <b>ngj.netrunner@gmail.com</b></p>
      <p class="lead">
        <a class="btn btn-primary btn-lg" href="#" role="button">Enjoy</a>
      </p>
    </div>
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

    def login_html(self, filename='login.html'):
        os.system(f'fsutil file createnew {filename} 2000')
        file = os.getcwd() + "\\" + filename
        print(file)
        f = open(file, 'a')
        f.write(self.login_page_html)
        f.close()
        pass

    def register_html(self, filename='register.html'):
        os.system(f'fsutil file createnew {filename} 1000')
        file = os.getcwd() + "\\" + filename
        print(file)
        f = open(file, 'a')
        f.write(self.register_page_html)
        f.close()
        pass

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
    def new_empty_file(self, name, size):
        self.line(f'fsutil file createnew {name} {size}')

    def create_file(self, filename, content):
        self.new_empty_file(filename, 5000)
        file = os.getcwd() + "\\" + filename
        f = open(file, 'a')
        f.truncate(0)
        f.write(content)
        f.close()

    def write_to_file(self, filename, what):
        file = os.getcwd() + "\\" + filename
        f = open(file, 'r+')
        f.truncate(0)
        f.write(what)
        f.close()

    def get_code_from_github(self, filename, source):
        code = urllib.request.urlopen(source)
        code = code.read()
        code = str(code, encoding='utf-8')

        self.create_file(filename, code)

        print(code)

    # Test Server
    def test_server(self):
        # ASKS USER IF IT WANTS TO TEST
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
        self.new_empty_file('database.db', 8000)
        self.create_file('app.py', self.f_app)
        self.create_file('models.py', self.f_models)

    def create_templates(self):
        """
        Template Folder Files

        [root]
          +  [Templates]
            +  [index]
                        index.html
            +  [admin]
                        admin.html
            +  [auth]
                        login.html
                        register.html
            +  base.html

        """
        self.go_to_folder('templates')
        self.base_html('base.html')
        self.create_folder('auth')
        self.create_folder('index')
        self.create_folder('admin')
        self.go_to_folder('templates/index')
        self.html_inherits_base('index.html')
        self.go_to_folder('templates/admin')
        self.html_inherits_base('admin.html')
        self.go_to_folder('templates/auth')
        self.register_html()
        self.login_html()
        self.go_to_folder()

    def create_static(self):
        """
        Static Folder Files

        [root]
          +  [Static]
            +  [css]
                        custom.css
                        auth.css
            +  [js]
                        custom.js

        """

        self.go_to_folder('static')
        self.create_folder('css')
        self.create_folder('js')
        self.go_to_folder('static/css')
        self.new_empty_file('custom.css', 1000)
        self.new_empty_file('auth.css', 1000)
        self.write_to_file('auth.css', self.auth_css)
        self.go_to_folder('static/js')
        self.new_empty_file('custom.js', 1000)
        self.go_to_folder()  # Goes back to Root
        os.system('cls')
        print(" Flask Minified Project Created Successfully\n")


# Running FastFlask()

fastflask = FastFlask()

fastflask.get_code_from_github('testfile.html', "https://github.com/ngeorgj/fast-flask/raw/master/temp/templates/base.py")

#fastflask.create_root()
#fastflask.create_templates()
#fastflask.create_static()
#fastflask.test_server()

# End


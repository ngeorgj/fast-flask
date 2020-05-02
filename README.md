<h1> Fast Flask </h1>

<h3> Abstract </h3>
<p>
This is an executable python file for creating an basic flask structure.
It allows you to save time in the boring part of your initial app and is very useful for newcomers.

Can be used for barely anyone, it's as simple as execute the file (yes, it's that simple)

It will create the files to you application, so you can just configure as you wish.

The 'app.py' includes basic imports from flask (Flask, render_template, redirect, etc..) and the very basic structure of the app.

It has an simple configurable db file named 'database.db' (sqlite3 as default, new technologies coming soon...)

First Step > Throw the file inside your preferable folder, my example folder will be "Example".

+ Example/
    + templates/
        + index/
            + index.html
        + admin/
            + admin.html
        + base.html
    + static/
        + css/
            + custom.css
        + js/
            + custom.js
    + app.py
    + models.py
    + database.db
</p>
    
<h2> Dependencies </h2>

You have to pip install some libraries and having <a href="https://www.python.org/">Python</a> installed.

<a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> <br>
`pip install flask` <br>
This will allow you to work with flask (obviously)<br><br>

<a href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/">Flask-SQLAlchemy</a> <br>
`pip install flask-sqlalchemy`<br>
This will allow you to work with databases via SQLAlchemy<br><br>

<h1> The APP </h1>
```python
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
```

<h2> How to use? </h2>
<p>
1 - Create a folder as the "Example" above. <br>
2 - Throw your 'fastflask.py' file inside it. <br>
3 - Execute the file [fastflask.py] <br>
4 - Choose if you want to server test it (Recommended) <br>
5 - You can close the website and edit your files and start developing with this base. <br>
</p>
<h1> Final Part </h2>
<p>
If you enjoyed this and it helps you somehow, please leave follow me here on github and spread the word haha!<br>
</p>
<h3> Donate </h3>

| <b>BTC</b>   36vmLnP61kSgsQcDLpkKDfashea2wTgkr1          | <br>
| <b>ETH</b>   0x1Ff8aaB40005eaB0e70AB87b5225f200AF1A3615  | <br>
| <b>LTC</b>   MRQkoS1kH11PNWwV3YYL5DJn3WZ1yejFAe          |



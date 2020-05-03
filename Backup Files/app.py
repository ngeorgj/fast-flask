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
        

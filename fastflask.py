# ==================================================================================================================== #
# FAST FLASK                                  This is an minified application creator for flask applications.          #
# Flask Minified App Generator                It will allow you to gain time on your flask projects that uses          #
# Please follow me on GitHub: @ngeorgj        The basic starting code, it does everything for you!                     #
# ==================================================================================================================== #

import os
import time
import sys
import urllib.request
import threading


class FastFlask:
    # Source Files from Base Repository 'fast-flask/raw/master/origin'
    github = 'https://github.com/ngeorgj/fast-flask/raw/master/origin/'

    """
    FAST FLASK SCRIPT
    Flask made easy (yes, more than it already is).

    The script gets data from the '/Origin/' folder in the fast-flask Repository
    
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

    available_os = {
        'AIX': 'aix',
        'Linux': 'linux',
        'Windows': 'win32',
        'macOS': 'darwin'}

    def __init__(self):
        self.os = ""
        self.root = ""
        self.get_os()

    def get_os(self):
        if sys.platform.startswith('aix'):
            self.os = self.available_os['AIX']
        elif sys.platform.startswith('linux'):
            self.os = self.available_os['Linux']
        elif sys.platform.startswith('win32'):
            self.os = self.available_os['Windows']
        elif sys.platform.startswith('darwin'):
            self.os = self.available_os['macOS']
        self.root = os.getcwd()
        print("User Operational System: " + self.os)

    thread_list = []

    def thread_add(self, function):
        thread = threading.Thread(target=function)
        self.thread_list.append(thread)
        thread.start()

    # Command Line
    def line(self, what):
        os.system(f'{what}')

    def create_folder(self, folder_name):
        os.system(f'mkdir {folder_name}')

    # Navigation
    def go_to_folder(self, dir_name=""):
        """
        Leaving go_to_folder(empty) will lead to root dir

        :param dir_name: directory you want to move
        """
        os.chdir(self.root + '\\' + dir_name)

    # Go to Root Directory
    def root_dir(self):
        self.line('cd ' + self.root)

    # File Handling & Creation
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

    def read_file(self, filename):  # For debug purposes only...
        file = os.getcwd() + "\\" + filename
        file = open(file, 'r')
        file = file.read()
        print(file)

    def get_code_from_github(self, filename, source):
        """
        This will get data from the "Origin" Folder inside the main repository.
        *This part was tricky.
        """
        code = urllib.request.urlopen(source)
        code = code.read()
        code = str(code, encoding='utf-8')  # MAJOR BUG in the project already.
        code = code.replace('\n', '')  # replaces whitespaces with nothing
        code = code.replace('\n\n', '\n')  # replaces double whitespaces with one whitespace and this solves a BIG BUG.
        self.create_file(filename, code)

    def get_html_from_github(self, filename, source):
        """
        This will get data from the "Origin" Folder inside the main repository.
        *This part was tricky.
        """
        code = urllib.request.urlopen(source)
        code = code.read()
        code = str(code, encoding='utf-8')  # MAJOR BUG in the project already.
        # code = code.replace('\n', '')
        # code = code.replace('\n\n', '\n')
        self.create_file(filename, code)

    # Ask about running test server
    def test_server(self):
        """
        Last question to user, asking if it wants to test the server 127.0.0.1:5000/
        """
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
        Application Basic Files

                                                    [root]
                                                      +  [Templates]
                                                      +  [Static]
                                                      +  app.py
                                                      +  models.py
                                                      +  database.db

        """

        # Creates 2 folders [templates, static]
        self.create_folder('templates')
        self.create_folder('static')

        # Creates the database file
        self.new_empty_file('database.db', 8000)

        # Creates 'app.py' and 'models.py'
        self.get_code_from_github('app.py', self.github + 'app.py')
        self.get_code_from_github('models.py', self.github + 'models.py')

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

        # Enters 'templates' folder and creates 1 file and 3 folders [base.html, auth, index, admin]
        self.go_to_folder('templates')
        self.get_html_from_github('base.html', self.github + 'templates/base.py')
        self.create_folder('auth')
        self.create_folder('index')
        self.create_folder('admin')

        # Enters 'templates/index' folder and creates 1 file [index.html]
        self.go_to_folder('templates/index')
        self.get_html_from_github('index.html', self.github + 'templates/index/index.py')

        # Enters 'templates/admin' folder and creates 1 file [admin.html]
        self.go_to_folder('templates/admin')
        self.get_html_from_github('admin.html', self.github + 'templates/admin/admin.py')

        # Enters 'templates/auth' folder and creates 2 files [login.html, register.html]
        self.go_to_folder('templates/auth')
        self.get_html_from_github('login.html', self.github + 'templates/auth/login.py')
        self.get_html_from_github('register.html', self.github + 'templates/auth/register.py')

        # Goes back to Root folder
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

        # Enters 'static' folder and creates 2 folders [css, js]
        self.go_to_folder('static')
        self.create_folder('css')
        self.create_folder('js')

        # Enters 'static/css' folder and creates 2 files [custom.css, auth.css]
        self.go_to_folder('static/css')
        self.get_html_from_github('custom.css', self.github + 'static/css/custom.py')
        self.get_html_from_github('auth.css', self.github + 'static/css/auth.py')

        # Enters 'static/js' folder and creates 1 file [custom.js]
        self.go_to_folder('static/js')
        self.get_html_from_github('custom.js', self.github + 'static/js/custom.py')

        # Goes back to root folder
        self.go_to_folder()
        os.system('cls')

    # Run FastFlask Application
    def run(self):
        self.thread_add(self.create_root())
        self.thread_add(self.create_templates())
        self.thread_add(self.create_static())
        print(" Flask Minified Project Created Successfully\n")
        self.test_server()


# Let's Run
fastflask = FastFlask()
fastflask.run()

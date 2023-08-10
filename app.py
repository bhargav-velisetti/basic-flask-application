from datetime import timedelta
import json 
from flask import Flask, render_template, redirect, session
from utils import db_utility,saml_auth,app_utility


app = Flask(__name__)
app_config = json.load(open('config/app_config.json'))

app.config['SECRET_KEY'] = 'xxxxxxxxx'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=app_config["session_timeout"]["value"])
    
@app.route('/')
def login():
    if app_config["deployment_mode"]["value"] == "DEV":
       # return  "Open Home Page"
        return render_template('home.html')
    else:
        session.permanent = True
        return saml_auth.authenticate()
  
@app.route('/home')
def home_page():
    return redirect('/')

@app.route('/home/db_section')
def db_page1():
    return render_template('db_section.html')

@app.route('/home/db_section/create_db_user')
def db_page2():
    db_list = ['DEV_DB','UAT_DB','PRD_DB']
    return db_utility.create_db_user(db_list)

@app.route('/home/db_section/reset_db_user_password')
def db_page3():
    return db_utility.reset_db_user_password()

@app.route('/home/db_section/grant_access_to_db_user')
def db_page4():
    return db_utility.grant_access_to_db_user()

@app.route('/home/app_section')
def app_page1():
    return render_template('app_section.html')

@app.route('/home/app_section/create_app_user')
def app_page2():
    return app_utility.create_app_user()

@app.route('/home/app_section/reset_app_user_password')
def app_page3():
    return app_utility.reset_app_user_password()

@app.route('/home/app_section/change_status')
def app_page4():
    return app_utility.change_status()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050, debug=True)

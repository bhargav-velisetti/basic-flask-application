from flask import render_template

def create_db_user(db_list : list):
    return render_template('create_db_user.html', db_list=db_list)

def reset_db_user_password():
    return 'Reset DB user paswword based on given inputs'

def grant_access_to_db_user():
    return 'Granting roles to DB users based on given input'
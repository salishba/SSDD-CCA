#!/usr/bin/env python3
 

import json
import os
from flask import Flask


 
from utils import bcrypt, getUUID,mail
from models import getJson, login_manager,db
 

    


login_manager.login_view='users.login'
login_manager.login_message='you need login to access this page'
login_manager.login_message_category='info'

with open( 'config.json', 'r') as c:
    params = json.load(c)["params"]

# params=[]

def get_or_create_secret_key():
    """Load persistent SECRET_KEY or create one and save it."""
    secret_file = os.path.join(os.path.dirname(__file__), 'instance', '.secret_key')
    if os.path.exists(secret_file):
        with open(secret_file, 'r') as f:
            return f.read().strip()
    else:
        os.makedirs(os.path.dirname(secret_file), exist_ok=True)
        secret_key = getUUID()
        with open(secret_file, 'w') as f:
            f.write(secret_key)
        return secret_key
   
def create_app():
    secret_key = get_or_create_secret_key()
    app = Flask("Blog")
    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SECURE=False,
        SESSION_COOKIE_SAMESITE='Lax',
    )
    local_server = params["local_server"]
    if (local_server):
        app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    app.config['SQLALCHEMY_BINDS'] = {
    # Configuration for the second database
    'site_db': 'sqlite:///site.db'}
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
        default_mail_params = {
            'gmail-user': '',
            'gmail-password': '',
            'mail_port': 465,
            'mail_ssl': True,
            'mail_server': 'smtp.gmail.com'
        }
        default_admin_params = {
            'admin_user': 'admin@example.com',
            'admin_password': 'admin'
        }
        mail_params=getJson('mail') or default_mail_params
        admin_params=getJson('admin') or default_admin_params
    app.config.update(
    params=params,
    mail_params=mail_params,
    admin_params=admin_params,
    SECRET_KEY=secret_key,
    MAIL_SERVER=mail_params['mail_server'],
    MAIL_PORT=mail_params['mail_port'],
    MAIL_USE_SSL=mail_params['mail_ssl'],
    MAIL_USERNAME=mail_params['gmail-user'],
    MAIL_PASSWORD=mail_params['gmail-password']
    )
    mail.init_app(app) 
    bcrypt.init_app(app)
    from users.routes import users
    from posts.routes import posts
    from main.routes import main
    from admin.routes import admin
    from errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(errors)

    @app.after_request
    def add_security_headers(response):
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' https://use.fontawesome.com https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://maxcdn.bootstrapcdn.com https://cdn.jsdelivr.net; font-src 'self' https://fonts.gstatic.com"
        return response

    return app

 

 










 
 













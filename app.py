'''
Created on 
    March 21, 2022

Course work: 
    Article Editor

@author: Sivaraam , Elakia

Source:
    
'''

# Import necessary modules
from flask import Flask
from routes.post import post_pages
from sqlmodel import SQLModel, create_engine
from models.post import Post

def create_app():
    app = Flask(__name__)

    app.engine = create_engine("sqlite:///database.db")

    @app.before_first_request
    def create_db():
        SQLModel.metadata.create_all(app.engine)

    app.register_blueprint(post_pages)

    return app

def startpy():
    create_app()
    pass

if __name__ == '__main__':
    startpy()
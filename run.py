from app import app
from Alchemy import banco
from flask import Flask

def create_app(): 
    app = Flask(__name__)
    banco.init_app(app)
    return app

if __name__ == "__main__":  
    app.run()


from app import app
from Alchemy import banco

banco.init_app(app)
banco.create_all()

if __name__ == "__main__":  
    app.run()


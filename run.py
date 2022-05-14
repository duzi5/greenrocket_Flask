from app import app
from Alchemy import banco


if __name__ == "__main__":  
    
    banco.init_app(app)
    banco.create_all()
    app.run()


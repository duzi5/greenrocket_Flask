from app import app
from Alchemy import banco

if __name__ == "__main__":  
    app.run()
    banco.create_all()


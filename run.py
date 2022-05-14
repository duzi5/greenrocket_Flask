from app import app
from Alchemy import banco




banco.init_app(app)

if __name__ == "__main__":  
    app.run()
  





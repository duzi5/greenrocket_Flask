
from app import app
from Alchemy import banco




banco.init_app(app)
with app.app_context():
    banco.init_app(app)
    banco.create_all()


if __name__ == "__main__":  
    app.run(debug = True)
    website_url = 'financas.localhost:5000'
    app.config['SERVER_NAME'] = website_url 
    app.url_map.default_subdomain = "www"






if __name__ == "__main__":
    from Alchemy import banco
    from app import app
    banco.init_app(app)
    app.run(debug = True, port = 2000 )


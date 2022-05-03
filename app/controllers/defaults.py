from app import app

@app.route('/index')
def index():
    return render_template('index.html')


    
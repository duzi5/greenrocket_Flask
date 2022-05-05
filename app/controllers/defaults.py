from doctest import run_docstring_examples
from string import octdigits
from Alchemy import banco
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.before_first_request
def criabanco(): 
    banco.create_all()

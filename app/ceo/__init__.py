from flask import Flask, Blueprint
from .controllers.ceoController import ceoController

ceo = Blueprint('ceo', __name__, url_prefix = 'ceo', template_folder='./pages', static_folder='./static')


ceo.route('/')(ceoController)
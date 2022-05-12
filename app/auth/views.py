from . import auth
from app import api
from app.resources.usuarios import UserLogin


api.add_resource(UserLogin, '/login')


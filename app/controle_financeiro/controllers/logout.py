from ..controllers import current_user
from flask_login import logout_user


def logout(): 
    logout_user()
    return("Você foi deslogado, volte sempre!")
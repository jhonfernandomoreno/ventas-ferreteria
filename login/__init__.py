from flask import Blueprint

login=Blueprint('inicio',__name__,template_folder="templates", static_folder='static')
from . import acceso

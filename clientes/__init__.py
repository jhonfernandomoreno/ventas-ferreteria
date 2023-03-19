from flask import Blueprint

cliente=Blueprint('clientes',__name__,template_folder="templates", static_folder='static')
from . import clientes
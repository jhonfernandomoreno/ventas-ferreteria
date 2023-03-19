from flask import Blueprint

vendedores=Blueprint('vendedores',__name__,template_folder="templates", static_folder='static')
from . import vendedor
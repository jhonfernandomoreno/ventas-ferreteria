from flask import Blueprint

facturacion=Blueprint('factura',__name__,template_folder="templates", static_folder='static')
from . import factura
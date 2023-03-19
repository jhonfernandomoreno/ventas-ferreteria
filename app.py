from flask import Flask, render_template
from login import login
from clientes import cliente
from dashboard import dashboard
from factura import facturacion
from productos import productos
from vendedores import vendedores
from flask_babel import Babel
import locale

def get_locale():
    lugar , hora = locale.getdefaultlocale()
    return lugar

app = Flask(__name__)
app.secret_key = b'7\x82\xdd\xb7\xf4(\xb9B]\xe3\xdb-\xa5\xb6q\x94'
app.config['BABEL_DEFAULT_LOCAL'] = 'es'
babel = Babel(app, locale_selector=get_locale)

app.register_blueprint(login)
app.register_blueprint(cliente)
app.register_blueprint(dashboard)
app.register_blueprint(facturacion)
app.register_blueprint(productos)
app.register_blueprint(vendedores)

@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'),404

@app.route('/acerca-de')
def acercade():
    return render_template('acercade.html')

if __name__ == '__main__':
    app.run(debug=True)

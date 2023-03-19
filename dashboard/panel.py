from flask import render_template, request, session,redirect
from . import dashboard


@dashboard.route('/dashboard')
def dash():
    return render_template("dashboard.html")

@dashboard.route('/dashboard-vendedor')
def dash_ven():
    return render_template("dashboard_vendedor.html")

@dashboard.before_request
def validar_sesion():
    ruta = request.path
    if 'rol' not in session:
        return redirect('/')
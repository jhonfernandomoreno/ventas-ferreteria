from flask import render_template, request, session, redirect, flash
from . import login
from controller import *

@login.route('/', methods=["GET","POST"])
def inicio():
    try:
        if request.method == 'POST':
            usuario=request.form['usr']
            clave=request.form['password']
            user=selectUser(usuario)
            print(user)
            if user != "":
                pw=find_password(user)
                rol=find_role(user)
                print(pw)
                if pw == clave:
                    session['rol']=rol
                    session['nombre']=usuario
                    print(session)
                    if session['rol'] =='admin':
                        return redirect('/dashboard')
                    else:
                        return redirect('/dashboard-vendedor')
                else:
                    print("Contraseña incorrecta")
                    mensaje="Contraseña incorrecta intente nuevamente"
                    return render_template('inicio.html',mensaje=mensaje,rol=rol)
    except Exception:
        mensaje="Usuario o contraseña incorrecto"
    return render_template("inicio.html")

@login.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect("/")


        
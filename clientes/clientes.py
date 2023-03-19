from flask import render_template, request, session, redirect, abort
from . import cliente
from controller import add_cliente, listar, search, borrar

@cliente.route('/clientes')
def clientes():
    return render_template("clientes.html")

@cliente.route('/clientes/agregar-cliente', methods=['GET','POST'])
def agregar_cli():
    titulo="Agregar Clientes"
    mensaje=False
    try:
        if request.method == 'POST':
            id=request.form.get('codigo_cli')
            nombre=request.form.get('nombre_cli')
            direccion=request.form.get('direccion_cli')
            telefono=request.form.get('telefono_cli')
            add_cliente(id, nombre, direccion, telefono)
            mensaje=True
            return render_template("agregar_cliente.html",titulo=titulo,mensaje=mensaje)
    except Exception:
        abort(404)
    return render_template("agregar_cliente.html",titulo=titulo,mensaje=mensaje)    
    
@cliente.route('/clientes/modificar-cliente/<int:dato>', methods=['GET','POST'])
def modificar_cliente(dato=0):
    titulo="Modificar Cliente"
    bandera=False
    datos=search(tabla="cliente", id_search="id_cli",id=dato)
    print(datos)
    try:
        if request.method == 'POST':
            id_cli=request.form['id_cli']
            nom_cli=request.form['nom_cli']
            dir_cli=request.form['dir_cli']
            tel_cli=request.form['tel_cli']
            borrar(tabla="cliente",id_search="id_cli",id=datos[0][0])
            add_cliente(id_cli,nom_cli,dir_cli,tel_cli)
            bandera = True
            datos=search(tabla="cliente", id_search="id_cli",id=id_cli)
            return render_template('modificar_cliente.html', datos=datos, titulo=titulo, bandera=bandera)
    except Exception:
        abort(404)
    return render_template('modificar_cliente.html', datos=datos, titulo=titulo,  bandera=bandera)

@cliente.route('/clientes/listar-cliente')
@cliente.route('/clientes/listar-cliente/<int:page>')
def listar_cliente(page=0):
    page = 10*page
    titulo="Listar Cliente"
    try:
        dato=listar(tabla="cliente",item=page)
        return render_template('listar_cliente.html',dato=dato, titulo=titulo)
    except Exception:
        return abort(404)

@cliente.before_request
def validar_sesion():
    if 'rol' not in session:
        return redirect('/')
    
@cliente.route('/cliente/buscar-cliente', methods=['GET','POST'])
def buscar_cliente():
    titulo= "Buscar Cliente"
    bandera=False
    try:
        if request.method == 'POST':
            prod = request.form.get('buscar_cli')
            print(prod)
            dato=search(tabla="cliente", id_search="id_cli",id=prod)
            print(dato)
            if dato != "":
                bandera=True
                return redirect(f'/clientes/modificar-cliente/{prod}')
    except Exception:
        abort(404)
    return render_template('search_cli.html', titulo=titulo, bandera=bandera)
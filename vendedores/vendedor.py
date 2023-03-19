from flask import render_template, request,session,redirect, abort
from . import vendedores
from controller import listar, add_vendedor, search, borrar

@vendedores.route('/vendedor')
def vendedor():
    return render_template("trabajadores.html")

@vendedores.route('/vendedor/agregar-vendedor', methods=['GET','POST'])
def agregar_vendedor():
    titulo="Agregar Vendedor"
    mensaje=False
    try:
        if request.method == 'POST':
            id=request.form.get('id_ven')
            nombre=request.form.get('nom_ven')
            apellido=request.form.get('ape_ven')
            direccion=request.form.get('dir_ven')
            telefono=request.form.get('tel_ven')
            add_vendedor(id, nombre,apellido, direccion, telefono)
            mensaje=True
            return render_template("agregar_trabajador.html",titulo=titulo,mensaje=mensaje)
    except Exception:
        abort(404)
    return render_template("agregar_trabajador.html",titulo=titulo,mensaje=mensaje)

@vendedores.route('/vendedor/modificar-vendedor/<int:dato>', methods=['GET','POST'])
def modificar_vendedor(dato=0):
    titulo="Modificar Cliente"
    bandera=False
    datos=search(tabla="vendedor", id_search="id_ven",id=dato)
    print(datos)
    try:
        if request.method == 'POST':
            id_ven=request.form['id_ven']
            nom_ven=request.form['nom_ven']
            ape_ven=request.form['ape_ven']
            dir_ven=request.form['dir_ven']
            tel_ven=request.form['tel_ven']
            borrar(tabla="cliente",id_search="id_cli",id=datos[0][0])
            add_vendedor(id_ven,nom_ven,ape_ven,dir_ven,tel_ven)
            bandera = True
            datos=search(tabla="vendedor", id_search="id_ven",id=id_ven)
            return render_template('modificar_trabajador.html', datos=datos, titulo=titulo, bandera=bandera)
    except Exception:
        abort(404)
    return render_template('modificar_trabajador.html', datos=datos, titulo=titulo,  bandera=bandera)

@vendedores.route('/vendedor/listar-vendedor')
@vendedores.route('/vendedor/listar-vendedor/<int:page>')
def listar_trabajador(page=0):
    page=10*page
    titulo="Listar Vendedor"
    try:
        dato=listar(tabla="vendedor",item=page)
        return render_template('listar_trabajadores.html',dato=dato, titulo=titulo)
    except Exception:
        return abort(404)

@vendedores.route('/vendedor/buscar-vendedor', methods=['GET','POST'])
def buscar_ven():
    titulo= "Buscar Vendedor"
    bandera=False
    try:
         if request.method == 'POST':
            prod = request.form.get('buscar_ven')
            print(prod)
            dato=search(tabla="vendedor", id_search="id_ven",id=prod)
            print(dato)
            if dato :
                return redirect(f'/vendedor/modificar-vendedor/{prod}')
            else:
                bandera=True
                return render_template('search_ven.html', titulo=titulo, bandera=bandera)
    except Exception:
        abort(404)
    return render_template('search_ven.html', titulo=titulo, bandera=bandera)
    
@vendedores.before_request
def validar_sesion():
    ruta = request.path
    if 'rol' not in session:
        return redirect('/') 
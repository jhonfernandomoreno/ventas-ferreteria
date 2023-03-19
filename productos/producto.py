from flask import render_template, request,session,redirect,abort
from . import productos
from controller import add_prod, listar,search, borrar

@productos.route('/productos')
def prod():
    return render_template("productos.html")

@productos.route('/productos/agregar-producto', methods=['GET','POST'])
def agregar_prod():
    titulo="Agregar Producto"
    mensaje=False
    try:
       if request.method == 'POST':
            id=request.form['id_prod']
            detalle=request.form['det_prod']
            cantidad=request.form['cant_prod']
            pre_compra=request.form['precio_compra']
            pre_venta=request.form['precio_venta']
            add_prod(id, detalle, cantidad, pre_compra, pre_venta)
            mensaje=True
            return render_template('agregar_producto.html',titulo=titulo, mensaje=mensaje)
    except Exception:
        abort(404)
    return render_template('agregar_producto.html',titulo=titulo, mensaje=mensaje)

@productos.route('/productos/modificar-producto/<int:dato>', methods=['GET','POST'])
def modificar_prod(dato=0):
    titulo="Modificar producto"
    bandera=False
    datos=search(tabla="producto", id_search="id_prod",id=dato)
    print(datos)
    try:
        if request.method == 'POST':
            id=request.form['id_prod']
            detalle=request.form['det_prod']
            cantidad=request.form['cant_prod']
            pre_compra=request.form['precio_compra']
            pre_venta=request.form['precio_venta']
            borrar(tabla="producto",id_search="id_prod",id=datos[0][0])
            add_prod(id,detalle,cantidad,pre_compra,pre_venta)
            bandera = True
            datos=search(tabla="producto", id_search="id_prod",id=id)
            return render_template('modificar_producto.html', datos=datos, titulo=titulo, bandera=bandera)
    except Exception:
        abort(404)
    return render_template('modificar_producto.html', datos=datos, titulo=titulo,  bandera=bandera)

@productos.route('/productos/buscar-producto', methods=['GET','POST'])
def buscar_prod():
    titulo= "Buscar Producto"
    bandera=False
    try:
        if request.method == 'POST':
            prod = request.form.get('buscar_pro')
            print(prod)
            dato=search(tabla="producto", id_search="id_prod",id=prod)
            print(dato)
            if dato != "":
                bandera=True
                return redirect(f'/productos/modificar-producto/{prod}')
    except Exception:
        abort(404)
    return render_template('search_prod.html', titulo=titulo, bandera=bandera)    

@productos.route('/productos/listar-productos')
@productos.route('/productos/listar-productos/<int:page>')
def listar_prod(page=0):
    page = 10*page
    titulo="Listar Productos"
    try:
        dato=listar(tabla="producto",item=page)
        return render_template('listar_productos_u.html',dato=dato, titulo=titulo)
    except Exception:
        return abort(404)
    
@productos.before_request
def validar_sesion():
    if 'rol' not in session:
        return redirect('/')
    
    
@productos.route('/api/productos/buscar/<int:codigo>')
def api_buscar_prod(codigo=0):
    cod = search(tabla="producto", id_search="id_prod",id=codigo)
    datos = {
        "codigo": cod[0][0],
        "desc": cod[0][1],
        "vUnitario": cod[0][4]
    }
    return datos
from flask import render_template, request, redirect,session,abort
from . import facturacion
from controller import search,add_fac
from datetime import datetime

@facturacion.route('/facturacion/buscar-cliente',methods=['GET','POST'])
def factura():
    titulo= "Buscar Cliente"
    bandera=False
    try:
        if request.method == 'POST':
            prod = request.form.get('buscar_cli')
            print(prod)
            dato=search(tabla="cliente", id_search="id_cli",id=prod)
            print(dato)
            if dato :
                bandera=True
                return redirect(f'/facturacion/factura/{prod}')
            else:
                return redirect('/clientes/agregar-cliente')
    except Exception:
        abort(404)
    return render_template('search.html', titulo=titulo, bandera=bandera)

@facturacion.route('/facturacion/factura/<int:dato>',methods=['GET','POST'])
def factura_electronica(dato=0):
    bandera=False
    now = datetime.now()
    dia=now.day
    mes=now.month
    anio=now.year
    if now.day in range(9):
        dia=f'0{now.day}'
    if now.month in range(9):
        mes=f'0{now.month}'
    fecha={'dia': dia, 'mes': mes, 'anio': anio}
    print(fecha)
    print(mes)
    cliente=search(tabla="cliente", id_search="id_cli",id=dato)
    try:
        if request.method == 'POST':
            detalles = request.get_json()
            for value in detalles:
                add_fac(value['factura'],value['cantidad'],value['codigo'], value['vUnitario'], value['subtotal'],dato)
            bandera=True
            return redirect('/facturacion/buscar-cliente')
    except Exception:
        abort(404)
    return render_template('factura_electronica.html',fecha=fecha, cliente=cliente,bandera=bandera)    
        


@facturacion.before_request
def validar_sesion():
    if 'rol' not in session:
        return redirect('/')
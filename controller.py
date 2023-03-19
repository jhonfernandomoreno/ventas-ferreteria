import sqlite3

def dbacces(frase):
    conn = sqlite3.connect('dbFerreteria.db')
    cursor= conn.cursor()
    cursor.execute(frase)
    conn.commit()
    dato=cursor.fetchall()
    cursor.close
    return dato

def selectUser(name):
    consusr=f'SELECT id_ven FROM vendedor where nom_ven="{name}";'
    dato=dbacces(consusr)
    return dato[0][0]

def find_password(user):
    conspw=f'SELECT pass_usr FROM usuario where id_user="{user}";'
    dato=dbacces(conspw)
    return dato[0][0]

def add_prod(id,detalle,cantidad, pre_compra, pre_venta):
    agregar=f'INSERT INTO producto VALUES ({id},"{detalle}",{cantidad},{pre_compra},{pre_venta});'
    dbacces(agregar)
    return f'el producto {id} se encuentra registrado'

def listar(tabla, item):
    listar=f'SELECT * FROM {tabla} LIMIT 10 OFFSET {item};'
    dato=dbacces(listar)
    return dato

def search(tabla,id_search, id):
    buscar=f'SELECT * FROM "{tabla}" WHERE "{id_search}"={id};'
    dato=dbacces(buscar)
    return dato

def modifi_client():
    pass

def add_vendedor(id, nombre, apellido, direccion,telefono):
    agregar=f'INSERT INTO vendedor VALUES ({id},"{nombre}","{apellido}","{direccion}","{telefono}");'
    dbacces(agregar)
    return f'el vendedor {id} se encuentra registrado'

def borrar(tabla,id_search,id):
    cadena=f'DELETE FROM "{tabla}" WHERE "{id_search}"={id};'
    dbacces(cadena)
    return f'El dato ha sido borrado'

def find_role(user):
    consusr=f'SELECT rol FROM usuario where id_user="{user}";'
    dato=dbacces(consusr)
    return dato[0][0]

def add_cliente(id, nombre, direccion, telefono):
    agregar=f'INSERT INTO cliente VALUES ("{id}","{nombre}","{direccion}","{telefono}");'
    dbacces(agregar)
    return f'el cliente {id} se encuentra registrado'

def add_fac(id_fac,cant,id_prod,val_unit,val_total,id_cli):
    agregar=f'INSERT INTO factura VALUES ({id_fac},{cant},{id_prod},{val_unit},{val_total},"{id_cli}");'
    dbacces(agregar)
    return f'La factura {id} se encuentra registrada'
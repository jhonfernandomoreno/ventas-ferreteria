const inputCodigo = document.getElementById("inputcodigo");
const formDetalle = document.getElementById("formDetalle");
const basePath = "http://localhost:5000/api";
const cedula = document.getElementById("inputcedula");
const idfactura = document.getElementById("inputNoFactu");

let total = 0;
const productos = []

formDetalle.addEventListener('submit', async(e) => {
    e.preventDefault();
    const codigoProd = e.target.elements.inputcodigo.value;
    console.log(codigoProd);
    // validaciones
    if (codigoProd == undefined || codigoProd == "") {
        alert("Ingrese un codigo");
    } else {
        // consulta
        const response = await fetch(`${basePath}/productos/buscar/${codigoProd}`);
        const json = await response.json();
        // validar si el producto existe 
        if (json.error) {
            alert("No se encontro el producto ");
        } else {
            console.log("El producto es: ", json);
            // obtener cantidad
            const cantidad = e.target.elements.inputcantidad.value;

            // construimos producto
            const producto = {
                    factura: idfactura.value,
                    cantidad: cantidad,
                    codigo: json.codigo,
                    desc: json.desc,
                    vUnitario: json.vUnitario,
                    subtotal: cantidad * json.vUnitario
                }
                // agregar el producto si existe
            productos.push(producto);
            renderizarProducto(producto);
            actualizarTotal(producto);
        }

    }
});

function actualizarTotal() {
    //recorrer productos
    // sumar cantidad * v unitario
    let ttotal = document.getElementById('totalfin');
    let total = 0;
    productos.forEach((prod) => {
        total += prod.vUnitario * prod.cantidad;
        ttotal.value = total;

    });
    //mostrar total
}

function renderizarProducto(prod) {
    const bodyTabla = document.getElementById("cuerpotabla");
    const tr = document.createElement("tr");
    let tdCant = document.createElement("td");
    tdCant.textContent = prod.cantidad
    tr.appendChild(tdCant);

    let tdDesc = document.createElement("td");
    tdDesc.textContent = prod.desc
    tr.appendChild(tdDesc);

    let tdVUnit = document.createElement("td");
    tdVUnit.textContent = prod.vUnitario
    tr.appendChild(tdVUnit);

    let tdSubtotal = document.createElement("td");
    tdSubtotal.textContent = prod.subtotal
    tr.appendChild(tdSubtotal);

    bodyTabla.appendChild(tr)

}

async function enviardata() {
    const response = await fetch(`http://localhost:5000/facturacion/factura/${cedula.value}`, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(productos) // body data type must match "Content-Type" header
    });
    if (response.ok == true) {
        alert("La Compra ha sido satisfactoria")
        location.replace('http://localhost:5000/facturacion/buscar-cliente');
    }
}
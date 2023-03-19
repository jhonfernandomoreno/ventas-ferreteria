const formDetalle = document.getElementById("formDetalle");
const inputcantidad = document.getElementById("inputcantidad");
const inputdescripcion = document.getElementById("inputdescripcion");
const inputunitario = document.getElementById("inputunitario");
const inputtotal = document.getElementById("inputtotal");
const cuerpotabla= document.getElementById("cuerpotabla");

let arregloDetalle = [];

const redibujartabla = () =>{
    cuerpotabla.innerHTML="";
    arregloDetalle.forEach((detalle) => {
        let fila = document.createElement("tr");
        fila.innerHTML=`<td>${detalle.cant}</td>
                        <td>${detalle.descripcion}</td>
                        <td>${detalle.unitario}</td>
                        <td>${detalle.total}</td>`;
        let tdeliminar = document.createElement("td");
        let botoneliminar=document.createElement("button");
        botoneliminar.classList.add("btn","btn-danger");
        botoneliminar.innerText="Eliminar";
        tdeliminar.appendChild(tdeliminar);
        fila.appendChild(tdeliminar);
        cuerpotabla.appendChild(fila);

    }); 
};

formDetalle.onsubmit = (e) =>{
    e.preventDefault();
    //creando objeto detalle
    const objdetalle={
        cant: inputcantidad.value,
        descripcion: inputdescripcion.value,
        unitario: inputunitario.value,
        total: inputtotal.value,
    };
    arregloDetalle.push(objdetalle);
    redibujartabla();
};

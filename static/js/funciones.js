function validarCampo() {
    let campo = document.getElementById("mibuscar").value;
    if (campo.length == 0 || /^\s+$/.test(campo)) {
        alert("El campo no puede estar vacio");
        return false;
    } else {
        return true;
    }
}
const clave = "inventario-demo-productos-v1";
const form = document.querySelector("#producto-form");
const lista = document.querySelector("#productos");
const mensaje = document.querySelector("#mensaje");
const buscar = document.querySelector("#buscar");
let productos = [];

try {
  const guardados = JSON.parse(localStorage.getItem(clave) || "[]");
  if (Array.isArray(guardados)) productos = guardados;
} catch {
  mensaje.textContent = "No fue posible leer los productos guardados en este navegador.";
}

function guardar() {
  try {
    localStorage.setItem(clave, JSON.stringify(productos));
    return true;
  } catch {
    mensaje.textContent = "No fue posible guardar los productos en este navegador.";
    return false;
  }
}

function mostrar() {
  lista.replaceChildren();
  const consulta = buscar.value.trim().toLocaleLowerCase();
  const visibles = productos.filter(p =>
    String(p.codigo).toLocaleLowerCase().includes(consulta) ||
    String(p.nombre).toLocaleLowerCase().includes(consulta)
  );
  document.querySelector("#vacio").textContent = visibles.length ? "" : "No hay productos para mostrar.";
  visibles.forEach(producto => {
    const fila = document.createElement("tr");
    [producto.codigo, producto.nombre, `$${Number(producto.precio).toFixed(2)}`, producto.existencia].forEach(valor => {
      const celda = document.createElement("td");
      celda.textContent = valor;
      fila.append(celda);
    });
    const celda = document.createElement("td");
    const boton = document.createElement("button");
    boton.type = "button";
    boton.className = "delete";
    boton.textContent = "Eliminar";
    boton.addEventListener("click", () => {
      const anteriores = productos;
      productos = productos.filter(p => p.codigo !== producto.codigo);
      if (!guardar()) productos = anteriores;
      mostrar();
    });
    celda.append(boton);
    fila.append(celda);
    lista.append(fila);
  });
}

form.addEventListener("submit", event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const datos = new FormData(form);
  const codigo = datos.get("codigo").trim();
  const nombre = datos.get("nombre").trim();
  const precio = Number(datos.get("precio"));
  const existencia = Number(datos.get("existencia"));
  if (!codigo || !nombre || !Number.isFinite(precio) || precio < 0 || !Number.isInteger(existencia) || existencia < 0) {
    mensaje.textContent = "Completa los campos con valores válidos.";
    return;
  }
  if (productos.some(p => p.codigo.toLocaleLowerCase() === codigo.toLocaleLowerCase())) {
    mensaje.textContent = "Ya existe un producto con ese código.";
    return;
  }
  productos.push({ codigo, nombre, precio, existencia });
  if (!guardar()) {
    productos.pop();
    return;
  }
  mensaje.textContent = "Producto agregado en este navegador.";
  form.reset();
  mostrar();
});
buscar.addEventListener("input", mostrar);
mostrar();

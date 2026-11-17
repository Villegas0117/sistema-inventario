# sistema-inventario
Sistema web para la gestión de inventarios de un comercio electrónico.

## Demostración web

La rama `produccion` incluye una interfaz Flask para mostrar la clase `Producto`.
La interfaz permite agregar, buscar y eliminar productos **solo en el navegador**
mediante `localStorage`: no utiliza base de datos ni comparte información entre
usuarios o dispositivos. Los datos pueden perderse al borrar los datos del navegador.
No hay autenticación y no debe utilizarse para información real o sensible.

### Ejecutar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -t . -v
flask --app app run
```

Abrir `http://127.0.0.1:5000`. El producto de ejemplo se crea desde
`src/producto.py`; los productos agregados en la interfaz son demostrativos y
permanecen en el navegador, no en el servidor.

### Desplegar en Render

1. En Render, seleccionar **New > Blueprint** y conectar el repositorio.
2. Seleccionar la rama `produccion` que contiene `render.yaml`.
3. Revisar que el servicio `sistema-inventario-demo` use el plan Free y crear el Blueprint.
4. Esperar a que terminen la instalación, las pruebas y el despliegue; abrir la URL
   `onrender.com` asignada por Render.
5. Comprobar el producto de ejemplo y agregar, buscar y eliminar un producto.

El archivo `render.yaml` instala dependencias, ejecuta pruebas antes de iniciar
Gunicorn y escucha en el puerto asignado por Render. El plan gratuito puede
suspenderse por inactividad y tardar en responder al reactivarse; consultar los
límites vigentes de la cuenta. Crear el Blueprint requiere acceso a Render y puede
estar sujeto a las condiciones de la plataforma.

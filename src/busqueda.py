def buscar_producto_por_codigo(productos, codigo):
    """Devuelve el primer producto con el código indicado o None si no existe."""
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None

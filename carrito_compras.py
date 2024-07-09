# Diccionario de productos disponibles (solo como ejemplo)
productos_disponibles = {
    'Arroz 15Kg': {'precio': 100.0, 'stock': 50},
    'Gasesosa Pepsi 3L': {'precio': 12.0, 'stock': 50},
    'Ron Cartavio': {'precio': 80.0, 'stock': 50},
}

# Carrito de compras (inicialmente vacío)
carrito = []

def agregar_producto_al_carrito(producto, cantidad):
    """
    Agrega un producto al carrito de compras.
    """
    if producto in productos_disponibles and cantidad <= productos_disponibles[producto]['stock']:
        carrito.append({'producto': producto, 'cantidad': cantidad})
        productos_disponibles[producto]['stock'] -= cantidad
        print(f"{cantidad} unidades de {producto} agregadas al carrito.")
        return True
    else:
        print(f"No hay suficiente stock de {producto}.")
        return False

def mostrar_carrito():
    """
    Muestra el contenido actual del carrito de compras.

    """
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Contenido del carrito:")
        total = 0.0
        for item in carrito:
            producto = item['producto']
            cantidad = item['cantidad']
            precio_unitario = productos_disponibles[producto]['precio']
            subtotal = precio_unitario * cantidad
            total += subtotal
            print(f"Producto: {producto}, Cantidad: {cantidad}, Precio unitario: ${precio_unitario}, Subtotal: ${subtotal}")
        print(f"Total del carrito: ${total}")

mostrar_carrito()

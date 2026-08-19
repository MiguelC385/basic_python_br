class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total_inventario(self):
        return self.precio * self.cantidad

mi_producto = Producto("Tablet", 3500, 3)

total = mi_producto.calcular_total_inventario()

print(f"Producto: {mi_producto.nombre}")
print(f"Cantidad: {mi_producto.cantidad}")
print(f"Precio unitario: {mi_producto.precio}")
print(f"Valor total del inventario: {total}")
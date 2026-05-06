# Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [["Mozarella", 24, 9000], ["Leche", 12, 3800], ["Cereal", 20, 2000]]
# Definir actualizar_precio(producto, nuevo_precio)
def actualizar_precio(producto, nuevo_precio):
    for i in inventario:
        if i[0] == producto:
            i[0] = producto
            i[2] = nuevo_precio
            return  
    print("producto no encontrado")
        
# Definir registrar_venta(producto, cantidad)
def registrar_venta(producto, cantidad):
    for i in inventario:
        
        if i[0] == producto and i[1] >= cantidad:
            i[1] = i[1] - cantidad
            print(f"Venta registrada: se compro {producto} \n Cantidad: {cantidad}")
            return
    print("Producto no encontrado o cantidad insuficiente")
        
 
# Definir anadir_producto(producto, cantidad, precio)
def añadir_producto(producto,cantidad,precio=1000):
    for i in inventario:
       if i[0] == producto:
            print("producto ya en existencias")
            return
    inventario.append([producto, cantidad, precio])
    print(f"producto añadido: {producto} - cantidad: {cantidad} - precio: {precio}")

# Definir mostrar_inventario()
def mostrar_inventario():
    for i in inventario:
        print(i)

# Llamar a actualizar_precio con el segundo producto
actualizar_precio("Leche", 1880)
# Llamar a registrar_venta con el primer producto
registrar_venta("Mozarella", 3)
# Llamar a anadir_producto con un producto nuevo
añadir_producto("Pan", 2000, 7800)
# Llamar a mostrar_inventario
mostrar_inventario()
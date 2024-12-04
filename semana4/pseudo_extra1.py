precio_de_producto = int(input("Ingrese el precio del producto para calcular su descuento "))
if(precio_de_producto < 100):
    descuento = int(precio_de_producto * 0.98)
else: descuento = int(precio_de_producto * 0.90)
print(f"El nuevo precio con el descuento es de {descuento}")
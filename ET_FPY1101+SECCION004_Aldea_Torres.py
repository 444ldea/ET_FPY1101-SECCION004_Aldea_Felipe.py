# productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]}

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],

productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

def stock_marca(marca):
    marca = marca.lower()
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower == marca:
            if modelo in stock:
                total += stock[modelo][1]
                print(f"el stock total es: {total}")

def busqueda_precio(p_min, p_max):
    busqueda = []
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            busqueda = modelo.append(f"{marca}-{modelo}")
            if busqueda:
                for item in sorted(busqueda):
                    print(item)
            else:
                print("no se encontró.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
    



#menu principal

while True:
    print("*** MENU PRINCIPAL***")
    print("1. Stock marca.\n2. Busqueda por precio.\n3. Actualizar precio.\n4. Salir.")
    opcion = input("ingrese opcion: ")
    if opcion == "1":
        stock_marca(marca)
    elif opcion == "2":
        while True:
            try:
                p_min = int(input("ingrese precio minimo: "))
                p_max = int(input("ingrese precio maximo: "))
            except ValueError:
                print("debe ingresar valores enteros")
        busqueda_precio(precio)
    elif opcion == "3":
        actualizar_precio()
    elif opcion == "4":
        print("programa finalizado.")
        break
    else:
        print("opcion invalida")
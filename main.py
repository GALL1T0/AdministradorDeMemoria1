# Espacios de memoria disponibles
espacios_de_memoria = {
    1: 1000,
    2: 400,
    3: 1800,
    4: 700,
    5: 900,
    6: 1200,
    7: 2000,
}


# Función para asignar espacio de memoria utilizando el algoritmo de primer ajuste
def primer_ajuste(archivo):
    for espacio, tamaño in espacios_de_memoria.items():
        if tamaño >= archivo["tamaño"]:
            return espacio
    return None


# Función para asignar espacio de memoria utilizando el algoritmo de mejor ajuste
def mejor_ajuste(archivo):
    mejor_espacio = None
    for espacio, tamaño in espacios_de_memoria.items():
        if tamaño >= archivo["tamaño"]:
            if mejor_espacio is None or tamaño < espacios_de_memoria[mejor_espacio]:
                mejor_espacio = espacio
    return mejor_espacio


# Función para asignar espacio de memoria utilizando el algoritmo de peor ajuste
def peor_ajuste(archivo):
    peor_espacio = None
    for espacio, tamaño in espacios_de_memoria.items():
        if tamaño >= archivo["tamaño"]:
            if peor_espacio is None or tamaño > espacios_de_memoria[peor_espacio]:
                peor_espacio = espacio
    return peor_espacio


# Función para asignar espacio de memoria utilizando el algoritmo de siguiente ajuste
def siguiente_ajuste(archivo, ultimo_espacio):
    espacios_disponibles = list(espacios_de_memoria.keys())
    if ultimo_espacio is None:
        ultimo_espacio = espacios_disponibles[0]
    else:
        ultimo_espacio_index = espacios_disponibles.index(ultimo_espacio)
        espacios_disponibles = espacios_disponibles[ultimo_espacio_index:] + espacios_disponibles[:ultimo_espacio_index]

    for espacio in espacios_disponibles:
        tamaño = espacios_de_memoria[espacio]
        if tamaño >= archivo["tamaño"]:
            return espacio
    return None


# Función principal para asignar archivos a memoria
def asignar_archivos():
    archivos = []
    with open("archivos.txt", "r") as archivo_txt:
        lineas = archivo_txt.readlines()
        for linea in lineas:
            nombre, tamaño = linea.strip().split(", ")
            tamaño = int(tamaño[:-2])
            archivos.append({"nombre": nombre, "tamaño": tamaño})

    ultimo_espacio_siguiente_ajuste = None  # Variable para llevar un registro del último espacio usado en Siguiente Ajuste

    while True:
        print("\nAlgoritmos de administración de memoria disponibles:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        print("5. Salir")

        opcion = int(input("Seleccione un algoritmo (1/2/3/4/5): "))
        if opcion == 5:
            break

        if opcion < 1 or opcion > 4:
            print("Opción no válida. Intente nuevamente.")
            continue

        algoritmo = None
        if opcion == 1:
            algoritmo = primer_ajuste
        elif opcion == 2:
            algoritmo = mejor_ajuste
        elif opcion == 3:
            algoritmo = peor_ajuste
        elif opcion == 4:
            algoritmo = lambda archivo: siguiente_ajuste(archivo, ultimo_espacio_siguiente_ajuste)

        for archivo in archivos:
            espacio = algoritmo(archivo)
            if espacio is not None:
                print(f"Archivo '{archivo['nombre']}' asignado al espacio {espacio} de {archivo['tamaño']} kb.")
                del espacios_de_memoria[espacio]
                if algoritmo == siguiente_ajuste:
                    ultimo_espacio_siguiente_ajuste = espacio
            else:
                print(f"No hay espacio suficiente para el archivo '{archivo['nombre']}' de {archivo['tamaño']} kb.")
# ...


if __name__ == "__main__":
    asignar_archivos()

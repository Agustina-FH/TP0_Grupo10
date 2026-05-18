def buscar_posicion (lista, elemento):
    for posicion in range(len(lista)):
        if lista[posicion] == elemento:
            return posicion


def baja_peliula(codigos, titulos, generos, directores, paises, años, clasificaciones):
    codigo = int(input("Ingrese el codigo de la pelicula: "))
    while codigo not in codigos:
        print("El codigo ingresado no se encuentra en los registros.")
        codigo = int(input("Ingrese el codigo de la pelicula: "))
    posicion = buscar_posicion(codigos, codigo)
    print("Titulo: ", titulos[posicion])
    print("Genero: ", generos[posicion])
    print("Director: ", directores[posicion])
    print("Pais de Origen: ", paises[posicion])
    print("Año de Publicacion: ", años[posicion])
    print("Clasificacion: ", clasificaciones[posicion])
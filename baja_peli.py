def buscar_posicion (lista, elemento):
    for posicion in range(len(lista)):
        if lista[posicion] == elemento:
            return posicion


def datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion):
    datos_pelicula = []

    datos_pelicula.append(codigos[posicion])
    datos_pelicula.append(titulos[posicion])
    datos_pelicula.append(generos[posicion])
    datos_pelicula.append(directores[posicion])
    datos_pelicula.append(paises[posicion])
    datos_pelicula.append(años[posicion])
    datos_pelicula.append(clasificaciones[posicion])

    return datos_pelicula


def baja_peliula(codigos, titulos, generos, directores, paises, años, clasificaciones):
    continuar = True
    while continuar:
        codigo = int(input("Ingrese el codigo de la pelicula: "))
        while codigo not in codigos:
            print("El codigo ingresado no se encuentra en los registros.")
            codigo = int(input("Ingrese el codigo de la pelicula: "))

        posicion = buscar_posicion(codigos, codigo)
        pelicula = datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion)

        for dato in pelicula:
            print(dato)

        print("¿Desea dar de baja esta pelicula? (S/N)").upper()
        opcion = input("Ingrese su respuesta: ")
        while opcion != "S" or opcion != "N":
            print("Respuesta invalida")
            print("¿Desea dar de baja esta pelicula? (S/N)").upper()
        opcion = input("Ingrese su respuesta: ")

        if opcion == "S":
            codigos.pop(posicion)
            titulos.pop(posicion)
            generos.pop(posicion)
            directores.pop(posicion)
            paises.pop(posicion)
            años.pop(posicion)
            clasificaciones.pop(posicion)
            print("Eliminacion exitosa.")

        else:
            print("¿Desea volver al menu principal? (S/N)").upper()
            op = input("Ingrese su respuesta: ")
            if op == "N":
                continuar = False

    print("Volviendo al menu principal..")
    
        



    


from Main import opcion_seleccionada

#FUNCIONES AUX

def no_numeros(string):
    numeros = "123456789"
    hay = False
    letra = 0
    while not hay and letra < len(string):
        if letra in numeros:
            hay = True
        letra += 1
    return hay

def buscar_posicion(lista, elemento):
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



#OPCION 1

def alta_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas):
    vacio = ""

    codigo = int(input("Ingrese el codigo de la pelicula: "))
    while codigo not in codigos and codigo >= 0:
        if codigo < 0:
            print("Invalido: no puede ser negativo.")
        else:
            print("El codigo ingresado ya se encuentra en los registros.")
        codigo = int(input("Ingrese el codigo de la pelicula: "))
    codigos.append(codigo)

    titulo = input("Ingrese el titulo de la pelicula: ")
    while titulo == vacio:
        print("Invalido: no puede ser vacio.")
        titulo = input("Ingrese el titulo de la pelicula: ")
    titulos.append(titulo)

    genero = input("Ingrese el genero de la pelicula: ")
    while genero == vacio:
        print("Invalido: no puede ser vacio.")
        titulo = input("Ingrese el genero de la pelicula: ")
    generos.append(genero)

    director = int(input("Ingrese el director de la pelicula: "))
    while no_numeros(director) and director == vacio:
        if director == vacio:
            print("Invalido: no puede ser vacio.")
        else:
            print("Invalido: no se permiten numeros")
        director = int(input("Ingrese el director de la pelicula: "))
    directores.append(director)

    pais = int(input("Ingrese el pais de origen de la pelicula: "))
    while no_numeros(pais) and pais == vacio:
        if pais == vacio:
            print("Invalido: no puede ser vacio.")
        else:
            print("Invalido: no se permiten numeros")
        pais = int(input("Ingrese el pais de origen de la pelicula: "))
    paises.append(pais)

    año = int(input("Ingrese el año de publicacion: "))
    while año < 1900:
        print("Invalido: no debe ser menor a 1900.")
        año = int(input("Ingrese el año de publicacion: "))
    años.append(año)

    clasificacion = input("Ingrese la clasificacion por edad de la pelicula: ")
    while clasificacion not in clasif_validas:
        print("Invalido: no se encuentra entre las clasificaciones validas.")
        clasificacion = input("Ingrese la clasificacion por edad de la pelicula: ")
    clasificaciones.append(clasificacion)
    


#OPCION 2
def sub_menu_modf(datos_peli):
    for posicion in range(1,len(datos_peli)):
        print(posicion+1,":",datos_peli[posicion])


def modificarPelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas):
    codigo = int(input("Ingrese el codigo de la pelicula: "))
    while codigo not in codigos:
        print("El codigo ingresado ya se encuentra en los registros.")
        codigo = int(input("Ingrese el codigo de la pelicula: "))
    
    posicion = buscar_posicion[codigos, codigo]
    pelicula = datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion)
    print("Mofidicar...")
    sub_menu_modf(pelicula)
    opcion = opcion_seleccionada(1,len(pelicula))

    if opcion == 1:
        titulo=input("Inese el nuevo titulo: ")
        while no_numeros(titulo):
            print("El titulo no puede contener numeros")
            titulo=input("Inese el nuevo titulo: ")
        titulos[posicion]=titulo

    if opcion == 2:
        genero=input("Ingrese el nuevo genero:")
        while no_numeros(genero):
            print("El genero no puede contener numeros")
            genero=input("Ingrese el nuevo genero:")
        generos[posicion]=genero

    if opcion == 3:
        director=input("Ingrese el nuevo director:")
        while no_numeros(director):
            print("El director no puede contener numeros")
            director=input("Ingrese el nuevo director:")
        directores[posicion]=director

    if opcion == 4:
        pais=input("Ingrese el nuevo pais:")
        while no_numeros(pais):
            print("El pais no puede contener numeros")
            pais=input("Ingrese el nuevo pais:")
        paises[posicion]=pais

    if opcion == 5:
        año=int(input("Ingrese el nuevo año:"))
        while año<1900: 
            print("El año debe ser mayor a 1900")
            año=int(input("Ingrese el nuevo año:"))
        años[posicion]=año

    if opcion == 6:
        clasificacion=input("Ingrese la nueva clasificacion:")
        while clasificacion not in clasif_validas:
            print("La clasificacion no es valida")
            clasificacion=input("Ingrese la nueva clasificacion:")
        clasificaciones[posicion]=clasificacion


#OPCION 3


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
    
        


    

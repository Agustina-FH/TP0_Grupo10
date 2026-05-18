def no_numeros(string):
    numeros = "123456789"
    hay = False
    letra = 0
    while not hay and letra < len(string):
        if letra in numeros:
            hay = True
        letra += 1
    return hay


def alta_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones):
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

    clasif_valida = ["ATP", "APTO13", "APTO16", "APTO16"]
    clasificacion = input("Ingrese la clasificacion por edad de la pelicula: ")
    while clasificacion not in clasif_valida:
        print("Invalido: no se encuentra entre las clasificaciones validas.")
        clasificacion = input("Ingrese la clasificacion por edad de la pelicula: ")
    clasificaciones.append(clasificacion)
    



    
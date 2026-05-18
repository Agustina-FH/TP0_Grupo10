def no_numeros(string):
    numeros = "123456789"
    hay = False
    letra = 0
    while not hay and letra < len(string):
        if letra in numeros:
            hay = True
        letra += 1
    return hay

def modificarPelicula(codigos, titulos, generos, directores, paises, años, clasificaciones):
    cod=int(input("Ingrese el codigo de la pelicula a modificar(-1 para finalizar):"))
    if cod in codigos:
        for i in range(len(codigos)):
            if codigos[i]==cod:
                posicion=i
        titulo=input("Inese el nuevo titulo:")
        while no_numeros(titulo):
            print("El titulo no puede contener numeros")
            titulo=input("Inese el nuevo titulo:")
        titulos[posicion]=titulo
        genero=input("Ingrese el nuevo genero:")
        while no_numeros(genero):
            print("El genero no puede contener numeros")
            genero=input("Ingrese el nuevo genero:")
        generos[posicion]=genero
        director=input("Ingrese el nuevo director:")
        while no_numeros(director):
            print("El director no puede contener numeros")
            director=input("Ingrese el nuevo director:")
        directores[posicion]=director
        pais=input("Ingrese el nuevo pais:")
        while no_numeros(pais):
            print("El pais no puede contener numeros")
            pais=input("Ingrese el nuevo pais:")
        paises[posicion]=pais
        año=int(input("Ingrese el nuevo año:"))
        while año<1900: 
            print("El año debe estar entre 1888 y 2024")
            año=int(input("Ingrese el nuevo año:"))
        clasificacion=input("Ingrese la nueva clasificacion:")
        clasificacionesPermitidas=[ "ATP", "APTO13", "APTO16" , "APTO18" ]
        while clasificacion not in clasificacionesPermitidas:
            print("La clasificacion no es valida")
            clasificacion=input("Ingrese la nueva clasificacion:")
        clasificaciones[posicion]=clasificacion

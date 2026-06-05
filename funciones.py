#FUNCIONES MENU

def opciones_menu():
    """Muestra las opciones del menu. Autor/a: Fernandez Haisner Agustina"""
    print("1: Alta de pelicula")
    print("2: Modificacion de pelicula")
    print("3: Baja de pelicula")
    print("4: Listado general")
    print("5: Buscar por codigo")
    print("6: Ordenar listado por año de publicacion")
    print("7: Listar peliculas por genero")
    print("8: Salir")


def opcion_seleccionada(primeraOP, ultimaOP):
    """Permite seleccionar opciones dentro de un rango introducido. Autor/a: Fernandez Haisner Agustina"""
    op = int(input("Ingrese la accion que desea llevar acabo: "))

    while op < primeraOP or op > ultimaOP:
        print("Valor fuera de rango")
        op = int(input("Ingrese la accion que desea llevar acabo: "))
    
    return op



#FUNCIONES AUX

def hay_numeros(string):
    """Revisa si en un string se escribieron numeros. Autor/a: Fernandez Haisner Agustina"""
    numeros = "123456789"
    hay = False
    letra = 0
    while not hay and letra < len(string):
        if string[letra] in numeros:
            hay = True
        letra += 1
    return hay


def buscar_posicion(lista, elemento):
    """Busca la posición de un elemento en una lista. Autor/a: Fernandez Haisner Agustina"""
    for posicion in range(len(lista)):
        if lista[posicion] == elemento:
            return posicion


def datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion):
    """Agrega los datos de una pelicula a una lista y devuelve la lista. Autor/a: Fernandez Haisner Agustina"""
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
    """Permite agregar peliculas con sus datos a las respectivas listas. Autor/a: Fernandez Haisner Agustina"""
    continuar = True
    while continuar:
        vacio = ""

        codigo = int(input("Ingrese el codigo de la pelicula que desea agregar: "))
        while codigo in codigos or codigo < 0:
            if codigo < 0:
                print("Invalido: no puede ser negativo.")
            else:
                print("El codigo ingresado ya se encuentra en los registros.")
            codigo = int(input("Ingrese el codigo de la pelicula que desea agregar: "))
        codigos.append(codigo)

        titulo = input("Ingrese el titulo de la pelicula: ")
        while titulo == vacio:
            print("Invalido: no puede ser vacio.")
            titulo = input("Ingrese el titulo de la pelicula: ")
        titulos.append(titulo)

        genero = input("Ingrese el genero de la pelicula: ")
        while genero == vacio:
            print("Invalido: no puede ser vacio.")
            genero = input("Ingrese el genero de la pelicula: ")
        generos.append(genero)

        director = input("Ingrese el director de la pelicula: ")
        while hay_numeros(director) or director == vacio:
            if director == vacio:
                print("Invalido: no puede ser vacio.")
            else:
                print("Invalido: no se permiten numeros")
            director = int(input("Ingrese el director de la pelicula: "))
        directores.append(director)

        pais = input("Ingrese el pais de origen de la pelicula: ")
        while hay_numeros(pais) or pais == vacio:
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

        print("Se dio de alta la pelicula exitosamente.")
        op = input("¿Desea volver al menu principal? (S/N): ").upper()
        while op != "S" and op != "N":
            print("Respuesta invalida")
            op = input("¿Desea volver al menu principal? (S/N): ").upper()
        if op == "S":
            continuar = False

    print("Volviendo al menu principal..")


#OPCION 2
def sub_menu_modf(datos_peli):
    """Permite ver los datos de la pelicula en forma de indice para seleccionar el dato a cambiar. Autor/a: Fernandez Haisner Agustina"""
    for posicion in range(1,len(datos_peli)):
        print(posicion,":",datos_peli[posicion])


def modificar_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas):
    """Permite modificar el dato seleccionado de la pelicula. Autor/a: Saffioti Martín"""
    continuar = True
    while continuar:
        codigo = int(input("Ingrese el codigo de la pelicula que desea modificar: "))
        while codigo not in codigos:
            print("El codigo ingresado no se encuentra en los registros.")
            codigo = int(input("Ingrese el codigo de la pelicula que desea modificar: "))
        
        posicion = buscar_posicion(codigos, codigo)
        pelicula = datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion)
        print("Mofidicar...")
        sub_menu_modf(pelicula)
        opcion = opcion_seleccionada(1,len(pelicula))

        if opcion == 1:
            titulo=input("Inese el nuevo titulo: ")
            while hay_numeros(titulo):
                print("El titulo no puede contener numeros")
                titulo=input("Inese el nuevo titulo: ")
            titulos[posicion]=titulo

        if opcion == 2:
            genero=input("Ingrese el nuevo genero:")
            while hay_numeros(genero):
                print("El genero no puede contener numeros")
                genero=input("Ingrese el nuevo genero: ")
            generos[posicion]=genero

        if opcion == 3:
            director=input("Ingrese el nuevo director: ")
            while hay_numeros(director):
                print("El director no puede contener numeros")
                director=input("Ingrese el nuevo director: ")
            directores[posicion]=director

        if opcion == 4:
            pais=input("Ingrese el nuevo pais: ")
            while hay_numeros(pais):
                print("El pais no puede contener numeros")
                pais=input("Ingrese el nuevo pais: ")
            paises[posicion]=pais

        if opcion == 5:
            año=int(input("Ingrese el nuevo año: "))
            while año<1900: 
                print("El año debe ser mayor a 1900")
                año=int(input("Ingrese el nuevo año: "))
            años[posicion]=año

        if opcion == 6:
            clasificacion=input("Ingrese la nueva clasificacion: ")
            while clasificacion not in clasif_validas:
                print("La clasificacion no es valida")
                clasificacion=input("Ingrese la nueva clasificacion: ")
            clasificaciones[posicion]=clasificacion
        
        print("Modificacion exitosa.")
        op = input("¿Desea volver al menu principal? (S/N): ").upper()
        while op != "S" and op != "N":
            print("Respuesta invalida")
            op = input("¿Desea volver al menu principal? (S/N): ").upper()
        if op == "S":
            continuar = False

    print("Volviendo al menu principal..")


#OPCION 3
def baja_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones):
    """Permite dar de baja una pelicula con doble confirmación. Autor/a: Fernandez Haisner Agustina"""
    continuar = True
    while continuar:
        codigo = int(input("Ingrese el codigo de la pelicula que desea eliminar: "))
        if codigo not in codigos:
            print("El codigo ingresado no se encuentra en los registros.")
            
        else:
            posicion = buscar_posicion(codigos, codigo)
            pelicula = datos_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, posicion)

            for dato in pelicula:
                print(dato)

            opcion = input("¿Desea dar de baja esta pelicula? (S/N): ").upper()
            while opcion != "S" and opcion != "N":
                print("Respuesta invalida")
                opcion = input("¿Desea dar de baja esta pelicula? (S/N): ").upper()

            if opcion == "S":
                codigos.pop(posicion)
                titulos.pop(posicion)
                generos.pop(posicion)
                directores.pop(posicion)
                paises.pop(posicion)
                años.pop(posicion)
                clasificaciones.pop(posicion)
                print("Eliminacion exitosa.")

        op = input("¿Desea volver al menu principal? (S/N): ").upper()
        while op != "S" and op != "N":
            print("Respuesta invalida")
            op = input("¿Desea volver al menu principal? (S/N): ").upper()
        if op == "S":
            continuar = False

    print("Volviendo al menu principal..")
    
        
#OPCION 4
def listado_general(codigos, titulos, generos, directores, paises, años, clasificaciones):
    """Permite ver el listado de todas las peliculas. Autor/a: Fernandez Haisner Agustina"""
    for posicion in range(len(codigos)):
        print(codigos[posicion],"|",titulos[posicion],"|",generos[posicion],"|",directores[posicion],"|",paises[posicion],"|",años[posicion],"|",clasificaciones[posicion])
    
    print("Volviendo al menu principal..")


#OPCION 5
def buscarCodigo (codigos, titulos, generos, directores, paises, años, clasificaciones,dato_solicitado):
    """Se le ingresa un codigo como dato, busca secuencialmente donde esta y da todos los datos de la pelicula. Autor: Saffioti Martín"""
    continuar = True
    while continuar:
        i=0
        existe = False
        while i < len(codigos) and not existe:
            if codigos[i] == dato_solicitado:
                existe = True
            else:
                i += 1
    
        if not existe:
            print("La pelicula no existe")
        else:
            print("La pelicula existe")
            print(f"Codigo:{codigos[i]}")
            print(f"Titulo:{titulos[i]}")
            print(f"Genero:{generos[i]}")
            print(f"Director/a:{directores[i]}")
            print(f"Pais:{paises[i]}")
            print(f"Año:{años[i]}")
            print(f"Clasificiacion:{clasificaciones[i]}")

        seguir = input("¿Desea volver al menu principal? (S/N): ").upper()
        while seguir != "S" and seguir != "N":
            print("Respuesta invalida")
            seguir = input("¿Desea volver al menu principal? (S/N): ").upper()
        if seguir == "S":
            continuar = False


#OPCION 6
def ordenamiento_año(lista_año, lista_titulo):
    """Ordena las peliculas en base a sus años de lanzamiento y los muestra (metodo utilizado: seleccion). Autor: Perez Lautaro Agustin"""
    for i in range(0, len(lista_año)-1):
        for j in range(i+1, len(lista_año)):
            if lista_año[i] > lista_año[j]:
                aux = lista_año[i]
                lista_año[i] = lista_año[j]
                lista_año[j] = aux
                aux_titulo = lista_titulo[i]
                lista_titulo[i] = lista_titulo[j]
                lista_titulo[j] = aux_titulo
    print("Peliculas ordenadas por año de publicacion: ")
    for i in range(len(lista_año)):
        print(f"{lista_año[i]} - {lista_titulo[i]}")


#OPCION 7
def pelis_genero(titulos, generos):
    """Permite mostrar las peliculas de un genero seleccionado. Autora: Fernandez Haisner Agustina""" 
    continuar = True
    while continuar:
        genero = input("Ingrese el genero que desea buscar: ")
        if genero not in generos:
            print("No se encontraron peliculas de ese genero.")
        else:
            print(f"Peliculas del genero {genero}: ")
            for i in range(len(generos)):
                if generos[i] == genero:
                    print(titulos[i])

        op = input("¿Desea volver al menu principal? (S/N): ").upper()
        while op != "S" and op != "N":
            print("Respuesta invalida")
            op = input("¿Desea volver al menu principal? (S/N): ").upper()
        if op == "S":
            continuar = False

    print("Volviendo al menu principal..")

#Documentación: Martín Saffioti

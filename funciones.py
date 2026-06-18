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
    print("8: Reporte Matricial por Genero y Clasificaciones")
    print("9: Reporte Estadistico General")
    print("10: Reporte Matricial por Año y País")
    print("11: Salir")


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
    numeros = ["1","2","3","4","5","6","7","8","9"]
    hay = False
    letra = 0
    while not hay and letra < len(string):
        if buscar_posicion(numeros,string[letra]) != -1:
            hay = True
        letra += 1
    return hay


def buscar_posicion(lista, elemento):
    """Busca la posición de un elemento en una lista. Autor/a: Fernandez Haisner Agustina"""
    posicion = -1
    pos = 0
    while posicion == -1 and pos < len(lista):
        if lista[pos] == elemento:
            posicion = pos
        pos += 1
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
        while buscar_posicion(codigos,codigo) != -1 or codigo < 0:
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
            director = input("Ingrese el director de la pelicula: ")
        directores.append(director)

        pais = input("Ingrese el pais de origen de la pelicula: ")
        while hay_numeros(pais) or pais == vacio:
            if pais == vacio:
                print("Invalido: no puede ser vacio.")
            else:
                print("Invalido: no se permiten numeros")
            pais = input("Ingrese el pais de origen de la pelicula: ")
        paises.append(pais)

        año = int(input("Ingrese el año de publicacion: "))
        while año < 1900:
            print("Invalido: no debe ser menor a 1900.")
            año = int(input("Ingrese el año de publicacion: "))
        años.append(año)

        clasificacion = input("Ingrese la clasificacion por edad de la pelicula: ")
        while buscar_posicion(clasif_validas, clasificacion) == -1:
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
        print()

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
        while buscar_posicion(codigos,codigo) == -1:
            print("El codigo ingresado no se encuentra en los registros.")
            codigo = int(input("Ingrese el codigo de la pelicula que desea modificar: "))
        print()
        
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
            genero=input("Ingrese el nuevo genero: ")
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
            while buscar_posicion(clasif_validas, clasificacion) == -1:
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
        print()

    print("Volviendo al menu principal..")


#OPCION 3
def baja_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones):
    """Permite dar de baja una pelicula con doble confirmación. Autor/a: Fernandez Haisner Agustina"""
    continuar = True
    while continuar:
        codigo = int(input("Ingrese el codigo de la pelicula que desea eliminar: "))
        if buscar_posicion(codigos,codigo) == -1:
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
        print()

    print("Volviendo al menu principal..")
    
        
#OPCION 4
def listado_general(codigos, titulos, generos, directores, paises, años, clasificaciones):
    """Permite ver el listado de todas las peliculas. Autor/a: Fernandez Haisner Agustina"""
    for posicion in range(len(codigos)):
        print(codigos[posicion],"|",titulos[posicion],"|",generos[posicion],"|",directores[posicion],"|",paises[posicion],"|",años[posicion],"|",clasificaciones[posicion])


#OPCION 5
def buscarCodigo (codigos, titulos, generos, directores, paises, años, clasificaciones):
    """Se le ingresa un codigo como dato, busca secuencialmente donde esta y da todos los datos de la pelicula. Autor: Saffioti Martín"""
    continuar = True
    while continuar:
        dato_solicitado=int(input("Ingrese el codigo que desea buscar: "))
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
        print()

    print("Volviendo al menu principal..")


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
        if buscar_posicion(generos,genero) == -1:
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
        print()

    print("Volviendo al menu principal..")

#OPCION 8
def reporteGeneroClasificacion(generos, clasificaciones, clasif_validas):
    """Muestra un reporte matricial por genero y clasificación de cuantas peliculas hay por cada combinación posible. Autor: Saffioti Martín"""
    matriz=[["GENEROS"]+clasif_validas]
    generos_unicos=[]
    for g in range(len(generos)):
        existe=False
        for i in range(len(generos_unicos)):
            if generos[g]==generos_unicos[i]:
                existe=True
        if existe==False:
            generos_unicos.append(generos[g])
    for f in range(len(generos_unicos)):
        matriz.append([])
        genero=generos_unicos[f]
        matriz[f+1].append(genero)
    
    for f in range(1,len(matriz)):
        for c in range (1,len(matriz[0])):
            cont=0
            for i in range(len(generos)):
                if generos[i]==matriz[f][0] and clasificaciones[i]==matriz[0][c]:
                    cont+=1
            matriz[f].append(cont)
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print("%-12s" % matriz[f][c], end="")
        print()

#OPCION 9
def reporte_estadistico(titulos, generos, paises, años, clasificaciones, clasif_validas):
    """Muestra indicadores estadísticos generales del catálogo usando recorridos, acumuladores y contadores. Autor: Perez Lautaro Agustin"""
    if len(titulos) != 0:

        print("REPORTE ESTADISTICO GENERAL")
        print()
        total = len(titulos)
        print(f"Cantidad total de peliculas: {total}")
        print()

        año_min = años[0]
        titulo_min = titulos[0]
        año_max = años[0]
        titulo_max = titulos[0]
        i = 1
        while i < len(años):
            if años[i] < año_min:
                año_min = años[i]
                titulo_min = titulos[i]
            if años[i] > año_max:
                año_max = años[i]
                titulo_max = titulos[i]
            i += 1
        print("Pelicula mas antigua:")
        print(f" Titulo: {titulo_min}")
        print(f"Año: {año_min}")
        print()
        print("Pelicula mas reciente:")
        print(f"Titulo: {titulo_max}")
        print(f"Año: {año_max}")
        print()

        print("Cantidad por clasificacion:")
        c = 0
        while c < len(clasif_validas):
            cont = 0
            i = 0
            while i < len(clasificaciones):
                if clasificaciones[i] == clasif_validas[c]:
                    cont += 1
                i += 1
            print(f" {clasif_validas[c]}:{cont}")
            c += 1
        print()

        generos_unicos = []
        i = 0
        while i < len(generos):
            existe = False
            j = 0
            while j < len(generos_unicos):
                if generos[i] == generos_unicos[j]:
                    existe = True
                j += 1
            if existe==False:
                generos_unicos.append(generos[i])
            i += 1

        genero_max = generos_unicos[0]
        cont_max = 0
        g = 0
        while g < len(generos_unicos):
            cont = 0
            i = 0
            while i < len(generos):
                if generos[i] == generos_unicos[g]:
                    cont += 1
                i += 1
            if cont > cont_max:
                cont_max = cont
                genero_max = generos_unicos[g]
            g += 1
        print("Genero mas frecuente:")
        print(f"{genero_max}")
        print()

        paises_unicos = []
        i = 0
        while i < len(paises):
            existe = False
            j = 0
            while j < len(paises_unicos):
                if paises[i] == paises_unicos[j]:
                    existe = True
                j += 1
            if not existe:
                paises_unicos.append(paises[i])
            i += 1

        pais_max = paises_unicos[0]
        cont_max = 0
        p = 0
        while p < len(paises_unicos):
            cont = 0
            i = 0
            while i < len(paises):
                if paises[i] == paises_unicos[p]:
                    cont += 1
                i += 1
            if cont > cont_max:
                cont_max = cont
                pais_max = paises_unicos[p]
            p += 1
        print("Pais con mayor cantidad de peliculas:")
        print(f"{pais_max}")
        print()

        acumulador = 0
        i = 0
        while i < len(años):
            acumulador += años[i]
            i += 1
        promedio = acumulador // total
        print("Promedio de años de publicacion:")
        print(f"{promedio}")
    
    else:
        print("No hay peliculas registradas")
    

#Documentación: Martín Saffioti

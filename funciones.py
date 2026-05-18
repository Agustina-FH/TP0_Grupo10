# funciones.py
def altaPelicula(codigos, nombres, genero, director, pais, clasificacion, años):
    cod = int(input("Ingrese codigo (-1 para finalizar): "))
    
    while cod != -1:
        # Validar codigo positivo
        while cod < 0:
            print("Error: El codigo debe ser positivo")
            cod = int(input("Ingrese codigo (-1 para finalizar): "))
        
        # Validar codigo repetido
        while cod in codigos:
            print("Error: Codigo ya existe, intente con otro")
            cod = int(input("Ingrese codigo (-1 para finalizar): "))
        
        # Validar titulo
        nom = input("Ingrese titulo de la pelicula: ")
        while len(nom) == 0:
            print("Error: El titulo no puede estar vacio")
            nom = input("Ingrese titulo de la pelicula: ")
        
        # Validar genero no vacio
        gen = input("Ingrese genero de la pelicula: ")
        while len(gen) == 0:
            print("Error: El genero no puede estar vacio")
            gen = input("Ingrese genero de la pelicula: ")
        
        # Validar director
        dir = input("Ingrese director de la pelicula: ")
        while len(dir) == 0 or any(char.isdigit() for char in dir):
            if len(dir) == 0:
                print("Error: El director no puede estar vacio")
            else:
                print("Error: El director no puede contener numeros")
            dir = input("Ingrese director de la pelicula: ")
        
        # Validar pais
        pa = input("Ingrese pais de origen: ")
        while len(pa) == 0 or any(char.isdigit() for char in pa):
            if len(pa) == 0:
                print("Error: El pais no puede estar vacio")
            else:
                print("Error: El pais no puede contener numeros")
            pa = input("Ingrese pais de origen: ")
        
        # Validar estreno
        año = int(input("Ingrese año de estreno: "))
        while año <= 1900:
            print("Error: El año debe ser mayor a 1900")
            año = int(input("Ingrese año de estreno: "))
        
        # Validar clasificacion
        cla = input("Ingrese clasificacion (ATP, APTO13, APTO16, APTO18): ").upper()
        clasificaciones_validas = ["ATP", "APTO13", "APTO16", "APTO18"]
        while cla not in clasificaciones_validas:
            print("Error: Clasificacion invalida. Opciones validas: ATP, APTO13, APTO16, APTO18")
            cla = input("Ingrese clasificacion (ATP, APTO13, APTO16, APTO18): ").upper()
        
        # Agregar pelicula
        codigos.append(cod)
        nombres.append(nom)
        genero.append(gen)
        director.append(dir)
        pais.append(pa)
        años.append(año)
        clasificacion.append(cla)
        print("Pelicula agregada correctamente\n")
        
        cod = int(input("Ingrese codigo (-1 para finalizar): "))

    def modificarPelicula(codigos, nombres, genero, director, pais, clasificacion, años):
        cod=int(input("Ingrese codigo de la pelicula a modificar: "))
        while cod not in codigos:
            print("Error: Codigo no encontrado, intente nuevamente")
            cod=int(input("Ingrese codigo de la pelicula a modificar: "))
        
        while cod!=-1:
            for i in range(len(codigos)):
                if codigos[i]==cod:
                    print("Pelicula encontrada: ", nombres[i])
                    print("1. Modificar titulo")
                    print("2. Modificar genero")
                    print("3. Modificar director")
                    print("4. Modificar pais")
                    print("5. Modificar año de estreno")
                    print("6. Modificar clasificacion")
                    opcion=int(input("Ingrese una opcion: "))
                    
                    if opcion==1:
                        nom=input("Ingrese nuevo titulo: ")
                        while nom=="":
                            print("Error: El titulo no puede estar vacio")
                            nom=input("Ingrese nuevo titulo: ")
                        nombres[i]=nom
                        print("Titulo modificado correctamente\n")
                    
                    elif opcion==2:
                        gen=input("Ingrese nuevo genero: ")
                        while gen=="":
                            print("Error: El genero no puede estar vacio")
                            gen=input("Ingrese nuevo genero: ")
                        genero[i]=gen
                        print("Genero modificado correctamente\n")
                    
                    elif opcion==3:
                        dir=input("Ingrese nuevo director: ")
                        while dir=="" or any(char.isdigit() for char in dir):
                            if dir=="":
                                print("Error: El director no puede estar vacio")
                            else:
                                print("Error: El director no puede contener numeros")
                            dir=input("Ingrese nuevo director: ")
                        director[i]=dir
                        print("Director modificado correctamente\n")
                    
                    elif opcion==4:
                        pa=input("Ingrese nuevo pais de origen: ")
                        while pa=="" or any(char.isdigit() for char in pa):
                            if pa=="":
                                print("Error: El pais no puede estar vacio")
                            else:
                                print("Error: El pais no puede contener numeros")
                            pa=input("Ingrese nuevo pais de origen: ")
                        pais[i]=pa
                        print("Pais modificado correctamente\n")
                    
                    elif opcion==5:
                        año=int(input("Ingrese nuevo año de estreno: "))
                        while año<=1900:
                            print("Error: El año debe ser mayor a 1900")
                            año=int(input("Ingrese nuevo año de estreno: "))
                        años[i]=año
                        print("Año de estreno modificado correctamente\n")
                    
                    elif opcion==6:
                        cla=input("Ingrese nueva clasificacion (ATP, APTO13, APTO16, APTO18): ").upper()
                        clasificaciones_validas=["ATP", "APTO13", "APTO16", "APTO18"]
                        while cla not in clasificaciones_validas:
                            print("Error: Clasificacion no valida")
                            cla=input("Ingrese nueva clasificacion (ATP, APTO13, APTO16, APTO18): ").upper()
                        clasificacion[i]=cla
                        print("Clasificacion modificada correctamente\n")
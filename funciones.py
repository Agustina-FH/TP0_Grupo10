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

    
    

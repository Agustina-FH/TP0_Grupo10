# funciones.py
def altaPelicula(codigos, nombres, genero, director, pais, clasificacion, años):
    cod = int(input("Ingrese codigo (-1 para finalizar): "))
    
    while cod != -1:
        # Validar que el codigo sea positivo
        while cod < 0:
            print("Error: El codigo debe ser positivo")
            cod = int(input("Ingrese codigo (-1 para finalizar): "))
        
        # Validar que el codigo no sea repetido
        while cod in codigos:
            print("Error: Codigo ya existe, intente con otro")
            cod = int(input("Ingrese codigo (-1 para finalizar): "))
        
        # Validar titulo/nombre no vacio
        nom = input("Ingrese titulo de la pelicula: ").strip()
        while not nom:
            print("Error: El titulo no puede estar vacio")
            nom = input("Ingrese titulo de la pelicula: ").strip()
        
        # Validar genero no vacio
        gen = input("Ingrese genero de la pelicula: ").strip()
        while not gen:
            print("Error: El genero no puede estar vacio")
            gen = input("Ingrese genero de la pelicula: ").strip()
        
        # Validar director no vacio y sin numeros
        dir = input("Ingrese director de la pelicula: ").strip()
        while not dir or any(char.isdigit() for char in dir):
            if not dir:
                print("Error: El director no puede estar vacio")
            else:
                print("Error: El director no puede contener numeros")
            dir = input("Ingrese director de la pelicula: ").strip()
        
        # Validar pais no vacio y sin numeros
        pa = input("Ingrese pais de origen: ").strip()
        while not pa or any(char.isdigit() for char in pa):
            if not pa:
                print("Error: El pais no puede estar vacio")
            else:
                print("Error: El pais no puede contener numeros")
            pa = input("Ingrese pais de origen: ").strip()
        
        # Validar año de estreno mayor a 1900
        año = int(input("Ingrese año de estreno: "))
        while año <= 1900:
            print("Error: El año debe ser mayor a 1900")
            año = int(input("Ingrese año de estreno: "))
        
        # Validar clasificacion
        cla = input("Ingrese clasificacion (ATP, APTO13, APTO16, APTO18): ").strip().upper()
        clasificaciones_validas = ["ATP", "APTO13", "APTO16", "APTO18"]
        while cla not in clasificaciones_validas:
            print("Error: Clasificacion invalida. Opciones validas: ATP, APTO13, APTO16, APTO18")
            cla = input("Ingrese clasificacion (ATP, APTO13, APTO16, APTO18): ").strip().upper()
        
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

    
    
from funciones import *


def main():
  """Genera las listas de los datos. Autor/a: Martín Saffioti"""
  # codigos=[]
  # titulos=[]
  # generos=[]
  # directores=[]
  # paises=[]
  # años=[]
  # clasificaciones=[]

  codigos = [
      101,102,103,104,
      105,106,107,108,
      109,110,111,112,113,114,115,116,117,118
  ]

  titulos = [
      "Drama Uno",
      "Drama Dos",
      "Drama Tres",
      "Drama Cuatro",

      "Comedia Uno",
      "Comedia Dos",
      "Comedia Tres",
      "Comedia Cuatro",

      "Accion Uno",
      "Accion Dos",
      "Accion Tres",
      "Accion Cuatro",
      "Accion Cinco",
      "Accion Seis",

      "Terror Uno",
      "Terror Dos",
      "Terror Tres",
      "Terror Cuatro"
  ]

  generos = [
      "Drama","Drama","Drama","Drama",
      "Comedia","Comedia","Comedia","Comedia",
      "Accion","Accion","Accion","Accion","Accion","Accion",
      "Terror","Terror","Terror","Terror"
  ]

  directores = [
      "Director A","Director B","Director C","Director D",
      "Director E","Director F","Director G","Director H",
      "Director I","Director J","Director K","Director L","Director M","Director N",
      "Director O","Director P","Director Q","Director R"
  ]

  paises = [
      "Argentina","Argentina","España","Mexico",
      "Argentina","España","Mexico","Chile",
      "Estados Unidos","Estados Unidos","Estados Unidos",
      "Canada","Reino Unido","Australia",
      "Argentina","Estados Unidos","España","Mexico"
  ]

  años = [
      2001,2003,2005,2007,
      2010,2011,2012,2013,
      2015,2016,2017,2018,2019,2020,
      2008,2009,2014,2021
  ]

  clasificaciones = [
      # Drama -> 2 ATP, 1 APTO13, 1 APTO18
      "ATP","ATP","APTO13","APTO18",

      # Comedia -> 1 ATP, 2 APTO13, 1 APTO16
      "ATP","APTO13","APTO13","APTO16",

      # Accion -> 1 APTO13, 3 APTO16, 2 APTO18
      "APTO13","APTO16","APTO16","APTO16","APTO18","APTO18",

      # Terror -> 1 ATP, 1 APTO16, 2 APTO18
      "ATP","APTO16","APTO18","APTO18"]

  opciones_menu()
  """Permite seleccionar entre las opciones del menu. Autor/a: Fernandez Haisner Agustina"""
  opcion=opcion_seleccionada(1,10)
  print()
  clasif_validas = ["ATP", "APTO13", "APTO16", "APTO18"]
  while opcion != 10:

    if opcion == 1:
      alta_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas)

    if opcion == 2:
      modificar_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas)

    if opcion == 3:
      baja_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones)

    if opcion == 4:
      listado_general(codigos, titulos, generos, directores, paises, años, clasificaciones)

    if opcion==5:
      buscarCodigo(codigos, titulos, generos, directores, paises, años, clasificaciones)
    
    if opcion==6:
      ordenamiento_año(años, titulos)
    
    if opcion==7:
      pelis_genero(titulos, generos)

    if opcion==8:
      reporteGeneroClasificacion(generos, clasificaciones, clasif_validas)

    if opcion==9:
      reporte_estadistico(titulos, generos, paises, años, clasificaciones, clasif_validas)

    print()
    opciones_menu()
    opcion=opcion_seleccionada(1,10)  
    print()  
  
  print("Saliendo..")
    
main()

#Documentación: Martín Saffioti

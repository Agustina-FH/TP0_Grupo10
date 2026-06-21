from funciones import *


def main():
  """Genera las listas de los datos. Autor/a: Martín Saffioti"""
  codigos=[]
  titulos=[]
  generos=[]
  directores=[]
  paises=[]
  años=[]
  clasificaciones=[]

  opciones_menu()
  """Permite seleccionar entre las opciones del menu. Autor/a: Fernandez Haisner Agustina"""
  opcion=opcion_seleccionada(1,11)
  print()
  clasif_validas = ["ATP", "APTO13", "APTO16", "APTO18"]
  while opcion != 11:

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

    if opcion==10:
      matrizAñoPais(titulos, generos, paises, años, clasificaciones, clasif_validas)

    print()
    opciones_menu()
    opcion=opcion_seleccionada(1,11)  
    print()  
  
  print("Saliendo..")
    
main()

#Documentación: Martín Saffioti

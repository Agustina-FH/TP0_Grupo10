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
  opcion=opcion_seleccionada(1,5)
  while opcion != 5:
    clasif_validas = ["ATP", "APTO13", "APTO16", "APTO18"]

    if opcion == 1:
      alta_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas)

    if opcion == 2:
      modificar_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones, clasif_validas)

    if opcion == 3:
      baja_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones)

    if opcion == 4:
      listado_general(codigos, titulos, generos, directores, paises, años, clasificaciones)

    opciones_menu()
    opcion=opcion_seleccionada(1,5)    
  
  print("Saliendo..")
    
main()

#Documentación: Martín Saffioti

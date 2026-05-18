from funciones import *

def opciones_menu():
    print("1: Alta de pelicula")
    print("2: Modificacion de pelicula")
    print("3: Baja de pelicula")
    print("4: Listado general")
    print("5: Salir")

def opcion_seleccionada(primeraOP, ultimaOP):
    op = int(input("Ingrese la accion que desea llevar acabo: "))

    while op < primeraOP or op > ultimaOP:
        print("Valor fuera de rango")
        op = int(input("Ingrese la accion que desea llevar acabo: "))
    
    return op

def main():
  codigos=[]
  titulos=[]
  generos=[]
  directores=[]
  paises=[]
  años=[]
  clasificaciones=[]

  opciones_menu()
  opcion=opcion_seleccionada(1,5)
  while opcion != 5:
    if opcion==1:
        alta_pelicula(codigos, titulos, generos, directores, paises, años, clasificaciones)
"""
  elif opcion==2:
    modificarPelicula(codigos,nombres,genero,director,pais,clasificacion,años)
  elif opcion==3:
    bajaPelicula(codigos,nombres,genero,director,pais,clasificacion,años)
  elif opcion==4:
    listadoGeneral(codigos,nombres,genero,director,pais,clasificacion,años)
"""

main()
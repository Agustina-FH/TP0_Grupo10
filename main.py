import funciones

def mostrarInicio():
  print("Bienvenido")
  print("1. Alta de Pelicula")
  print("2. Modificación de Pelicula")
  print("3. Baja de Pelicula")
  print("4. Listado General")
  

def main():
  codigos=[]
  nombres=[]
  genero=[]
  director=[]
  pais=[]
  clasificacion=[]
  años=[]
  mostrarInicio():
  opcion=int(input("Ingrese una opcion:"))
  if opcion==1:
    funciones.altaPelicula(codigos, nombres, genero, director, pais, clasificacion, años)
  elif opcion==2:
    funciones.modificarPelicula(codigos,nombres,genero,director,pais,clasificacion,años)
  elif opcion==3:
    funciones.bajaPelicula(codigos,nombres,genero,director,pais,clasificacion,años)
  elif opcion==4:
    funciones.listadoGeneral(codigos,nombres,genero,director,pais,clasificacion,años)

main()
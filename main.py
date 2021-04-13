#Importamos la librería Matplotlib
import matplotlib.pyplot as plt

#Abrimos el documento cargado previamente
mpl1 = open('matplotlib1.txt','r')

#Leemos el contenido del archivo
txt1 = mpl1.readlines()

#Cerramos el archivo
mpl1.close()

#Imprimimos el contenido del archivo
print(txt1)

#Relacionamos con un nombre a cada uno de los datos del archivo
num1 = (txt1[0].rstrip())
num2 = (txt1[1].rstrip())
num3 = (txt1[2].rstrip())
num4 = (txt1[3].rstrip())
num5 = (txt1[4].rstrip())
num6 = (txt1[5].rstrip())

#Convertimos los datos a números enteros
ent1 = int(num1)
ent2 = int(num2)
ent3 = int(num3)
ent4 = int(num4)
ent5 = int(num5)
ent6 = int(num6)

#Creamos una lista con las entradas del archivo ingresado
lista =[ent1,ent2,ent3,ent4,ent5,ent6]

#Imprimimos el contexto de la gráfica 1
print("La rectora de un colegio realizó una encuesta por 6 meses, en donde preguntó a los estudiantes si para ellos su imagen era favorable; a continuación, la cantidad de estudiantes que indicaron una imagen favorable de la rectora")

#Creamos la gráfica
plt.plot(lista,'r')

#Damos nombre al eje X
plt.xlabel ('Voto favorable por la rectora')

#Damos nombre al eje Y
plt.ylabel('Número de estudiantes')

#Establecemos el título de la gráfica
plt.title('Gráfica de votos favorables')

#Guardamos el archivo con un nombre específico
plt.savefig("graficafav.png")

#Cerramos el archivo
plt.close()

#Abrimos el documento cargado previamente
mpl2 = open('malplotlib2.txt','r')

#Leemos el contenido del archivo
txt2 = mpl2.readlines()

#Cerramos el archivo
mpl2.close()

#Imprimimos el contenido del archivo
print(txt2)

#Relacionamos con un nombre a cada uno de los datos del archivo
nume1 = (txt2[0].rstrip('\n'))
nume2 = (txt2[1].rstrip('\n'))
nume3 = (txt2[2].rstrip('\n'))
nume4 = (txt2[3].rstrip('\n'))
nume5 = (txt2[4].rstrip('\n'))
nume6 = (txt2[5].rstrip('\n'))

#Convertimos los datos a números float
ente1 = float(nume1)
ente2 = float(nume2)
ente3 = float(nume3)
ente4 = float(nume4)
ente5 = float(nume5)
ente6 = float(nume6)

#Creamos una lista con las entradas del archivo ingresado
listita = [ente1,ente2,ente3,ente4,ente5,ente6]

#Imprimimos el contexto de la gráfica 2
print("En el colegio se sacaron 3 notas a lo largo de 2 meses y queremos comparar los datos de mi prima con los míos; estos son los siguientes: ")

#Creamos la gráfica con dos variables
plt.plot(lista1,'b--', lista2, 'g--')

#Damos nombre al eje X
plt.xlabel ('Mes')

#Damos nombre al eje Y
plt.ylabel('Notas')

#Establecemos el título de la gráfica
plt.title('Notas: Verde: Mis notas. Azul: Las notas de mi prima')

#Guardamos el archivo con un nombre específico
plt.savefig("misnotas.png")

#Cerramos el archivo
plt.close()

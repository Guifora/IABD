import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns
import networkx as nx

#Ejercicio 1B
#Grafico tarta
options = ["1 persona","2 personas","3 personas","4 personas","5 personas","6 personas"]
count = [5,15,20,10,8,2] 
plt.pie(count, labels = options, autopct = "%0.1f%%")
plt.title("Numero de personas que componen una familia")
plt.show()

#Ejercicio 1C
#Diagrama de Barras

options = ["1","2","3","4","5","6"]
count = [5,15,20,10,8,2] 

plt.bar(options, count)
plt.xlabel("Numero de personas")
plt.ylabel("Familias")
plt.title("Numero de personas que componen una familia")
plt.show()

#Ejercicio 11
#Histograma

data = [9,12,6,11,19,5,8,13,2,8,5,12,0,9,4,15,18,10,6,16]
bins = [0, 5, 10, 15, 20]
plt.hist(data,bins=bins, color = "blue", edgecolor = "k")
plt.show()
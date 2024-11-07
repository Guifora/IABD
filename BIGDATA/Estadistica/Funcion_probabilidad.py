import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt

# EJERCICIO 1

media=1.90
desviacion_estandar=0.10

ej1_1=(1-sc.norm.cdf(2,loc=media,scale=desviacion_estandar))

print(f"La probabilidad de que mida mas de 2 metros es: {ej1_1}")

ej1_2=sc.norm.cdf(1.85,loc=media,scale=desviacion_estandar)

print(f"La probabilidad de que mida menos de 1.85 metros es: {ej1_2}")

ej1_3=(sc.norm.cdf(2,loc=media,scale=desviacion_estandar)-ej1_2)

print(f"La probabilidad de que mida entre 1.85 metros y 2 metros es: {ej1_3}")

x = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 100)
y = sc.norm.pdf(x, loc=media, scale=desviacion_estandar)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.fill_between(x, y, alpha=0.2)
plt.title(f'Distribución Normal (Media: {media}, Desviación Estándar: {desviacion_estandar})')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.grid(True)
plt.show()

# EJERCICIO 2

media=3.2
desviacion_estandar=0.5
ej2_1=sc.norm.pdf(3.5,loc=media,scale=desviacion_estandar)
print(f"La probabilidad de que un bebe recien nacido pese exactamente 3.5 kg es: {ej2_1}")
ej2_2=sc.norm.ppf(0.8,loc=media,scale=desviacion_estandar)
print(f"El peso minimo que debe tener un recien  nacido para que el 80% de los bebes pesen menos que el es: {ej2_2}")

# EJERCICIO 3


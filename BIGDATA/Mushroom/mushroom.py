import pandas as pd
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt


pd.set_option('display.max_colwidth', None)
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
x = mushroom.data.features 
y = mushroom.data.targets 

df_mushroom=pd.DataFrame(x)
df_poison=pd.DataFrame(y)

#Agregamos el Dataframe poison al nuestro dataframe de Mushroom
df_mushroom['poisonous'] = df_poison

#Dataframe con las caracteristicas
df_characteristics=mushroom.variables

print(df_mushroom.head(5))

counts = df_mushroom['poisonous'].value_counts()
labels = ['Comestibles' if label == 'e' else 'Venenosas' for label in counts.index]

plt.figure(figsize=(8, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'])
plt.title('Proporción de Setas Venenosas y No Venenosas')
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.show()

#df_mushroom=X
#print(df_mushroom)
# metadata 
#print(mushroom.metadata) 
  
# variable information 
#print(mushroom.variables) 

df_characteristics=mushroom.variables

df_filtrado = df_characteristics.drop(['units', 'demographic'], axis=1)
#df.info()
#df.describe()
#df_filtrado.info()

df_filtrado["role"]=df_filtrado["role"].astype("category")
df_filtrado["type"]=df_filtrado["type"].astype("category")
df_filtrado["name"]=df_filtrado["name"].astype("string")
df_filtrado['missing_values'] = df_filtrado['missing_values'].map({'yes': True, 'no': False})
df_filtrado["missing_values"]=df_filtrado["missing_values"].astype("bool")
print(df_filtrado)
print(df_filtrado.dtypes)
#descriptions = df_filtrado[df_filtrado["name"] == "population"]["description"].tolist()
#for desc in descriptions:
 #   print(desc)

import pandas as pd

# Cargar el archivo CSV original
df = pd.read_csv('Marvel_Movies_Dataset.csv')

# Reemplazar comas por puntos en todas las columnas numéricas
# Es importante asegurarse de que solo las columnas numéricas se vean afectadas
df['IMDb'] = df['IMDb'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['IMDB_Metascore'] = df['IMDB_Metascore'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['RottenTomatoes_Critics'] = df['RottenTomatoes_Critics'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['RottenTomatoes_Audience'] = df['RottenTomatoes_Audience'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['Budget'] = df['Budget'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['Domestic_Gross'] = df['Domestic_Gross'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
df['Worldwide_Gross'] = df['Worldwide_Gross'].apply(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)

# Guardar el archivo corregido
df.to_csv('Marvel_Movies_Dataset_Copy.csv', index=False)

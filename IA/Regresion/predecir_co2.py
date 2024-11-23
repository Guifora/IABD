import joblib
import numpy as np
import pandas as pd

# Intentar cargar el modelo y el preprocesador previamente guardados
try:
    modelo = joblib.load('mejor_modelo_co2.pkl')  # Asegúrate de que el nombre del archivo sea correcto
except FileNotFoundError:
    print("Error: El archivo del modelo 'mejor_modelo_co2.pkl' no se encuentra.")
    exit()  # Salir del programa si el modelo no se encuentra
except Exception as e:
    print(f"Error inesperado al cargar el modelo: {e}")
    exit()  # Salir del programa si ocurre cualquier otro tipo de error

# Función para predecir la clase
def predecir():
    print("Introduce los siguientes valores para realizar la predicción:")
    try:
        Volume = float(input("Ingrese el valor de Volume: "))
        Weight = float(input("Ingrese el valor de Weight: "))
        # Verificar que los valores sean positivos (puedes ajustar esta validación según sea necesario)
        if Volume <= 0 or Weight <= 0:
            raise ValueError("Los valores de Volume y Weight deben ser mayores que 0.")
        
        nueva_muestra = np.array([[Volume, Weight]])
        
        # Realizar la predicción usando el modelo cargado
        prediccion = modelo.predict(nueva_muestra)  # Aquí, el modelo debe manejar el escalado si se usa un pipeline
        print(f"Predicción del CO2 para los valores dados (Volume: {Volume}, Weight: {Weight}): {prediccion[0]}")
        return prediccion
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Llamar a la función para predecir
if __name__ == "__main__":
    predecir()

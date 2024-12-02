import joblib
import numpy as np

# Intentar cargar el modelo y el preprocesador previamente guardados
try:
    modelo = joblib.load('modelo_ej1.pkl')  # Asegúrate de que el nombre del archivo sea correcto
except FileNotFoundError:
    print("Error: El archivo del modelo 'mejor_modelo_co2.pkl' no se encuentra.")
    exit()  # Salir del programa si el modelo no se encuentra
except Exception as e:
    print(f"Error inesperado al cargar el modelo: {e}")
    exit()  # Salir del programa si ocurre cualquier otro tipo de error

def predecir():
    print("Introduce los siguientes valores para realizar la predicción:")
    try:
        anc_petalo = float(input("Escribe la anchura del pétalo: "))
        lar_petalo = float(input("Escribe la largura del pétalo: "))
        anc_sepalo = float(input("Escribe la anchura del sépalo: "))
        lar_sepalo = float(input("Escribe la largura del sépalo: "))
        
        if anc_petalo <= 0 or lar_petalo <= 0 or anc_petalo <= 0 or lar_petalo <= 0 :
            raise ValueError("Los valores de anchura y largura del petalo y sepalo deben ser mayores que 0.")
        nueva_muestra = np.array([lar_sepalo, anc_sepalo, lar_petalo, anc_petalo]).reshape(1, -1)

        predicción = modelo.predict(nueva_muestra)
        target_names = ['setosa', 'versicolor', 'virginica']

        print(f"El tipo de flor es {target_names[predicción[0]]}.")
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    
# Llamar a la función para predecir
if __name__ == "__main__":
    predecir()
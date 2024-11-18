import joblib
import numpy as np

# Cargar el modelo guardado
modelo = joblib.load('mejor_modelo_ridge.pkl')

# Función para pedir al usuario los datos
def pedir_datos():
    print("Por favor, ingresa los siguientes valores para hacer la predicción:")
    
    # Lista de características del dataset (puedes ajustar esto según el dataset)
    features = [
        "Edad (years)",
        "Sexo (0=Femenino, 1=Masculino)",
        "Índice de masa corporal (BMI)",
        "Presión arterial promedio (BP)",
        "Suma de las medidas del tricep (S1)",
        "Nivel de insulina (S2)",
        "Nivel de glucosa (S3)",
        "Medicamento (S4)",
        "Familiares con diabetes (S5)"
    ]
    
    # Recoger los datos ingresados por el usuario
    user_input = []
    for feature in features:
        value = float(input(f"{feature}: "))
        user_input.append(value)
    
    return np.array(user_input).reshape(1, -1)

# Obtener los datos del usuario
X_usuario = pedir_datos()

# Realizar la predicción
prediccion = modelo.predict(X_usuario)

# Mostrar el resultado de la predicción
print(f"\nLa predicción para el progreso de la diabetes es: {prediccion[0]:.2f}")

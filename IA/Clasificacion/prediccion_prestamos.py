import joblib
import pandas as pd

# Cargar el modelo previamente guardado
modelo = joblib.load('mejor_modelo_prestamos.pkl')

# Función para predecir la clase
def predecir():
    # Solicitar datos al usuario
    print("Introduce los siguientes valores para realizar la predicción:")

    int_rate = float(input("Tasa de interés (int_rate): "))
    installment = float(input("Cuota del préstamo (installment): "))
    fico = int(input("Puntaje FICO (fico): "))
    revol_bal = float(input("Balance de crédito Revolving (revol_bal): "))
    revol_util = float(input("Utilización del crédito Revolving (revol_util): "))
    inq_last_6mths = int(input("Consultas de crédito en los últimos 6 meses (inq_last_6mths): "))
    pub_rec = int(input("Registros públicos (pub_rec): "))
    purpose = input("Propósito del préstamo (purpose): ")

    # Crear un DataFrame con los datos ingresados
    # Aquí añadimos las columnas faltantes 'dti' y 'credit.policy', con valores predeterminados (por ejemplo, 0)
    data = pd.DataFrame({
        'int.rate': [int_rate],
        'installment': [installment],
        'fico': [fico],
        'revol.bal': [revol_bal],
        'revol.util': [revol_util],
        'inq.last.6mths': [inq_last_6mths],
        'pub.rec': [pub_rec],
        'purpose': [purpose],
        'dti': [0],  # Valor por defecto para 'dti'
        'credit.policy': [1]  # Valor por defecto para 'credit.policy'
    })

    # Hacer la predicción usando el modelo
    prediccion = modelo.predict(data)

    # Mostrar el resultado de la predicción
    if prediccion == 0:
        print("La predicción es: El préstamo NO será pagado.")
    else:
        print("La predicción es: El préstamo SERÁ pagado.")

# Llamar a la función para predecir
if __name__ == "__main__":
    predecir()
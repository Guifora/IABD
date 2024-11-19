import joblib
import pandas as pd

# Intentar cargar el modelo previamente guardado
try:
    modelo = joblib.load('mejor_modelo_prestamos.pkl')
except FileNotFoundError:
    print("Error: El archivo del modelo 'mejor_modelo_prestamos.pkl' no se encuentra.")
    exit()  # Salir del programa si el modelo no se encuentra
except joblib.externals.loky.process_executor.TerminatedWorkerError:
    print("Error: Hubo un problema al intentar cargar el modelo.")
    exit()  # Salir del programa si hay un error al cargar el modelo
except Exception as e:
    print(f"Error inesperado al cargar el modelo: {e}")
    exit()  # Salir del programa si ocurre cualquier otro tipo de error

# Función para predecir la clase
def predecir():
    print("Introduce los siguientes valores para realizar la predicción:")

    try:
        # Solicitar datos al usuario con validación de tipo
        int_rate = float(input("Tasa de interés (int_rate): "))
        installment = float(input("Cuota del préstamo (installment): "))
        fico = int(input("Puntaje FICO (fico): "))
        revol_bal = float(input("Balance de crédito Revolving (revol_bal): "))
        revol_util = float(input("Utilización del crédito Revolving (revol_util): "))
        inq_last_6mths = int(input("Consultas de crédito en los últimos 6 meses (inq_last_6mths): "))
        pub_rec = int(input("Registros públicos (pub_rec): "))
        purpose = input("Propósito del préstamo (purpose): ")

        # Comprobar que 'purpose' no esté vacío
        if not purpose:
            raise ValueError("El campo 'purpose' no puede estar vacío.")

        # Crear un DataFrame con los datos ingresados
        data = pd.DataFrame({
            'int.rate': [int_rate],
            'installment': [installment],
            'fico': [fico],
            'revol.bal': [revol_bal],
            'revol.util': [revol_util],
            'inq.last.6mths': [inq_last_6mths],
            'pub.rec': [pub_rec],
            'purpose': [purpose],
            'credit.policy': [1]  # Valor por defecto para 'credit.policy'
        })

        # Hacer la predicción usando el modelo
        prediccion = modelo.predict(data)

        # Mostrar el resultado de la predicción
        if prediccion == 0:
            print("La predicción es: El préstamo NO será pagado.")
        else:
            print("La predicción es: El préstamo SERÁ pagado.")

    except ValueError as e:
        print(f"Error de valor: {e}. Por favor, ingresa datos válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para predecir
if __name__ == "__main__":
    predecir()

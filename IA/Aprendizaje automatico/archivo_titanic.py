import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,  StandardScaler, FunctionTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn import set_config
from sklearn.compose import ColumnTransformer
import joblib

def column_family(X):
    return X[:, [0]] + X[:, [1]]

def family_name(function_transformer, feature_names_in):
    return ["family"]  # feature names out

def family_pipeline():
    return make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        FunctionTransformer(column_family, feature_names_out=family_name))

def encode_sex(X):
    X[:, 0] = np.where(X[:, 0] == 'male', 0, 1)  # Reemplaza 'male' por 0 y 'female' por 1
    return X

def categorize_age(X):
    bins = [-1, 16, 32, 48, 64, 100]
    labels = [1, 2, 3, 4, 5]
    # Aplicar pd.cut directamente sobre la columna de edad
    categorized_age = pd.cut(X[:, 0], bins=bins, labels=labels).astype(int)
    
    return categorized_age.reshape(-1, 1)

final_model_reloaded = joblib.load("Titanic_model.pkl")
new_data = pd.read_csv("titanic.csv")  # Escribe la ruta del archivo 
predictions = final_model_reloaded.predict(new_data)
print(predictions)
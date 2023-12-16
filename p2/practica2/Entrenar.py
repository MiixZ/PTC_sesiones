import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV


def main():
    # Cargar los datos
    colnames = ['perímetro', 'profundidad', 'anchura', 'clase']
    data = pd.read_csv('piernasDataset.csv', names=colnames, header=None)

    # Dividir los datos en características y etiquetas
    X = data.drop('clase', axis=1)
    y = data['clase']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=25)

    # Definir los parámetros para la búsqueda en cuadrícula
    param_grid = {'C': [0.1, 1, 10, 100, 1000],
                  'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
                  'kernel': ['rbf', 'linear', 'poly']}

    # Diccionario para almacenar la precisión de cada kernel
    precision_scores = {}

    # Entrenar el clasificador SVM para cada kernel
    for kernel in ['rbf', 'linear', 'poly']:
        clf = SVC(kernel=kernel)
        clf.fit(X_train, y_train)

        # Evaluar el clasificador en el conjunto de prueba
        y_pred = clf.predict(X_test)

        # Generar la matriz de confusión y calcular las métricas de rendimiento
        print(f"Kernel: {kernel}")
        print("Matriz de confusión:")
        print(confusion_matrix(y_test, y_pred))

        report = classification_report(y_test, y_pred, zero_division=1, output_dict=True)
        print("Reporte de clasificación:")
        print(report)

        # Almacenar la precisión del kernel
        precision_scores[kernel] = report['macro avg']['precision']

    # Elegir el kernel con la mayor precisión
    best_kernel = max(precision_scores, key=precision_scores.get)
    print(f"El kernel con la mayor precisión es: {best_kernel} con una precisión de {precision_scores[best_kernel]}")

    # Ajustar el modelo a los datos con el mejor kernel
    grid = GridSearchCV(SVC(kernel=best_kernel), param_grid, refit=True, verbose=3)
    grid.fit(X_train, y_train)

    best_SVC = grid.best_estimator_
    print(f"El mejor clasificador es: {best_SVC}")

    # Guardamos el clasificador
    with open('clasificador.pkl', 'wb') as f:
        pickle.dump(best_SVC, f)

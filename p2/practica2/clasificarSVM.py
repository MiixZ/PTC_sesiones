import pickle
from warnings import simplefilter
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV


def main():
    # Cargar los datos
    colnames = ['perímetro', 'profundidad', 'anchura', 'clase']
    data = pd.read_csv('piernasDataset.csv', names=colnames)

    # Ignoramos los warnings
    simplefilter(action='ignore', category=FutureWarning)
    simplefilter(action='ignore', category=DeprecationWarning)

    # Dividir los datos en características y etiquetas
    X = data.drop('clase', axis=1)
    y = data['clase']
    # Entrenar el clasificador SVM para cada kernel
    for kernel in ['rbf', 'linear', 'poly']:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=25)

        if kernel == 'poly':
            clf = SVC(kernel=kernel, degree=3)
            svc1 = SVC(kernel=kernel, degree=3)
        else:
            clf = SVC(kernel=kernel)
            svc1 = SVC(kernel=kernel)

        clf.fit(X_train, y_train)

        # Evaluar el clasificador en el conjunto de prueba
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Generar la matriz de confusión y calcular las métricas de rendimiento
        print(f"Kernel: {kernel}")
        print("Matriz de confusión:", confusion_matrix(y_test, y_pred))
        print("Accuracy:", accuracy)

        print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
        print("f1-score es la media entre precisión y recall")
        print(classification_report(y_test, y_pred, zero_division=1))

        # Cross validation
        print("Cross validation:")
        scores = cross_val_score(svc1, X, y, cv=5)
        print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=25)

    # Definir los parámetros para la búsqueda en cuadrícula
    param_grid = {
                    'C': [1, 10, 100, 1000],
                    'gamma': [0.001, 0.005, 0.01, 0.1, 1, 10, 100, 500, 1000]
                 }

    # Elegimos el kernel rbf
    best_kernel = 'rbf'
    # Ajustar el modelo a los datos con el mejor kernel
    grid = GridSearchCV(SVC(kernel=best_kernel), param_grid)
    grid.fit(X_train, y_train)

    best_SVC = grid.best_estimator_
    print(f"El mejor estimador es: {best_SVC}")

    y_pred = best_SVC.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Matriz de confusión:", confusion_matrix(y_test, y_pred))
    print("Accuracy:", accuracy)

    print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
    print("f1-score es la media entre precisión y recall")
    print(classification_report(y_test, y_pred, zero_division=1))

    # Cross validation
    print("Cross validation:")
    svc2 = SVC(kernel=best_kernel, C=best_SVC.C, gamma=best_SVC.gamma, class_weight="balanced")
    scores = cross_val_score(svc2, X, y, cv=5)

    print("Scores 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))

    # Guardamos el clasificador
    with open('clasificador.pkl', 'wb') as f:
        pickle.dump(best_SVC, f)

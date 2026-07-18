import numpy as np
from sklearn.neighbors import NearestNeighbors
import sklearn.metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

def get_knn(df, n, k, metric):
    """
    Devuelve los k vecinos más cercanos para el cliente n.

    Parámetros
    ----------
    df : DataFrame
        Datos (escalados o no).
    n : int
        Índice del cliente.
    k : int
        Número de vecinos.
    metric : str
        Métrica de distancia ('euclidean' o 'manhattan').
    """

    nbrs = NearestNeighbors(
        n_neighbors=k,
        metric=metric
    )

    nbrs.fit(df)

    distances, indices = nbrs.kneighbors([df.iloc[n]])

    result = df.iloc[indices[0]].copy()
    result['distance'] = distances[0]

    return result
#==================================
def evaluate_knn(X_train, X_test, y_train, y_test):
    """
    Función que recibe los datos de entrenamiento y prueba,
     devuelve una lista con los f1_score desdde k=1 hasta k=10.
    """

    scores = []

    for k in range(1, 11):

        model = KNeighborsClassifier(
            n_neighbors=k
        )

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        scores.append(f1_score(y_test, pred))

    return scores
#====================================
def eval_classifier(y_true, y_pred):
    
    f1_score = sklearn.metrics.f1_score(y_true, y_pred)
    print(f'F1: {f1_score:.2f}')
    
# si tienes algún problema con la siguiente línea, reinicia el kernel y ejecuta el cuaderno de nuevo
    cm = sklearn.metrics.confusion_matrix(y_true, y_pred, normalize='all')
    print('Matriz de confusión')
    print(cm)
#====================================
def rnd_model_predict(P, size, seed=42):
    """ Genera predicciones aleatorias para un
     clasificador binario con probabilidad P de
     predecir 1. 
     """

    rng = np.random.default_rng(seed=seed)
    return rng.binomial(n=1, p=P, size=size)
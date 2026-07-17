from sklearn.neighbors import NearestNeighbors

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
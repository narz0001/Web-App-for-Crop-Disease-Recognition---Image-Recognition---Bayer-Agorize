from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def train_knn_model(X, y, n_neighbors=7, p=1, weights='uniform'):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, p=p, weights=weights)
    knn.fit(X, y)
    return knn

def evaluate_knn_model(knn, X_test, y_test):
    y_pred = knn.predict(X_test)
    report = accuracy_score(y_test, y_pred)
    return report
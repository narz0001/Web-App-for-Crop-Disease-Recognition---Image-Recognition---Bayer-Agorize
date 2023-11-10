from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import NuSVC
from sklearn.ensemble import RandomForestClassifier

def train_knn_model(X_train, y_train, n_neighbors=7, p=1, weights='uniform'):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, p=p, weights=weights)
    knn.fit(X_train, y_train)
    return knn

def train_svc_model(X_train, y_train, kernel='rbf', nu=0.1):
    svc = NuSVC(kernel=kernel, nu=nu)
    svc.fit(X_train, y_train)
    return svc

def train_rf_model(X_train, y_train, criterion='entropy', max_depth=10, min_samples_split=5, min_samples_leaf=2, n_estimators=100):
    rf_model = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
    rf_model.fit(X_train, y_train)
    return rf_model

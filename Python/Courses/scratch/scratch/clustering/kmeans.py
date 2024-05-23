import numpy as np

class KMeans:
    def __init__(self, n_clusters, max_iter=100, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centroids = None

    def initialize_centroids(self, X):
        if self.random_state:
            np.random.seed(self.random_state)
        self.centroids = X[np.random.choice(len(X), self.n_clusters, replace=False)]

    def compute_distances(self, X):
        distances = np.zeros((len(X), self.n_clusters))
        for i, point in enumerate(X):
            for j, centroid in enumerate(self.centroids):
                distances[i, j] = np.linalg.norm(point - centroid)
        return distances

    def assign_clusters(self, distances):
        return np.argmin(distances, axis=1)

    def update_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            centroids[k] = np.mean(X[labels == k], axis=0)
        return centroids

    def fit(self, X):
        self.initialize_centroids(X)
        for _ in range(self.max_iter):
            distances = self.compute_distances(X)
            labels = self.assign_clusters(distances)
            new_centroids = self.update_centroids(X, labels)
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids
        return self

    def predict(self, X):
        distances = self.compute_distances(X)
        return self.assign_clusters(distances)
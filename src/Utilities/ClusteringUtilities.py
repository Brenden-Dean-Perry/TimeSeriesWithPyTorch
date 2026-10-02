from sklearn.neighbors import NearestNeighbors
import numpy as np

def hopkins(X, frac=0.1, random_state=None):
    """
    Hopkins statistic measures the degree to which clusters exist in our data.

    A Hopkins statistic close to 1 indicates high clustering tendency, while
    values around 0.5 suggest randomness or uniform distribution. Values between
    0.7 and 0.99 indicate the dataset has a high tendency to form meaningful clusters.
    :param X:
    :param frac:
    :param random_state:
    :return:
    """
    rng = np.random.default_rng(random_state)
    n, d = X.shape
    m = int(frac * n)
    nbrs = NearestNeighbors(n_neighbors=2).fit(X)

    real_idx = rng.choice(n, m, replace=False)
    real = X[real_idx]

    mins, maxs = X.min(axis=0), X.max(axis=0)
    uniform = rng.uniform(mins, maxs, size=(m, d))

    u_dist = nbrs.kneighbors(uniform, return_distance=True)[0][:, 1]
    w_dist = nbrs.kneighbors(real, return_distance=True)[0][:, 1]

    return u_dist.sum() / (u_dist.sum() + w_dist.sum())
import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian mixture centers and covariances
        np.random.seed(42)
        self.centers = np.random.uniform(-3, 3, (10, dim))
        self.covariances = [np.eye(dim) * np.random.uniform(0.5, 2.0) for _ in range(10)]
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-4, 4, (5, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 5)
        # Correlation structure
        self.correlation_matrix = np.random.rand(dim, dim)
        self.correlation_matrix = np.dot(self.correlation_matrix, self.correlation_matrix.T)
        np.fill_diagonal(self.correlation_matrix, 1.0)
        
    def f(self, x):
        # Gaussian mixture components
        gm_value = 0.0
        for i in range(10):
            center = self.centers[i]
            cov = self.covariances[i]
            inv_cov = np.linalg.inv(cov)
            diff = x - center
            exponent = -0.5 * np.dot(diff, np.dot(inv_cov, diff))
            gm_value += np.exp(exponent) / np.sqrt((2 * np.pi)**self.dim * np.linalg.det(cov))
        
        # Radial basis functions
        rbf_value = 0.0
        for i in range(5):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x - center
            rbf_value += np.exp(-0.5 * np.sum((diff / width)**2))
        
        # Correlated quadratic term
        correlated_term = np.dot(x, np.dot(self.correlation_matrix, x))
        
        # Add noise and scaling
        noise = np.random.normal(0, 0.1)
        
        return gm_value + 0.5 * rbf_value + 0.3 * correlated_term + noise
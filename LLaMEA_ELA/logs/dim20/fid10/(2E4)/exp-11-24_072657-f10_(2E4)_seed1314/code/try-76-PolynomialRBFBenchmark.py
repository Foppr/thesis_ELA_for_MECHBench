import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and weights for different scales
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (10, dim))
        self.weights = np.random.normal(0, 1, 10)
        self.scale_factors = np.logspace(-1, 1, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion terms with mixed degrees
        poly_terms = np.zeros_like(x_norm)
        for i in range(1, 6):
            poly_terms += (x_norm ** i) * np.sin(i * np.pi * x_norm) * np.cos(i * np.pi * x_norm)
        
        # Radial basis function components with different bandwidths
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum(((x_norm - self.centers[i]) ** 2) * (self.scale_factors ** 2))
            rbf_sum += self.weights[i] * np.exp(-dist / (2 * (0.5 + 0.5 * i)))
        
        # Adaptive conditioning based on dimensionality and input magnitude
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.mean(np.abs(x_norm))
        
        # Multi-scale interaction terms with varying coupling strengths
        coupling_terms = 0.0
        for i in range(self.dim - 1):
            coupling_terms += (x_norm[i] ** 2 + x_norm[i+1] ** 2) * np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i+1])
        
        # Combined landscape with exponential modulation and adaptive scaling
        result = (np.sum(poly_terms) + 0.5 * rbf_sum + 0.3 * coupling_terms) * condition_factor
        
        # Add noise for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise
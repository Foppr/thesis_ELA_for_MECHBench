import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Radial basis function component
        rb_value = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rb_value += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Adaptive noise component that depends on position
        noise = np.sum(np.sin(x) * np.cos(0.5 * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Polynomial conditioning term
        poly_term = np.sum(x**3 + 0.1 * x**4)
        
        # Cross-dimensional interaction
        cross_term = np.sum((x[:-1] ** 2) * (x[1:] ** 2))
        
        # Combine all terms with different scaling factors
        return rb_value + 0.5 * noise + 0.1 * poly_term + 0.05 * cross_term
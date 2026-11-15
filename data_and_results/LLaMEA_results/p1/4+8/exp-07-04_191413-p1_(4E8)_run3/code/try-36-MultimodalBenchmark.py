import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        
    def f(self, x):
        # Radial basis function component with increased complexity
        rb_value = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rb_value += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Enhanced noise component with higher frequency oscillations
        noise = np.sum(np.sin(2.0 * x) * np.cos(0.7 * x) * np.exp(-0.15 * np.sum(x**2)))
        
        # Enhanced polynomial conditioning term
        poly_term = np.sum(x**4 + 0.15 * x**5)
        
        # Cross-dimensional interaction with cubic terms
        cross_term = np.sum((x[:-1] ** 3) * (x[1:] ** 3))
        
        # Additional radial symmetry term
        radial_symmetry = np.sum((x**2) * np.exp(-0.2 * np.sum(x**2)))
        
        # Combine all terms with different scaling factors
        return rb_value + 0.6 * noise + 0.15 * poly_term + 0.1 * cross_term + 0.03 * radial_symmetry
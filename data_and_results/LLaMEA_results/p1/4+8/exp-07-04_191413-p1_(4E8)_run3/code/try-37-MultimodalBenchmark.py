import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        self.symmetry_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.symmetry_weights = np.random.uniform(0.1, 1.5, 5)
        
    def f(self, x):
        # Enhanced radial basis function component
        rb_value = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rb_value += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Additional radial symmetry terms
        symmetry_value = 0.0
        for i in range(5):
            center = self.symmetry_centers[i]
            weight = self.symmetry_weights[i]
            distance = np.sum((x - center) ** 2)
            symmetry_value += weight * np.exp(-distance / (2 * 0.4 ** 2))
        
        # Enhanced oscillatory noise component
        noise = np.sum(np.sin(3 * x) * np.cos(0.7 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Stronger polynomial conditioning term
        poly_term = np.sum(x**4 + 0.2 * x**5 + 0.05 * x**6)
        
        # Enhanced cross-dimensional interaction
        cross_term = np.sum((x[:-1] ** 3) * (x[1:] ** 3)) + 0.5 * np.sum(x**2)
        
        # Additional high-frequency sinusoidal component
        high_freq = np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        # Combine all terms with different scaling factors
        return rb_value + 0.7 * symmetry_value + 0.6 * noise + 0.15 * poly_term + 0.1 * cross_term + 0.3 * high_freq
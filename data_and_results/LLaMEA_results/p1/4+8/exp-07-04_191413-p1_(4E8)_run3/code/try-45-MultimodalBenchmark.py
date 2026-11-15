import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        
    def f(self, x):
        # Enhanced radial basis function component with varying widths
        rb_value = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            # Use adaptive width based on dimensionality
            width = 0.3 + 0.7 * (i / 14.0)
            rb_value += weight * np.exp(-distance / (2 * width ** 2))
        
        # Dynamic noise component with position-dependent amplitude
        noise = np.sum(np.sin(2 * x) * np.cos(0.3 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Enhanced polynomial conditioning term with mixed powers
        poly_term = np.sum(x**4 + 0.2 * x**5 + 0.05 * x**6)
        
        # Increased cross-dimensional interaction with higher-order coupling
        cross_term = np.sum((x[:-2] ** 2) * (x[1:-1] ** 2) * (x[2:] ** 2))
        
        # Additional trigonometric coupling term
        trig_term = np.sum(np.sin(0.5 * x) * np.cos(0.7 * x) * np.sin(0.3 * x))
        
        # Combine all terms with different scaling factors
        return rb_value + 0.6 * noise + 0.15 * poly_term + 0.1 * cross_term + 0.08 * trig_term
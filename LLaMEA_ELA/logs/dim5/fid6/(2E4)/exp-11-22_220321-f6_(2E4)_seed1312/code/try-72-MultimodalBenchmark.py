import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.sigma = 1.0
        self.k = 2.0
        self.gamma = 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with exponential decay
        rb_func = 0.0
        for i in range(self.dim):
            rb_func += np.exp(-self.sigma * (x[i] ** 2))
            
        # Adaptive polynomial corrugation with dimension-dependent exponents
        poly_corrugation = 0.0
        for i in range(self.dim):
            poly_corrugation += (x[i] ** (4 + i % 3)) * np.cos(self.k * x[i])
            
        # Trigonometric twist field with varying frequencies
        twist_field = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                twist_field += np.sin(x[i] + x[j]) * np.cos(self.gamma * x[i] * x[j])
                
        # Cross-dimensional coupling with exponential weighting
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i] ** 2 + x[j] ** 2) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Asymmetric sigmoidal penalty
        penalty = 0.0
        for i in range(self.dim):
            penalty += (1 / (1 + np.exp(-x[i])) - 0.5) ** 3
            
        return 0.5 * rb_func + 0.3 * poly_corrugation + 0.2 * twist_field + 0.1 * cross_coupling + 0.4 * penalty
import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1.0, 1.0, dim)
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.polynomial_degree = np.random.randint(2, 5)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Sinusoidal component
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(self.frequencies[i] * x[i]) * self.coefficients[i]
        
        # Polynomial basin component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** self.polynomial_degree) * (1.0 / self.polynomial_degree)
        
        # Chaotic interaction term using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic_term += np.sin(x[i-1] * x[i]) * 0.3
        
        # Combine all terms with a global scaling factor
        result = 2.0 * sin_term + 0.5 * poly_term + chaotic_term
        
        # Add small noise for additional complexity
        result += np.random.normal(0, 0.01)
        
        return result
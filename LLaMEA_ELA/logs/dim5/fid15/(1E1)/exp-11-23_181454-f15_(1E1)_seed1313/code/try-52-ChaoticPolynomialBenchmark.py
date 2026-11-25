import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for chaotic behavior
        self.coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 4))
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Polynomial base term with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** 2 + x[i] ** 4) * (i + 1) / self.dim
            
        # Sinusoidal chaotic component
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1)
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i] ** 2)
            
        # Add coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x[i] * x[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
                
        # Combine terms with adaptive weights
        total = 0.5 * poly_term + 0.3 * sin_term + 0.2 * coupling_term
        
        # Add noise for increased difficulty
        noise = 0.001 * np.sum(np.random.uniform(-1, 1, self.dim))
        
        return total + noise
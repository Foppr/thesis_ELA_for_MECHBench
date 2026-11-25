import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree
        poly_term = np.sum(x**7)
        
        # Sinusoidal oscillations with different frequencies
        sin_term = np.sum(np.sin(1.3 * x) * np.sin(0.9 * x) * np.sin(0.4 * x))
        
        # Cross-term interactions with quartic scaling
        cross_term = np.sum(x[:-1]**4 * x[1:]**4)
        
        # Combined function with adjusted weights
        return 0.3 * poly_term + 0.6 * sin_term + 0.1 * cross_term
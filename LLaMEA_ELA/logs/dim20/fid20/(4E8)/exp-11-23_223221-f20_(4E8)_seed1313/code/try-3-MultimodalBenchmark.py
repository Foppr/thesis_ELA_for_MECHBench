import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations with multiple local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Additional cross-terms for increased complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.01 * x[i] * x[j] * np.sin(3.0 * (x[i] + x[j]))
        
        return quadratic + sinusoidal + cross_terms
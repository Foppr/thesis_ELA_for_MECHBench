import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal terms to create many local minima
        f2 = np.sum(np.sin(10.0 * x) * np.cos(3.0 * x))
        
        # Polynomial terms with varying degrees for increased complexity
        f3 = 0.01 * np.sum(x**6)
        
        # Additional coupling terms between dimensions to increase interdependence
        f4 = 0.05 * np.sum((x[:-1] - x[1:])**2)
        
        # Combined function with balanced weights
        return f1 + 0.5 * f2 + f3 + f4
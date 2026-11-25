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
        f2 = np.sum(np.sin(15.0 * x) * np.cos(5.0 * x))
        
        # Additional sine coupling between dimensions
        f3 = 0.3 * np.sum(np.sin(7.0 * (x[:-1] - x[1:]))**2)
        
        # Polynomial terms with varying degrees for increased complexity
        f4 = 0.02 * np.sum(x**6)
        
        # Shifted polynomial term to create asymmetric landscape
        f5 = 0.01 * np.sum((x + 0.5)**4)
        
        # Additional coupling terms between dimensions to increase interdependence
        f6 = 0.08 * np.sum((x[:-1] - x[1:])**2)
        
        # Combined function with balanced weights
        return f1 + 0.7 * f2 + 0.5 * f3 + f4 + f5 + f6
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
        
        # Higher-order polynomial terms for increased complexity
        f3 = 0.02 * np.sum(x**8)
        
        # Additional coupling terms between dimensions with varying weights
        f4 = 0.1 * np.sum((x[:-1] - x[1:])**4)
        
        # Cross-term interactions to increase interdependence
        f5 = 0.03 * np.sum(x[:-1] * x[1:])
        
        # Additional trigonometric term with different frequency for diversity
        f6 = 0.3 * np.sum(np.sin(7.0 * x) * np.sin(2.0 * x))
        
        # Combined function with adjusted weights
        return f1 + 0.7 * f2 + f3 + f4 + f5 + 0.4 * f6
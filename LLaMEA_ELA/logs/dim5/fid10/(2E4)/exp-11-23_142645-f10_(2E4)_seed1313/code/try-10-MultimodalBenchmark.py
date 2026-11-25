import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Add multiple sinusoidal perturbations with different frequencies and amplitudes
        f2 = 0.3 * (np.sum(np.sin(2.5 * x)) + 0.4 * np.sum(np.sin(6.0 * x)) + 0.2 * np.sum(np.sin(10.0 * x)))
        
        # Add a quartic term to increase function curvature
        f3 = 0.015 * np.sum(x**4)
        
        # Add a fifth-order polynomial term for additional complexity
        f4 = 0.008 * np.sum(x**5)
        
        # Add interaction terms between variables
        f5 = 0.02 * np.sum(x[:-1] * x[1:])
        
        # Shift global minimum to (1,1,...,1) instead of origin
        shift = np.ones(self.dim)
        return f1 + f2 + f3 + f4 + f5 + 2.0 * np.sum((x - shift)**2)
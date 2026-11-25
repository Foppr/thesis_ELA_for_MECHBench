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
        f2 = 0.2 * (np.sum(np.sin(3.0 * x)) + 0.5 * np.sum(np.sin(7.0 * x)) + 0.3 * np.sum(np.sin(11.0 * x)))
        
        # Add a quartic term to increase function curvature
        f3 = 0.02 * np.sum(x**4)
        
        # Add a fifth-order polynomial term for additional complexity
        f4 = 0.005 * np.sum(x**5)
        
        # Combine terms with different weights to create challenging landscape
        return f1 + f2 + f3 + f4
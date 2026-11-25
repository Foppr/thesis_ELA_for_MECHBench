import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(2.5 * x) * np.exp(-0.03 * x**2) + 
                         0.4 * np.sin(6.0 * x) * np.exp(-0.08 * x**2))
        
        # Combined polynomial terms for additional complexity
        f3 = 0.015 * np.sum(x**4 + 0.6 * x**3 + 0.15 * x**2)
        
        # Add a multi-modal component with exponential decay
        f4 = 0.15 * np.sum(np.exp(-0.3 * (x - 1.5)**2) + np.exp(-0.3 * (x + 1.5)**2))
        
        return f1 + f2 + f3 + f4
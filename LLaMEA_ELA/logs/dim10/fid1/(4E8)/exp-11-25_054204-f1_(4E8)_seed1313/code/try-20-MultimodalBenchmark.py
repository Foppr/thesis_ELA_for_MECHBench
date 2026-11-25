import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Exponential decay modulation with sinusoidal perturbations
        f2 = np.sum(np.exp(-0.5 * x**2) * np.sin(3.0 * x)**2)
        
        # Additional high-frequency oscillation component
        f3 = 0.5 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Saddle-point inducing term with mixed polynomial and trigonometric components
        f4 = 0.1 * np.sum(x**4 * np.cos(2.0 * x))
        
        # Cross-term interaction creating complex valleys
        f5 = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(5.0 * (x[:-1] + x[1:])))
        
        return f1 + f2 + f3 + f4 + f5
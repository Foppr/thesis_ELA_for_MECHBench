import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base function
        f1 = np.sum(x**2)
        
        # Enhanced exponential decay with sinusoidal perturbations
        f2 = np.sum(np.exp(-0.3 * x**2) * np.sin(4.0 * x)**3)
        
        # High-frequency oscillation component with variable amplitude
        f3 = 0.7 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) * np.exp(-0.1 * x**2))
        
        # Stronger saddle-point inducing term with quartic and trigonometric coupling
        f4 = 0.15 * np.sum(x**4 * np.sin(3.0 * x)**2)
        
        # Enhanced cross-term interaction creating more complex valleys and ridges
        f5 = 0.1 * np.sum(x[:-1] * x[1:] * np.sin(8.0 * (x[:-1] + x[1:])) * np.exp(-0.2 * (x[:-1]**2 + x[1:]**2)))
        
        # Additional cubic interaction term for increased nonlinearity
        f6 = 0.05 * np.sum((x[:-2] + x[1:-1] + x[2:])**3 * np.cos(5.0 * x[1:-1]))
        
        return f1 + f2 + f3 + f4 + f5 + f6
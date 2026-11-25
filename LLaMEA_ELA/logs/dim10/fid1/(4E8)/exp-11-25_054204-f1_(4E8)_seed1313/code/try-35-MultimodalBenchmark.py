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
        
        # High-frequency oscillation component with cubic modulation
        f3 = 0.6 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) * np.abs(x)**1.5)
        
        # Saddle-point inducing term with enhanced polynomial and trigonometric components
        f4 = 0.15 * np.sum(x**5 * np.cos(3.0 * x))
        
        # Cross-term interaction with Gaussian perturbations creating complex valleys
        f5 = 0.08 * np.sum(x[:-1] * x[1:] * np.sin(6.0 * (x[:-1] + x[1:])) * np.exp(-0.5 * (x[:-1]**2 + x[1:]**2)))
        
        # Additional cubic nonlinearity term
        f6 = 0.03 * np.sum(x**3 * np.sin(2.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6
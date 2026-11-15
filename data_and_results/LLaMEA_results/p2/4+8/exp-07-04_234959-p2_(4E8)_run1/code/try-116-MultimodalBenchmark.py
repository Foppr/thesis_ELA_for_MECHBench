import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at the center
        self.global_min = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic component
        f1 = np.sum((x - self.global_min)**2)
        
        # Non-separable high-order polynomial with coupling
        f2 = np.sum((x**3 - 3 * x)**2)
        
        # Trigonometric modulation with varying frequency
        f3 = np.sum(np.sin(2 * np.pi * x) * np.cos(1.5 * np.pi * x))
        
        # Adaptive conditioning based on dimension
        condition = 1 + 0.5 * np.sin(self.dim)
        f4 = np.sum(condition * (x**4 - 2 * x**2 + 1))
        
        # Sharp ridge structure with localized perturbations
        ridge = np.sum(np.exp(-0.5 * (x - 1)**2) + np.exp(-0.5 * (x + 1)**2))
        f5 = ridge
        
        # Combined function with dynamic weights
        return 0.2 * f1 + 0.3 * f2 + 0.15 * f3 + 0.25 * f4 + 0.1 * f5
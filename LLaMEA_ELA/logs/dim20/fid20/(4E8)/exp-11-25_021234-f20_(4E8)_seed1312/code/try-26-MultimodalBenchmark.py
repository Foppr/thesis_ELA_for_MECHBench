import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with exponential decay
        f2 = 0.3 * np.sum(np.sin(8.0 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Additional high-frequency oscillations
        f3 = 0.2 * np.sum(np.sin(15.0 * x) * np.exp(-0.1 * x**2))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        f4 = adaptive_scale * np.sum(np.cos(10.0 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Complex cubic and quartic terms for increased landscape complexity
        f5 = 0.01 * np.sum(x**3 * np.sin(5.0 * x))
        f6 = 0.005 * np.sum(x**4 * np.cos(3.0 * x))
        
        # Add a global deceptive term that creates multiple local minima
        f7 = 0.1 * np.sum(np.exp(-0.5 * (x - 1.0)**2) + np.exp(-0.5 * (x + 1.0)**2) - 1.0)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
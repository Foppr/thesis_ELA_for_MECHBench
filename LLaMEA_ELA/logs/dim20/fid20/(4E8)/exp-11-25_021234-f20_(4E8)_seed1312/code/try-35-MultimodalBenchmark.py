import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal modulations with fractal-like behavior
        f2 = 0.4 * np.sum(np.sin(12.0 * x) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x**2))
        
        # Additional high-frequency oscillations with adaptive decay
        f3 = 0.25 * np.sum(np.sin(20.0 * x) * np.exp(-0.1 * x**2) * np.cos(2.0 * x))
        
        # Adaptive scaling based on dimensionality and local curvature
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.05 * np.std(x)
        f4 = adaptive_scale * np.sum(np.cos(15.0 * x) * np.exp(-0.08 * np.abs(x)) * np.sin(4.0 * x))
        
        # Complex cubic and quartic terms with chaotic perturbations
        f5 = 0.02 * np.sum(x**3 * np.sin(7.0 * x) * np.cos(2.0 * x))
        f6 = 0.01 * np.sum(x**4 * np.cos(5.0 * x) * np.exp(-0.03 * x**2))
        
        # Fractal-like deceptive term with multiple local minima
        f7 = 0.15 * np.sum(np.exp(-0.3 * (x - 1.5)**2) + np.exp(-0.3 * (x + 1.5)**2) - 1.0)
        
        # Saddle point enhancement for increased complexity
        f8 = 0.08 * np.sum(x**2 * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
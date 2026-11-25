import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced exponential decay with varying rates
        f2 = np.sum(np.exp(-0.3 * x**2) - 1.0)
        
        # High-frequency trigonometric perturbations with multiple harmonics
        f3 = 0.7 * np.sum(np.sin(12.0 * x) * np.cos(18.0 * x) + 0.5 * np.sin(20.0 * x))
        
        # Additional quartic and quintic terms for increased curvature
        f4 = 0.015 * np.sum(x**4 + 0.005 * x**5)
        
        # Modified interaction terms between variables
        f5 = 0.008 * np.sum(np.exp(-x**2) * x**3 + 0.003 * np.sin(x) * np.cos(2*x))
        
        # Cross-terms to increase problem conditioning
        f6 = 0.002 * np.sum((x[:-1] - x[1:])**2)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
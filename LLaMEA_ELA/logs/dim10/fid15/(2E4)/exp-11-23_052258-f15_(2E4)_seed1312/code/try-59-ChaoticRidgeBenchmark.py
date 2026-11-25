import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested exponential spirals with adaptive base modulation
        f1 = np.sum(np.exp(2.0 * np.abs(x) * np.sin(3.0 * x) * np.cos(1.5 * x)) * 
                   np.exp(-0.1 * x**2))
        
        # Adaptive trigonometric coupling with dynamic phase shifts and frequency modulation
        f2 = 0.5 * np.sum(np.sin(4.2 * x[:-1] + 3.8 * x[1:] + 0.8 * np.sin(2.0 * x[:-1])) * 
                         np.cos(3.1 * x[:-1] - 4.1 * x[1:] + 0.6 * np.cos(1.7 * x[1:])) * 
                         np.exp(-0.05 * (x[:-1]**2 + x[1:]**2)))
        
        # Fractal-like ridge with self-similar curvature and chaotic perturbations
        f3 = 0.4 * np.sum(((x[:-1] - x[1:]) ** 6 + 0.3 * np.sin(15.0 * (x[:-1] + x[1:])) * 
                          np.exp(-0.2 * (x[:-1]**2 + x[1:]**2))) * 
                         np.cos(2.0 * np.log(np.abs(x[:-1]) + 1e-8)))
        
        # High-frequency chaotic component with logistic-like modulation and complex sine waves
        f4 = 0.3 * np.sum(np.sin(25.0 * np.abs(x) + np.cos(12.0 * x)) * 
                         np.exp(-0.7 * x**2) * np.sin(3.0 * x) * np.cos(0.5 * x))
        
        # Multi-scale polynomial chaos with nested roots and fractal-like perturbations
        f5 = 0.25 * np.sum((x**9 - 4.2 * x**5 + 3.7 * x**3 - 1.8 * x) * 
                          np.cos(x * np.sin(0.7 * x)) * np.exp(-0.3 * x**2))
        
        # Additional chaotic saddle-point terms with varying amplitude and frequency
        f6 = 0.2 * np.sum(np.sin(10.0 * x + np.cos(5.0 * x)) * 
                         np.exp(-0.4 * x**2) * (np.abs(x) + 1.0)**(-1.5))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
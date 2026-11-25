import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic exponential component with fractional Brownian motion
        f1 = np.sum(np.exp(0.9 * x**2 * np.sin(x) * np.cos(0.6 * x)) * 
                   np.exp(-0.1 * np.sum(np.abs(np.diff(x, prepend=x[0]))**1.8)))
        
        # Quaternion-valued trigonometric coupling with adaptive weights
        f2 = 0.45 * np.sum(np.sin(3.2 * x[:-1] + 2.8 * x[1:] + 0.6 * np.sin(x[:-1] * x[1:])) +
                          np.cos(2.2 * x[:-1] - 3.8 * x[1:] + 0.4 * np.cos(x[:-1] * x[1:])))
        
        # Adaptive ridge with variable curvature and fractional polynomial terms
        f3 = 0.41 * np.sum((x[:-1] - x[1:]) ** 3.7 + 0.25 * np.sin(12.5 * (x[:-1] + x[1:])) *
                          np.exp(-0.06 * np.abs(x[:-1] - x[1:])))
        
        # Hyper-chaotic component with perturbed sine waves and fractional derivatives
        f4 = 0.34 * np.sum(np.sin(17.5 * np.abs(x) + np.cos(9.5 * x)) * 
                          np.exp(-0.32 * x**2) * np.sin(0.6 * np.sum(x**3)))
        
        # High-dimensional polynomial with hyper-chaotic perturbations
        f5 = 0.27 * np.sum((x**6.8 - 3.9 * x**4.1 + 3.2 * x**1.9) * 
                          np.cos(1.6 * x) * np.exp(-0.22 * np.sum(x**2)))
        
        # Fractional interaction term for increased dimensional complexity
        f6 = 0.21 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.4 * 
                          np.sin(2.3 * np.sum(x[:-1] + x[1:])))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
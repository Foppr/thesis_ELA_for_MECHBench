import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic exponential component with fractional Brownian motion
        f1 = np.sum(np.exp(0.8 * x**2 * np.sin(x) * np.cos(0.5 * x)) * 
                   np.exp(-0.1 * np.sum(np.abs(np.diff(x, prepend=x[0]))**1.7)))
        
        # Quaternion-valued trigonometric coupling with adaptive weights
        f2 = 0.42 * np.sum(np.sin(3.1 * x[:-1] + 2.9 * x[1:] + 0.5 * np.sin(x[:-1] * x[1:])) +
                          np.cos(2.3 * x[:-1] - 3.7 * x[1:] + 0.3 * np.cos(x[:-1] * x[1:])))
        
        # Adaptive ridge with variable curvature and fractional polynomial terms
        f3 = 0.38 * np.sum((x[:-1] - x[1:]) ** 3.5 + 0.22 * np.sin(13.0 * (x[:-1] + x[1:])) *
                          np.exp(-0.05 * np.abs(x[:-1] - x[1:])))
        
        # Hyper-chaotic component with perturbed sine waves and fractional derivatives
        f4 = 0.31 * np.sum(np.sin(18.0 * np.abs(x) + np.cos(9.0 * x)) * 
                          np.exp(-0.3 * x**2) * np.sin(0.7 * np.sum(x**3)))
        
        # High-dimensional polynomial with hyper-chaotic perturbations
        f5 = 0.24 * np.sum((x**7 - 3.8 * x**4 + 3.1 * x**2) * 
                          np.cos(1.5 * x) * np.exp(-0.2 * np.sum(x**2)))
        
        # Fractional interaction term for increased dimensional complexity
        f6 = 0.19 * np.sum(np.abs(x[:-1] - x[1:]) ** 1.3 * 
                          np.sin(2.1 * np.sum(x[:-1] + x[1:])))
        
        # Additional chaotic component with dynamic phase coupling and hyper-chaotic modulation
        f7 = 0.28 * np.sum(np.sin(5.0 * x**3 + 2.0 * np.cos(4.0 * x)) * 
                          np.exp(-0.15 * np.abs(x)**1.8) * 
                          np.cos(0.9 * np.sum(np.sin(2.5 * x))))
        
        # Multi-scale fractal-like perturbation with variable dimensionality
        f8 = 0.35 * np.sum((np.sin(7.0 * x + np.cos(3.0 * x)))**2.3 * 
                          np.exp(-0.2 * np.sum(x**4)) * 
                          np.sin(1.2 * np.sum(np.abs(x)**0.7)))
        
        # Hybrid trigonometric-polynomial component for enhanced complexity
        f9 = 0.21 * np.sum((np.cos(2.0 * x) + np.sin(1.5 * x))**3.2 * 
                          (x**2 + 0.5 * np.sin(3.0 * x)) * 
                          np.exp(-0.1 * np.sum(x**2)))
        
        # Dynamic dimensional coupling with variable scaling factors
        f10 = 0.17 * np.sum(np.sin(4.0 * x) * np.cos(2.5 * x) * 
                           np.exp(-0.08 * np.sum(np.abs(x)**1.9)) * 
                           np.sin(0.6 * np.sum(x**3)))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
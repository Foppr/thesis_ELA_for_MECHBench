import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Highly multimodal exponential coupling with nested chaotic modulation
        f1 = np.sum(np.exp(2.0 * x**2 * np.sin(3.0 * x) * np.cos(0.7 * x)) * 
                   np.sin(5.0 * x + np.cos(2.0 * x)))
        
        # Multi-scale phase-coupled trigonometric interactions with dynamic weights
        f2 = 0.6 * np.sum(np.sin(4.2 * x[:-1] + 3.8 * x[1:] + 0.8 * np.sin(x[:-1])) * 
                         np.cos(3.1 * x[:-1] - 4.5 * x[1:] + 0.6 * np.cos(x[1:])) * 
                         np.exp(-0.3 * (x[:-1]**2 + x[1:]**2)))
        
        # Fractal-like ridge with variable curvature and chaotic perturbations
        f3 = 0.5 * np.sum((x[:-1] - x[1:]) ** 6 + 0.3 * np.sin(17.0 * (x[:-1] + x[1:])) * 
                         np.exp(-0.2 * (x[:-1]**2 + x[1:]**2)) * 
                         np.cos(2.0 * x[:-1]) * np.sin(1.5 * x[1:]))
        
        # Ultra-high frequency chaotic component with logistic-like behavior
        f4 = 0.4 * np.sum(np.sin(25.0 * np.abs(x) + np.cos(12.0 * x)) * 
                         np.exp(-0.8 * x**2) * np.sin(3.0 * x) * 
                         np.cos(0.5 * x**2))
        
        # High-order polynomial with nested chaotic modulation for extreme multimodality
        f5 = 0.3 * np.sum((x**9 - 4.2 * x**5 + 4.1 * x**3 - 1.8 * x) * 
                         np.cos(x * np.sin(0.7 * x)) * np.exp(-0.3 * x**2) * 
                         np.sin(2.0 * x))
        
        # Additional nested chaotic perturbations for increased complexity
        f6 = 0.25 * np.sum(np.sin(10.0 * x + np.cos(8.0 * x)) * 
                          np.exp(-0.4 * x**2) * 
                          np.sin(3.5 * x) * 
                          np.cos(1.2 * x**3))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
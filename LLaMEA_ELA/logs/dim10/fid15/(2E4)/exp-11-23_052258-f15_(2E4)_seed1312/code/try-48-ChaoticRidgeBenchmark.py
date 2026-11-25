import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with dynamic base and chaotic modulation
        f1 = np.sum(np.exp(0.7 * x**2 * np.sin(x) * np.cos(0.3 * x)))
        
        # Multi-scale trigonometric coupling for complex interactions with phase shifts
        f2 = 0.45 * np.sum(np.sin(3.1 * x[:-1] + 2.9 * x[1:] + 0.5 * np.sin(x[:-1])) + 
                          np.cos(2.3 * x[:-1] - 3.1 * x[1:] + 0.7 * np.cos(x[1:])))
        
        # Asymmetric ridge with variable curvature, noise, and chaotic perturbations
        f3 = 0.42 * np.sum((x[:-1] - x[1:]) ** 4 + 0.25 * np.sin(13.0 * (x[:-1] + x[1:])) * 
                          np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Chaotic component with logistic map and perturbed sine waves, higher frequency
        f4 = 0.35 * np.sum(np.sin(18.0 * np.abs(x) + np.cos(9.0 * x)) * 
                          np.exp(-0.6 * x**2) * np.sin(2.5 * x))
        
        # Additional high-frequency polynomial terms with chaotic modulation for increased multimodality
        f5 = 0.25 * np.sum((x**7 - 3.8 * x**4 + 3.1 * x**2) * 
                          np.cos(x * np.sin(0.5 * x)) * np.exp(-0.2 * x**2))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5
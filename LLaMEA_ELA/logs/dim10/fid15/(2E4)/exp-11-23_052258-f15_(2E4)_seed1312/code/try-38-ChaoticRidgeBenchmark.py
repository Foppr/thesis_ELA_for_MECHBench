import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with dynamic base and chaotic modulation
        f1 = np.sum(np.exp(0.5 * x**2 * np.sin(x) * np.cos(0.3 * x)))
        
        # Multi-scale trigonometric coupling with phase shifts and chaotic interference
        f2 = 0.4 * np.sum(np.sin(3.0 * x[:-1] + 4.0 * x[1:] + np.sin(1.5 * x[:-1])) + 
                          np.cos(2.0 * x[:-1] - 3.0 * x[1:] + np.cos(1.2 * x[1:])))
        
        # Asymmetric ridge with variable curvature, noise, and fractal-like perturbations
        f3 = 0.4 * np.sum((x[:-1] - x[1:]) ** 5 + 0.2 * np.sin(15.0 * (x[:-1] + x[1:])) * 
                          np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Chaotic component with logistic map, perturbed sine waves, and multi-modal interactions
        f4 = 0.3 * np.sum(np.sin(20.0 * np.abs(x) + np.cos(10.0 * x)) * 
                          np.exp(-0.7 * x**2) * np.sin(5.0 * x))
        
        # Additional high-frequency polynomial terms with chaotic coefficients for increased multimodality
        f5 = 0.2 * np.sum((x**8 - 4.0 * x**5 + 3.0 * x**3) * np.cos(x) * np.sin(0.5 * x))
        
        # Cross-dimensional coupling with chaotic interaction weights
        f6 = 0.15 * np.sum(np.sin(x[:-1] * x[1:] * np.exp(-0.2 * x[:-1]**2)) * 
                           np.cos(x[:-1] + x[1:]) * np.sin(3.0 * (x[:-1] - x[1:])))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
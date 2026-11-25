import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with dynamic base
        f1 = np.sum(np.exp(0.4 * x**2 * np.sin(x)))
        
        # Multi-scale trigonometric coupling for complex interactions
        f2 = 0.3 * np.sum(np.sin(2.5 * x[:-1] + 3.5 * x[1:]) + np.cos(1.8 * x[:-1] - 2.8 * x[1:]))
        
        # Asymmetric ridge with variable curvature and noise
        f3 = 0.3 * np.sum((x[:-1] - x[1:]) ** 4 + 0.15 * np.sin(12.0 * (x[:-1] + x[1:])))
        
        # Chaotic component with logistic map and perturbed sine waves
        f4 = 0.25 * np.sum(np.sin(16.0 * np.abs(x) + np.cos(8.0 * x)) * np.exp(-0.6 * x**2))
        
        # Additional high-frequency polynomial terms for increased multimodality
        f5 = 0.15 * np.sum((x**7 - 3.5 * x**4 + 2.5 * x**2) * np.cos(x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5
import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with dynamic base and chaotic modulation
        f1 = np.sum(np.exp(0.5 * x**2 * np.sin(x) * np.cos(0.3 * x)))
        
        # Multi-scale trigonometric coupling with asymmetric interaction weights
        f2 = 0.4 * np.sum(np.sin(3.0 * x[:-1] + 2.0 * x[1:]) * np.cos(1.5 * x[:-1] - 2.5 * x[1:]))
        
        # Asymmetric ridge with variable curvature, noise, and chaotic perturbations
        f3 = 0.35 * np.sum((x[:-1] - x[1:]) ** 4 + 0.2 * np.sin(15.0 * (x[:-1] + x[1:])) * np.exp(-0.5 * x[:-1]**2))
        
        # Chaotic component with logistic map and perturbed sine waves with varying frequencies
        f4 = 0.3 * np.sum(np.sin(20.0 * np.abs(x) + np.cos(10.0 * x)) * np.exp(-0.7 * x**2) * np.sin(0.5 * x))
        
        # Additional high-frequency polynomial terms with chaotic modulation for increased multimodality
        f5 = 0.2 * np.sum((x**8 - 4.0 * x**5 + 3.0 * x**3) * np.cos(2.0 * x) * np.sin(0.2 * x))
        
        # Combine all terms with different weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5
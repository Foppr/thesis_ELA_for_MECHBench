import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential growth with dynamic base and chaotic modulation
        f1 = np.sum(np.exp(0.8 * x**2 * np.sin(x) * np.cos(0.4 * x)))
        
        # Multi-scale trigonometric coupling for complex interactions with phase shifts
        f2 = 0.5 * np.sum(np.sin(3.5 * x[:-1] + 2.7 * x[1:] + 0.6 * np.sin(x[:-1])) + 
                          np.cos(2.5 * x[:-1] - 3.3 * x[1:] + 0.8 * np.cos(x[1:])))
        
        # Asymmetric ridge with variable curvature, noise, and chaotic perturbations
        f3 = 0.45 * np.sum((x[:-1] - x[1:]) ** 4 + 0.3 * np.sin(14.0 * (x[:-1] + x[1:])) * 
                          np.exp(-0.12 * (x[:-1]**2 + x[1:]**2)))
        
        # Chaotic component with logistic map and perturbed sine waves, higher frequency
        f4 = 0.38 * np.sum(np.sin(19.0 * np.abs(x) + np.cos(9.5 * x)) * 
                          np.exp(-0.65 * x**2) * np.sin(2.7 * x))
        
        # Additional high-frequency polynomial terms with chaotic modulation for increased multimodality
        f5 = 0.28 * np.sum((x**7 - 4.0 * x**4 + 3.3 * x**2) * 
                          np.cos(x * np.sin(0.6 * x)) * np.exp(-0.22 * x**2))
        
        # Introduce a new chaotic perturbation term to increase landscape complexity
        f6 = 0.15 * np.sum(np.sin(25.0 * x + np.cos(12.0 * x)) * 
                          np.exp(-0.3 * x**2) * np.sin(3.0 * x))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
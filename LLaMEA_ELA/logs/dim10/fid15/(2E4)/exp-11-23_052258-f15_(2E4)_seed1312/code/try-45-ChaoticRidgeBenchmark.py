import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential coupling with dynamic base and phase modulation
        f1 = np.sum(np.exp(0.5 * x**2 * np.sin(x) * np.cos(0.3 * x)))
        
        # Multi-scale trigonometric coupling with varying interaction weights
        f2 = 0.4 * np.sum(np.sin(3.0 * x[:-1] + 2.0 * x[1:]) + np.cos(2.0 * x[:-1] - 1.5 * x[1:]))
        
        # Asymmetric ridge with variable curvature and noise
        f3 = 0.35 * np.sum((x[:-1] - x[1:]) ** 4 + 0.2 * np.sin(10.0 * (x[:-1] + x[1:])))
        
        # Chaotic component with logistic map and perturbed sine waves
        f4 = 0.3 * np.sum(np.sin(15.0 * np.abs(x) + np.cos(7.0 * x)) * np.exp(-0.5 * x**2))
        
        # Additional high-frequency polynomial terms for increased multimodality with irregular peaks
        f5 = 0.2 * np.sum((x**8 - 4.0 * x**5 + 3.0 * x**3) * np.cos(1.5 * x))
        
        # Cross-term interactions to increase non-separability and algorithmic difficulty
        f6 = 0.15 * np.sum(np.sin(x[:-1] * x[1:]) * np.exp(-0.2 * (x[:-1]**2 + x[1:]**2)))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
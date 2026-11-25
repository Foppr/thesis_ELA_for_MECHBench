import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential coupling with dynamic base and phase modulation
        f1 = np.sum(np.exp(0.6 * x**2 * np.sin(x) * np.cos(0.4 * x)))
        
        # Multi-scale trigonometric coupling with varying interaction weights
        f2 = 0.35 * np.sum(np.sin(3.5 * x[:-1] + 1.8 * x[1:]) + np.cos(1.8 * x[:-1] - 1.7 * x[1:]))
        
        # Asymmetric ridge with variable curvature and noise
        f3 = 0.4 * np.sum((x[:-1] - x[1:]) ** 4 + 0.25 * np.sin(9.0 * (x[:-1] + x[1:])))
        
        # Chaotic component with logistic map and perturbed sine waves
        f4 = 0.35 * np.sum(np.sin(16.0 * np.abs(x) + np.cos(6.5 * x)) * np.exp(-0.4 * x**2))
        
        # Additional high-frequency polynomial terms for increased multimodality with irregular peaks
        f5 = 0.25 * np.sum((x**9 - 3.8 * x**5 + 2.8 * x**3) * np.cos(1.6 * x))
        
        # Cross-term interactions to increase non-separability and algorithmic difficulty
        f6 = 0.2 * np.sum(np.sin(x[:-1] * x[1:]) * np.exp(-0.15 * (x[:-1]**2 + x[1:]**2)))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6
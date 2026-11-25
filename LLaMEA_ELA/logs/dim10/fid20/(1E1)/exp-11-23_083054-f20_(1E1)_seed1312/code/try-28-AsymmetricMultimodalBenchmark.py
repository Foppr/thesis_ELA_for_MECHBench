import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with asymmetric weights
        f1 = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric components with varying frequencies and phases
        f2 = np.sum(np.sin(2 * np.pi * x_norm) ** 2 + 
                   0.7 * np.cos(3 * np.pi * x_norm) ** 2 + 
                   0.4 * np.sin(5 * np.pi * x_norm) ** 2)
        
        # Exponential interaction terms creating steep gradients
        f3 = np.sum(np.exp(0.5 * x_norm**2) - 1.0 + 
                   0.3 * np.exp(0.8 * x_norm**2) - 0.3)
        
        # Cross-terms with asymmetric scaling to create complex valleys
        f4 = np.sum((x_norm[:-1] - x_norm[1:]) ** 2 * (1 + 0.5 * np.abs(x_norm[:-1])))
        
        # Asymmetric sinusoidal component
        f5 = np.sum(0.6 * np.sin(4 * np.pi * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combine all terms with different weights
        return 0.4 * f1 + 0.3 * f2 + 0.15 * f3 + 0.1 * f4 + 0.05 * f5
import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Asymmetric polynomial terms with different exponents
        f1 = np.sum(np.abs(x_norm)**3 + 0.5 * np.abs(x_norm)**5)
        
        # Trigonometric components with varying frequencies and phases
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                   0.7 * np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential interaction terms creating steep gradients
        f3 = np.sum(np.exp(2 * np.abs(x_norm)) - 1 + 0.3 * np.exp(4 * np.abs(x_norm)) - 1)
        
        # Cross-terms with asymmetric weights to create non-uniform landscape
        f4 = np.sum((x_norm[:-1] ** 2) * (x_norm[1:] ** 3) + 0.5 * (x_norm[1:] ** 2) * (x_norm[:-1] ** 4))
        
        # High-frequency oscillatory component for fine structure
        f5 = np.sum(np.sin(20 * np.pi * x_norm) ** 2 + 0.2 * np.sin(30 * np.pi * x_norm) ** 2)
        
        # Combine with asymmetric weights to emphasize different characteristics
        return 0.4 * f1 + 0.3 * f2 + 0.15 * f3 + 0.1 * f4 + 0.05 * f5
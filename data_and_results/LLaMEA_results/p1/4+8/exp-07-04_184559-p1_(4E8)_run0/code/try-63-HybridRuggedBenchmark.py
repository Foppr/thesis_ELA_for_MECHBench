import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic component with adaptive conditioning
        f1 = np.sum((1 + 0.1 * np.abs(x_norm)) * x_norm**2)
        
        # Non-separable sine-cosine interaction term with enhanced coupling
        f2 = np.sum(np.sin(2 * x_norm) * np.cos(2 * x_norm))
        
        # Cross-term interaction creating strong non-separability
        f3 = np.sum(np.sin(3 * (x_norm[:-1] + x_norm[1:])) * np.cos(3 * (x_norm[:-1] - x_norm[1:])))
        
        # Global ruggedness term with higher frequency modulation
        f4 = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(-0.3 * np.sum(x_norm**2)))
        
        # Additional chaotic modulation for increased complexity
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(-x_norm**2)) * np.cos(np.pi * x_norm * np.exp(-x_norm**2)))
        
        # Combine all components with optimized weights
        return 0.3 * f1 + 1.2 * f2 + 1.0 * f3 + 1.8 * f4 + 0.7 * f5
import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic component with enhanced adaptive conditioning
        f1 = np.sum((1 + 0.2 * np.abs(x_norm) + 0.05 * x_norm**4) * x_norm**2)
        
        # Non-separable sine-cosine interaction term with enhanced chaotic modulation
        f2 = np.sum(np.sin(x_norm) * np.cos(x_norm) * np.exp(-0.15 * np.sum(x_norm**2)))
        
        # Cross-term interaction creating non-separability with variable coupling and higher frequency
        f3 = np.sum(np.sin(3 * (x_norm[:-1] + x_norm[1:])) * np.cos(0.7 * (x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.3 * np.sin(4 * np.pi * x_norm[:-1]) + 0.1 * x_norm[:-1]**3))
        
        # Global ruggedness term with multiple local minima and enhanced chaotic perturbations
        f4 = np.sum(np.sin(4 * np.pi * x_norm) * np.exp(-0.4 * np.sum(x_norm**2)) * 
                   (1 + 0.2 * np.sin(8 * np.pi * x_norm) + 0.1 * np.cos(6 * np.pi * x_norm)))
        
        # Additional chaotic component with polynomial modulation for enhanced complexity
        f5 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                   np.exp(-0.25 * np.sum(x_norm**2)) * 
                   (1 + 0.1 * np.sin(6 * np.pi * np.sum(x_norm**2)) + 0.05 * x_norm**3))
        
        # Add higher-order polynomial interaction term for increased complexity
        f6 = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                   np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with optimized weights
        return 0.4 * f1 + 1.5 * f2 + 0.7 * f3 + 2.0 * f4 + 1.0 * f5 + 0.5 * f6
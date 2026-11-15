import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic component with adaptive conditioning
        f1 = np.sum((1 + 0.15 * np.abs(x_norm)) * x_norm**2)
        
        # Non-separable sine-cosine interaction term with chaotic modulation
        f2 = np.sum(np.sin(1.5 * x_norm) * np.cos(1.5 * x_norm) * np.exp(-0.15 * np.sum(x_norm**2)))
        
        # Cross-term interaction creating non-separability with variable coupling
        f3 = np.sum(np.sin(2.5 * (x_norm[:-1] + x_norm[1:])) * np.cos(0.7 * (x_norm[:-1] - x_norm[1:])) * 
                   (1 + 0.25 * np.sin(3.5 * np.pi * x_norm[:-1])))
        
        # Global ruggedness term with multiple local minima and chaotic perturbations
        f4 = np.sum(np.sin(3.5 * np.pi * x_norm) * np.exp(-0.35 * np.sum(x_norm**2)) * 
                   (1 + 0.15 * np.sin(7.5 * np.pi * x_norm)))
        
        # Additional chaotic component for enhanced complexity
        f5 = np.sum(np.sin(4.5 * np.pi * x_norm) * np.cos(2.5 * np.pi * x_norm) * 
                   np.exp(-0.25 * np.sum(x_norm**2)) * 
                   (1 + 0.08 * np.sin(5.5 * np.pi * np.sum(x_norm**2))))
        
        # Combine all components with optimized weights
        return 0.35 * f1 + 1.1 * f2 + 0.65 * f3 + 1.7 * f4 + 0.85 * f5
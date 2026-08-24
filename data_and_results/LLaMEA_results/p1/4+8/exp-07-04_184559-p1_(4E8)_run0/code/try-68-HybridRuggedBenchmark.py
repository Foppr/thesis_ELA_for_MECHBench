import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic component
        f1 = np.sum(x_norm**2)
        
        # Non-separable sine-cosine interaction term with chaotic modulation
        f2 = np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        # Cross-term interaction creating non-separability with chaotic logistic map
        chaotic_factor = 1 + 0.1 * np.sin(10 * np.sum(x_norm**2))
        f3 = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]) * chaotic_factor)
        
        # Global ruggedness term with multiple local minima and chaotic modulation
        logistic_map = 4 * x_norm * (1 - x_norm)
        ruggedness_term = np.sin(5 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2))
        f4 = np.sum(ruggedness_term * logistic_map.flatten()[:len(x_norm)])
        
        # Add a chaotic perturbation term
        chaos_perturbation = np.sum(np.sin(100 * x_norm) * np.cos(50 * x_norm))
        
        # Combine all components with different weights
        return 0.5 * f1 + 1.5 * f2 + 0.8 * f3 + 2.0 * f4 + 0.3 * chaos_perturbation
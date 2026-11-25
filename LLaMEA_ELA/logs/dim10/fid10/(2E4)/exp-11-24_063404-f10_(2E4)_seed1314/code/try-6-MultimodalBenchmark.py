import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Chaotic interaction terms using trigonometric functions with irrational multiples
        f3 = np.sum(np.sin(np.sqrt(2) * np.pi * x_norm) * np.cos(np.pi * x_norm) * 
                   np.sin(np.sqrt(3) * np.pi * x_norm))
        
        # Nested minima structure with exponential scaling
        f4 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(5 * x_norm)**2)
        
        # Cross-term interactions creating complex valleys and ridges
        f5 = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Add a small perturbation term to increase complexity
        f6 = 0.001 * np.sum(np.sin(100 * x_norm) * np.cos(50 * x_norm))
        
        # Combine all terms with different weights to create a complex landscape
        return 2.0 * f1 + 0.5 * f2 + 0.3 * f3 + 0.1 * f4 + 0.05 * f5 + 0.005 * f6 + 1e-8 * np.sum(x_norm**6)
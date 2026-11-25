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
        f2 = np.sum(np.sin(12 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Chaotic interaction terms using trigonometric functions with irrational multiples
        f3 = np.sum(np.sin(np.sqrt(2) * np.pi * x_norm) * np.cos(np.pi * x_norm) * 
                   np.sin(np.sqrt(5) * np.pi * x_norm))
        
        # Nested minima structure with exponential scaling
        f4 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(6 * x_norm)**2)
        
        # Enhanced cross-term interactions creating complex valleys and ridges
        f5 = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]) * 
                   np.sin(0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Add a small perturbation term to increase complexity
        f6 = 0.001 * np.sum(np.sin(150 * x_norm) * np.cos(75 * x_norm))
        
        # Additional chaotic term with fractional powers for more irregularity
        f7 = np.sum(np.sin(np.pi * x_norm) * np.cos(np.sqrt(7) * np.pi * x_norm) * 
                   np.sin(np.sqrt(11) * np.pi * x_norm) * np.abs(x_norm)**0.3)
        
        # Combine all terms with different weights to create a complex landscape
        return 1.5 * f1 + 0.6 * f2 + 0.4 * f3 + 0.15 * f4 + 0.08 * f5 + 0.008 * f6 + 0.005 * f7 + 1e-8 * np.sum(x_norm**6)
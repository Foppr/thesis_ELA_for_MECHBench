import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with dimension-dependent scaling
        f1 = np.sum(x_norm**2 * (1 + 0.1 * np.abs(x_norm)))
        
        # Chaotic oscillation with exponential modulation and phase shifts
        f2 = 0.5 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                         np.exp(-0.5 * np.abs(x_norm)) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        f3 = 0.3 * np.sum(np.exp(-x_norm**2) * np.sin(3 * np.pi * x_norm) * 
                         (1 + 0.2 * np.cos(5 * np.pi * x_norm)))
        
        # Conditional interaction with parity-based activation and memory effect
        f4 = 0.2 * np.sum((x_norm[:-1] * x_norm[1:]) * 
                         (1 + 0.4 * np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:])))
        
        # Fourth-order polynomial with random coefficient modulation
        f5 = 0.1 * np.sum((x_norm**4) * (1 + 0.2 * np.sin(2 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with non-uniform scaling and delay effects
        f6 = 0.15 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) ** 1.7 * 
                          (1 + 0.3 * np.cos(4 * np.pi * x_norm[:-1])))
        
        # Additional high-frequency chaotic component
        f7 = 0.05 * np.sum(np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                         np.exp(-0.3 * x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
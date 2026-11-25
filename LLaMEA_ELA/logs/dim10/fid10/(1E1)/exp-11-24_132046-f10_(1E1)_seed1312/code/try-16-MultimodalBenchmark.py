import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with dimension-dependent scaling
        f1 = np.sum(x_norm**2 * (1 + 0.1 * np.abs(x_norm)))
        
        # Enhanced chaotic oscillation with higher frequency components and phase modulation
        f2 = 0.6 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm) * 
                         np.exp(-0.4 * np.abs(x_norm)) * (1 + 0.4 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying steepness and additional harmonic components
        f3 = 0.4 * np.sum(np.exp(-x_norm**2) * np.sin(4 * np.pi * x_norm) * 
                         (1 + 0.3 * np.cos(6 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.sin(2 * np.pi * x_norm)))
        
        # Conditional interaction with parity-based activation and memory effect
        f4 = 0.25 * np.sum((x_norm[:-1] * x_norm[1:]) * 
                          (1 + 0.5 * np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:])) * 
                          (1 + 0.1 * np.cos(3 * np.pi * x_norm[:-1])))
        
        # Fourth-order polynomial with random coefficient modulation and additional harmonic terms
        f5 = 0.15 * np.sum((x_norm**4) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)) * 
                          (1 + 0.2 * np.cos(2 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with non-uniform scaling and delay effects
        f6 = 0.2 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) ** 1.8 * 
                         (1 + 0.4 * np.cos(5 * np.pi * x_norm[:-1])) * 
                         (1 + 0.1 * np.sin(4 * np.pi * x_norm[1:-1])))
        
        # Additional high-frequency chaotic component with enhanced non-linearity
        f7 = 0.08 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm) * 
                         np.exp(-0.4 * x_norm**2) * (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # New cross-dimensional interaction term with modified coupling strength and phase shift
        f8 = 0.15 * np.sum(np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                          np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                          (1 + 0.2 * np.sin(4 * np.pi * x_norm[:-1])) * 
                          (1 + 0.1 * np.cos(5 * np.pi * x_norm[1:])))
        
        # Add a global scaling factor to increase the overall difficulty
        return 1.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)
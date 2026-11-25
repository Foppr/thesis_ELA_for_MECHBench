import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with dimension-dependent scaling and harmonic modulation
        f1 = np.sum(x_norm**2 * (1 + 0.1 * np.abs(x_norm)) * (1 + 0.2 * np.sin(3 * np.pi * x_norm)))
        
        # Enhanced chaotic oscillation with higher frequency components, phase modulation, and memory effect
        f2 = 0.7 * np.sum(np.sin(11 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * 
                         np.exp(-0.3 * np.abs(x_norm)) * (1 + 0.5 * np.sin(7 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(4 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying steepness, harmonic components, and nonlinear activation
        f3 = 0.45 * np.sum(np.exp(-x_norm**2) * np.sin(5 * np.pi * x_norm) * 
                          (1 + 0.3 * np.cos(7 * np.pi * x_norm)) * 
                          (1 + 0.2 * np.sin(3 * np.pi * x_norm)) * 
                          (1 + 0.1 * np.cos(5 * np.pi * x_norm)))
        
        # Conditional interaction with parity-based activation, memory effect, and cross-dimensional interference
        f4 = 0.3 * np.sum((x_norm[:-1] * x_norm[1:]) * 
                          (1 + 0.6 * np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:])) * 
                          (1 + 0.2 * np.cos(4 * np.pi * x_norm[:-1])) * 
                          (1 + 0.1 * np.sin(6 * np.pi * x_norm[1:-1])))
        
        # Fourth-order polynomial with random coefficient modulation, harmonic terms, and cross-dimensional coupling
        f5 = 0.2 * np.sum((x_norm**4) * (1 + 0.3 * np.sin(4 * np.pi * x_norm)) * 
                          (1 + 0.2 * np.cos(3 * np.pi * x_norm)) * 
                          (1 + 0.1 * np.sin(5 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with non-uniform scaling, delay effects, and additional interference
        f6 = 0.25 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) ** 2.0 * 
                          (1 + 0.5 * np.cos(6 * np.pi * x_norm[:-1])) * 
                          (1 + 0.1 * np.sin(5 * np.pi * x_norm[1:-1])) * 
                          (1 + 0.3 * np.cos(2 * np.pi * x_norm[:-1])))
        
        # Additional high-frequency chaotic component with enhanced non-linearity and harmonic coupling
        f7 = 0.1 * np.sum(np.sin(17 * np.pi * x_norm) * np.cos(21 * np.pi * x_norm) * 
                         np.exp(-0.35 * x_norm**2) * (1 + 0.4 * np.sin(9 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(8 * np.pi * x_norm)))
        
        # Add a global scaling factor to increase the overall difficulty
        return 1.3 * (f1 + f2 + f3 + f4 + f5 + f6 + f7)
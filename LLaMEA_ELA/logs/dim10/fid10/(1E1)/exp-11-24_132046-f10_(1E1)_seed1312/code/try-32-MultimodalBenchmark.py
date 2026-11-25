import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with dimension-dependent scaling and enhanced nonlinearity
        f1 = np.sum(x_norm**2 * (1 + 0.15 * np.abs(x_norm) + 0.05 * x_norm**4))
        
        # Enhanced chaotic oscillation with higher frequency components, phase modulation, and amplitude control
        f2 = 0.7 * np.sum(np.sin(11 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                         np.exp(-0.5 * np.abs(x_norm)) * (1 + 0.5 * np.sin(7 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.cos(9 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying steepness, additional harmonic components, and parity-based modulation
        f3 = 0.5 * np.sum(np.exp(-x_norm**2) * np.sin(5 * np.pi * x_norm) * 
                         (1 + 0.4 * np.cos(7 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.sin(3 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(5 * np.pi * x_norm)))
        
        # Conditional interaction with parity-based activation, memory effect, and cross-dimensional coupling
        f4 = 0.3 * np.sum((x_norm[:-1] * x_norm[1:]) * 
                          (1 + 0.6 * np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:])) * 
                          (1 + 0.2 * np.cos(4 * np.pi * x_norm[:-1])) * 
                          (1 + 0.15 * np.sin(3 * np.pi * x_norm[1:-1])))
        
        # Fourth-order polynomial with random coefficient modulation, additional harmonic terms, and fractal scaling
        f5 = 0.2 * np.sum((x_norm**4) * (1 + 0.4 * np.sin(4 * np.pi * x_norm)) * 
                          (1 + 0.3 * np.cos(3 * np.pi * x_norm)) * 
                          (1 + 0.25 * np.sin(6 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with non-uniform scaling, delay effects, and multi-scale interference
        f6 = 0.3 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) ** 2.1 * 
                         (1 + 0.5 * np.cos(6 * np.pi * x_norm[:-1])) * 
                         (1 + 0.2 * np.sin(5 * np.pi * x_norm[1:-1])) * 
                         (1 + 0.1 * np.cos(7 * np.pi * x_norm[:-1])))
        
        # Additional high-frequency chaotic component with enhanced non-linearity and recursive modulation
        f7 = 0.1 * np.sum(np.sin(20 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * 
                         np.exp(-0.5 * x_norm**2) * (1 + 0.4 * np.sin(9 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(11 * np.pi * x_norm)))
        
        # Fractal-like structure with recursive harmonic components and multi-scale amplitude modulation
        f8 = 0.15 * np.sum(np.sin(30 * np.pi * x_norm) * np.cos(37 * np.pi * x_norm) * 
                         (1 + 0.3 * np.sin(13 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(19 * np.pi * x_norm)) * 
                         (1 + 0.15 * np.sin(23 * np.pi * x_norm)))
        
        # Multi-scale interference patterns with varying amplitude modulation and harmonic coupling
        f9 = 0.08 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) * 
                         (1 + 0.4 * np.sin(11 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.cos(15 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.sin(17 * np.pi * x_norm)))
        
        # Additional chaotic modulation with memory effect and dimensional coupling
        f10 = 0.06 * np.sum(np.sin(23 * np.pi * x_norm) * np.cos(29 * np.pi * x_norm) * 
                          (1 + 0.35 * np.sin(8 * np.pi * x_norm)) * 
                          (1 + 0.25 * np.cos(12 * np.pi * x_norm)) * 
                          (1 + 0.18 * np.sin(16 * np.pi * x_norm)))
        
        # Add a global scaling factor to increase the overall difficulty
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)
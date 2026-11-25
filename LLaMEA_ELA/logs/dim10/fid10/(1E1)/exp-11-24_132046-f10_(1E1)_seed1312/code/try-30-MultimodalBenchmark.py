import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with dimension-dependent scaling and adaptive coefficients
        f1 = np.sum(x_norm**2 * (1 + 0.2 * np.abs(x_norm)) * (1 + 0.1 * np.sin(3 * x_norm)))
        
        # Enhanced chaotic oscillation with higher frequency components, phase modulation, and amplitude control
        f2 = 0.8 * np.sum(np.sin(11 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                         np.exp(-0.5 * np.abs(x_norm)) * (1 + 0.5 * np.sin(7 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.cos(9 * np.pi * x_norm)))
        
        # Asymmetric saddle points with varying steepness, harmonic components, and exponential decay
        f3 = 0.5 * np.sum(np.exp(-x_norm**2) * np.sin(5 * np.pi * x_norm) * 
                         (1 + 0.4 * np.cos(7 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.sin(3 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(5 * np.pi * x_norm)))
        
        # Conditional interaction with parity-based activation, memory effect, and non-linear coupling
        f4 = 0.3 * np.sum((x_norm[:-1] * x_norm[1:]) * 
                          (1 + 0.6 * np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:])) * 
                          (1 + 0.2 * np.cos(4 * np.pi * x_norm[:-1])) * 
                          (1 + 0.1 * np.sin(3 * np.pi * x_norm[1:-1])))
        
        # Fourth-order polynomial with random coefficient modulation, harmonic terms, and additional non-linearities
        f5 = 0.2 * np.sum((x_norm**4) * (1 + 0.4 * np.sin(4 * np.pi * x_norm)) * 
                          (1 + 0.3 * np.cos(3 * np.pi * x_norm)) * 
                          (1 + 0.2 * np.sin(5 * np.pi * x_norm)) * 
                          (1 + 0.1 * np.cos(6 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with non-uniform scaling, delay effects, and multi-scale interactions
        f6 = 0.3 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) ** 2.0 * 
                         (1 + 0.5 * np.cos(6 * np.pi * x_norm[:-1])) * 
                         (1 + 0.2 * np.sin(5 * np.pi * x_norm[1:-1])) * 
                         (1 + 0.1 * np.cos(7 * np.pi * x_norm[:-1])))
        
        # Additional high-frequency chaotic component with enhanced non-linearity and multi-scale modulation
        f7 = 0.12 * np.sum(np.sin(19 * np.pi * x_norm) * np.cos(23 * np.pi * x_norm) * 
                         np.exp(-0.5 * x_norm**2) * (1 + 0.4 * np.sin(9 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(11 * np.pi * x_norm)))
        
        # Fractal-like structure with recursive harmonic components and multi-scale interference
        f8 = 0.15 * np.sum(np.sin(31 * np.pi * x_norm) * np.cos(37 * np.pi * x_norm) * 
                         (1 + 0.3 * np.sin(13 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.cos(19 * np.pi * x_norm)) * 
                         (1 + 0.1 * np.sin(23 * np.pi * x_norm)))
        
        # Multi-scale interference patterns with varying amplitude modulation, frequency mixing, and phase coupling
        f9 = 0.08 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm) * 
                         (1 + 0.4 * np.sin(11 * np.pi * x_norm)) * 
                         (1 + 0.3 * np.cos(15 * np.pi * x_norm)) * 
                         (1 + 0.2 * np.sin(17 * np.pi * x_norm)))
        
        # Additional high-order interaction terms with increased complexity and non-uniform scaling
        f10 = 0.1 * np.sum((x_norm**6) * (1 + 0.3 * np.cos(5 * np.pi * x_norm)) * 
                          (1 + 0.2 * np.sin(7 * np.pi * x_norm)) * 
                          (1 + 0.1 * np.cos(9 * np.pi * x_norm)))
        
        # Add a global scaling factor to increase the overall difficulty and introduce more aggressive non-linearities
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)
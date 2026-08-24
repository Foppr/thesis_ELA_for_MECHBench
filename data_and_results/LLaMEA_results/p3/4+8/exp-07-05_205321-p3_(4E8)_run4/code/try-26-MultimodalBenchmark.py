import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal interference with varying frequencies
        chaotic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * 
                        np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential decay with Gaussian-like behavior
        exponential = np.sum(np.exp(-0.5 * x_scaled**2) * np.sin(10 * x_scaled)**2)
        
        # Saddle point structure with interaction terms
        saddle = np.sum(x_scaled[:-1]**3 * x_scaled[1:])
        
        # Hyperbolic tangent interaction for flat regions
        hyperbolic = np.sum(np.tanh(x_scaled)**2)
        
        # Combine all terms with different weights
        return 0.15 * quadratic + 0.35 * chaotic + 0.25 * exponential + 0.15 * saddle + 0.1 * hyperbolic + 3.0
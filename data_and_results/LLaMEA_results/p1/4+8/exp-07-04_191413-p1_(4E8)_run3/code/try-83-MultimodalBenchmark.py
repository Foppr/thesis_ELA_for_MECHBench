import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with varying degrees
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric components with multiple frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(5 * np.pi * x_norm) + 
                          0.3 * np.sin(8 * np.pi * x_norm))
        
        # Chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(np.pi * x_norm * (1 + np.sin(3 * np.pi * x_norm))) * 
                        np.exp(-0.1 * x_norm**2))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.1 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                                    (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Adaptive conditioning based on dimension
        conditioning = np.sum((1 + 0.1 * self.dim) * x_norm**2)
        
        # Combine all terms with different weights
        return poly_term + 0.7 * trig_term + 0.4 * chaotic + 0.2 * cross_coupling + conditioning
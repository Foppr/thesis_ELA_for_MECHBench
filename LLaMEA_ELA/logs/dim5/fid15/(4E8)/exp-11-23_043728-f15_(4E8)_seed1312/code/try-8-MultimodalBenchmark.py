import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base function
        quadratic = np.sum(x_norm**2)
        
        # Sinusoidal oscillations with exponential decay
        oscillation = np.sum(np.exp(-np.abs(x_norm)) * np.sin(3 * np.pi * x_norm)**2)
        
        # Repulsive barriers at boundaries
        barrier = np.sum(1.0 / (1.0 + np.exp(2 * (np.abs(x_norm) - 0.8))) + 
                        1.0 / (1.0 + np.exp(2 * (0.8 - np.abs(x_norm)))))
        
        # Cross-term interactions
        cross_term = 0.5 * np.sum(np.sin(2 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]))
        
        return quadratic + oscillation + barrier + cross_term
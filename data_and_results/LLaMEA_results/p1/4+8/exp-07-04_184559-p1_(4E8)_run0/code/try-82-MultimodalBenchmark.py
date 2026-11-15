import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponentially decaying basis functions
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(5 * np.pi * r))
        
        # Sinusoidal spiral term to create rotational complexity
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(9 * theta) * np.cos(5 * theta) * np.exp(-2 * r)
        else:
            spiral = 0.0
            
        # Additional high-frequency oscillation in all dimensions with chaotic modulation
        chaotic_mod = np.prod(np.sin(15 * x_norm + np.sin(x_norm)))
        
        # Cross-term interaction between dimensions
        cross_term = np.sum(np.sin(2 * x_norm) * np.cos(3 * x_norm) * np.exp(-0.5 * r**2))
        
        # Quadratic penalty to keep solution near origin
        penalty = 0.3 * np.sum(x_norm**2)
        
        # Add a chaotic logistic map component for enhanced complexity
        logistic = 0.0
        if self.dim > 0:
            logistic = np.sum(np.mod(3.8 * np.abs(x_norm) * (1 - np.abs(x_norm)), 1))
        
        # Combine all components
        return radial + 2.5 * spiral + chaotic_mod + cross_term + penalty + 0.1 * logistic
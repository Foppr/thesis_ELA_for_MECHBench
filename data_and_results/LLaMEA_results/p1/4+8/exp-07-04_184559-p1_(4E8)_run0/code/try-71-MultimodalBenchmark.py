import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponentially decaying basis functions
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(4 * np.pi * r))
        
        # Sinusoidal spiral term to create rotational complexity
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(5 * theta) * np.cos(3 * theta)
        else:
            spiral = 0.0
            
        # Additional high-frequency oscillation in all dimensions
        oscillation = np.sum(np.sin(12 * x_norm) * np.cos(6 * x_norm))
        
        # Quadratic penalty to keep solution near origin
        penalty = 0.3 * np.sum(x_norm**2)
        
        # Chaotic logistic map component for added complexity
        logistic = 0.0
        if self.dim >= 2:
            logistic = 0.1 * (4 * x_norm[0] * (1 - x_norm[0]) + 4 * x_norm[1] * (1 - x_norm[1]))
        
        # Cross-term interaction between dimensions
        cross_term = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all components
        return radial + 1.5 * spiral + oscillation + penalty + logistic + cross_term
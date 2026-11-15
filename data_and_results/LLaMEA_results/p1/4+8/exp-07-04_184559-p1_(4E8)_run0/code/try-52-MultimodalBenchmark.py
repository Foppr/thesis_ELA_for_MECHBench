import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponentially decaying basis functions
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-5 * r**2) * np.cos(3 * np.pi * r))
        
        # Sinusoidal spiral term to create rotational complexity
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(7 * theta) * np.cos(4 * theta)
        else:
            spiral = 0.0
            
        # Additional high-frequency oscillation in all dimensions
        oscillation = np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Quadratic penalty to keep solution near origin
        penalty = 0.5 * np.sum(x_norm**2)
        
        # Combine all components
        return radial + 2 * spiral + oscillation + penalty
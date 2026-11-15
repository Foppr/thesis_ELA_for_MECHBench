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
            spiral = np.sin(9 * theta) * np.cos(5 * theta)
        else:
            spiral = 0.0
            
        # Chaotic phase modulation component using logistic map
        if self.dim >= 2:
            logistic_input = 4.0 * (x_norm[0] + 0.5) * (1 - (x_norm[0] + 0.5))
            chaotic_mod = np.sin(15 * logistic_input)
        else:
            chaotic_mod = 0.0
            
        # Additional high-frequency oscillation in all dimensions with adaptive frequency
        freq_factor = 1.0 + 0.5 * np.sin(r)
        oscillation = np.sum(np.sin(freq_factor * 12 * x_norm) * np.cos(freq_factor * 10 * x_norm))
        
        # Quadratic penalty to keep solution near origin
        penalty = 0.3 * np.sum(x_norm**2)
        
        # Add a global scaling factor and noise term for increased complexity
        noise = 0.05 * np.random.rand()
        
        # Combine all components
        return radial + 2.5 * spiral + chaotic_mod + oscillation + penalty + noise
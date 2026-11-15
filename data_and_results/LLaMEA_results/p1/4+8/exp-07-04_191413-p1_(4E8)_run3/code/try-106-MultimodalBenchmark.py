import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_decay = np.exp(-r**2)
        
        # Multi-layered sinusoidal modulations with increasing frequencies
        sin_layer1 = np.sum(np.sin(2 * np.pi * x_norm) ** 2)
        sin_layer2 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        sin_layer3 = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += x_norm[i] * x_norm[i+1] * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Chaotic modulation using a logistic map-like term
        logistic_mod = 0.0
        for i in range(self.dim):
            logistic_mod += np.sin(10 * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Add a polynomial interaction term for increased complexity
        poly_term = 0.1 * np.sum(x_norm**6)
        
        # Combine all components with different weights
        return radial_decay + 0.5 * sin_layer1 + 0.3 * sin_layer2 + 0.2 * sin_layer3 + 0.1 * coupling + 0.15 * logistic_mod + poly_term
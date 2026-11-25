import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r) * r**2
        
        # Harmonic oscillations in multiple directions
        harmonic_sum = 0.0
        for i in range(self.dim):
            # Create directional harmonics with different frequencies
            freq = 2**(i % 3 + 1)
            harmonic_sum += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Add radial oscillation component
        radial_oscillation = np.sum(np.sin(3 * np.pi * r) * np.cos(3 * np.pi * r))
        
        # Combine all terms with different weights
        result = radial_term + 0.5 * harmonic_sum + 0.1 * radial_oscillation
        
        return result
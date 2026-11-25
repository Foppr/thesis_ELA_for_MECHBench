import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multiple quadratic wells with different centers and scales
        well1 = np.sum((x - 1.0)**2 + (x + 1.0)**2)
        well2 = np.sum((x - 2.0)**2 + (x + 2.0)**2)
        well3 = np.sum((x - 0.5)**2 + (x + 0.5)**2)
        
        # Sinusoidal modulation to create periodic variations
        sin_mod = np.sum(np.sin(0.8 * x) * np.cos(0.6 * x))
        
        # Additional high-frequency oscillation component
        high_freq = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Combine all components with different weights
        result = 0.3 * well1 + 0.2 * well2 + 0.1 * well3 + 0.2 * sin_mod + 0.2 * high_freq
        
        return result
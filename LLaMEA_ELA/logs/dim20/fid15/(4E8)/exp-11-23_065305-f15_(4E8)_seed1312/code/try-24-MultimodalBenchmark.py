import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Exponential decay component with sinusoidal modulation
        exp_term = np.sum(np.exp(-x_scaled**2) * np.cos(3 * np.pi * x_scaled))
        
        # Trigonometric polynomial creating multiple local minima
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Saddle-point structure with mixed powers
        saddle_term = np.sum(x_scaled**3 * np.sin(x_scaled) + x_scaled**5 * np.cos(x_scaled))
        
        # Combine all terms with different weights
        result = 0.5 * exp_term + 0.3 * trig_term + 0.2 * saddle_term
        
        return result
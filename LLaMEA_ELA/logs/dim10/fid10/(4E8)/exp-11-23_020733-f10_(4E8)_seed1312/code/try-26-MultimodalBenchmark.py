import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with varying degrees
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Trigonometric terms creating multiple local minima with higher frequencies
        trig_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Exponential barrier term with modified parameters for steeper gradients
        exp_barrier = np.sum(np.exp(-x_scaled**2 / 0.3) * (1 - np.exp(-x_scaled**2 / 0.1)))
        
        # Additional exponential interaction term between dimensions
        exp_interaction = np.sum(np.exp(-(x_scaled[:-1]**2 + x_scaled[1:]**2)) * np.sin(np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Cross-term creating interaction between dimensions with sine modulation
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(2 * np.pi * x_scaled[:-1]))
        
        # Shifted global minimum to (0.1, 0.1, ..., 0.1) to increase difficulty
        shift = np.sum((x_scaled - 0.02)**2)
        
        # Combine all terms with different weights
        return 0.8 * poly_term + 0.4 * trig_term + 0.25 * exp_barrier + 0.15 * exp_interaction + 0.1 * cross_term + 0.05 * shift
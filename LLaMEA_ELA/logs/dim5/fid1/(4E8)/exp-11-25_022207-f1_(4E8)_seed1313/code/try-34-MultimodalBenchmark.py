import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified exponential decay terms with varying rates
        exp_term = np.sum(np.exp(-np.abs(x_norm) * (1.0 + 0.3 * np.cos(2 * x_norm))) * (1.0 + 0.4 * np.sin(4 * x_norm)))
        
        # Enhanced trigonometric oscillations with higher frequencies
        trig_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Additional asymmetric saddle points with cubic and quartic terms
        saddle_term = np.sum(x_norm**3 * np.exp(-0.3 * x_norm**2) + 0.1 * x_norm**4)
        
        # Cross-dimensional interaction with modified weights
        cross_term = 0.15 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**1.7)
        
        # Add a global scaling factor to control the overall landscape complexity
        return exp_term + trig_term + saddle_term + cross_term
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_term = np.sum(np.exp(-np.abs(x_norm)) * (1.0 + 0.5 * np.sin(3 * x_norm)))
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_term = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Asymmetric saddle points with polynomial interactions
        saddle_term = np.sum(x_norm**3 * np.exp(-0.5 * x_norm**2))
        
        # Cross-dimensional interaction with asymmetric weights
        cross_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**1.5)
        
        # Add a global scaling factor to control the overall landscape complexity
        return exp_term + trig_term + saddle_term + cross_term
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with different rates
        exp_term = np.sum(np.exp(-np.abs(x_norm)) * np.cos(2 * np.pi * x_norm))
        
        # Trigonometric interaction terms with varying frequencies
        trig_term = np.sum(np.sin(np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Sine wave component with shifted phase to create multiple minima
        sine_term = np.sum(np.sin(4 * np.pi * (x_norm + 0.2)) ** 2)
        
        # Product of all dimensions with a global scaling factor
        product_term = np.prod(x_norm ** 2 + 0.1)
        
        # Combine terms with varying weights and add a constant offset
        result = 0.3 * exp_term + 0.4 * trig_term + 0.2 * sine_term + 0.1 * product_term
        
        return result
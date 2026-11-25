import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with varying exponents
        poly_term = np.sum((x_scaled ** 3) * (x_scaled ** 2 + 0.5))
        
        # Trigonometric component with multiple frequencies
        trig_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Exponential penalty term that increases complexity
        exp_term = np.sum(np.exp(-x_scaled ** 2) * (1 + 0.1 * np.sin(20 * x_scaled)))
        
        # Cross-term interaction creating non-separability
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(3 * np.pi * x_scaled[:-1]))
        
        # Combine all terms with different weights
        return 0.5 * poly_term + 0.3 * trig_term + 0.2 * exp_term + 0.1 * cross_term
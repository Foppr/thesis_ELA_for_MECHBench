import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with different degrees
        poly_term = np.sum(x_scaled**6) + 0.5 * np.sum(x_scaled**4) + 0.1 * np.sum(x_scaled**2)
        
        # Exponential terms that create steep gradients and multiple local optima
        exp_term = np.sum(np.exp(2 * x_scaled**2) - 1)
        
        # Trigonometric terms with varying frequencies to increase multimodality
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Cross-terms that create interaction between dimensions
        cross_term = 0.3 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combine all terms to form the final landscape
        return poly_term + 0.5 * exp_term + 0.2 * trig_term + cross_term
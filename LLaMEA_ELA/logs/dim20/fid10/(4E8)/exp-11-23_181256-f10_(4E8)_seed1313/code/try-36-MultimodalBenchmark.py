import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6)
        
        # Exponential terms creating steep gradients
        exp_term = np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        # Logarithmic barrier terms preventing boundary escape
        log_term = np.sum(np.log(1 + 0.1 * x_scaled**2))
        
        # Sine wave interactions creating oscillating valleys
        sine_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Cross-terms enhancing dimension interaction
        cross_term = 0.3 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Global minimum at origin with additional scaling
        return 2.0 * poly_term + 1.5 * exp_term + 0.8 * log_term + 1.2 * sine_term + cross_term + 0.5 * np.sum(x_scaled**8)
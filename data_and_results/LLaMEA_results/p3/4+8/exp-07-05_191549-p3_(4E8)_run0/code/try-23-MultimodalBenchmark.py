import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial conditioning term
        poly_term = np.sum(x_scaled**6 - 3*x_scaled**4 + 2*x_scaled**2)
        
        # Nested sinusoidal oscillations with varying frequencies
        sin_term = np.sum(np.sin(20 * np.pi * x_scaled) * np.sin(10 * np.pi * x_scaled) * np.sin(5 * np.pi * x_scaled))
        
        # Exponential modulation to create rugged terrain
        exp_mod = np.sum(np.exp(-5 * np.abs(x_scaled)) * np.sin(15 * np.pi * x_scaled)**2)
        
        # Cross-term interaction
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * np.cos(4 * np.pi * x_scaled[1:]))
        
        # Combine all terms with different weights
        return 0.4 * poly_term + 0.3 * sin_term + 0.2 * exp_mod + 0.1 * cross_term
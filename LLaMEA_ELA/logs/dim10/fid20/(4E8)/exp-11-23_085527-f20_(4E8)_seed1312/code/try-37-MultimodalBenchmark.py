import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees including cubic and quartic
        poly_term = np.sum(0.8 * x_norm**4 + 0.6 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric components creating high-frequency oscillations
        trig_term = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) + 
                          np.sin(7 * np.pi * x_norm**2) * np.cos(11 * np.pi * x_norm**2))
        
        # Exponential barrier terms with sharper gradients
        exp_term = np.sum(np.exp(-2.0 * x_norm**2) - 1.0)
        
        # Cross-terms creating non-separability and increased complexity
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(4 * np.pi * x_norm[:-1]))
        
        # Combined function with different weights
        return 2.5 * poly_term + 4.0 * trig_term + 0.7 * exp_term + 0.3 * cross_term
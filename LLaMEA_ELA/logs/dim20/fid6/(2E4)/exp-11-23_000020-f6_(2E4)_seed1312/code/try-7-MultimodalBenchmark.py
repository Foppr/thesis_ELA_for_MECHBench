import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic term for conditioning
        quad_term = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with different frequencies
        sin_term = np.sum(np.sin(3 * np.pi * x_norm)**2 + 
                         0.5 * np.sin(7 * np.pi * x_norm)**2 + 
                         0.3 * np.sin(11 * np.pi * x_norm)**2)
        
        # Gaussian-like terms creating multiple local minima
        gaussian_term = np.sum(np.exp(-2 * (x_norm**2)) * 
                              np.cos(2 * np.pi * x_norm)**2)
        
        # Cross-term interaction creating complex landscape
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * 
                           np.sin(np.pi * x_norm[:-1]) * 
                           np.cos(np.pi * x_norm[1:]))
        
        # Combine all terms with appropriate weights
        return 0.2 * quad_term + 0.4 * sin_term + 0.3 * gaussian_term + 0.1 * cross_term + 1.0
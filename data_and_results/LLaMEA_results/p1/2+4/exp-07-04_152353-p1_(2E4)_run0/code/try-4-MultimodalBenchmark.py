import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # High-frequency trigonometric oscillations creating many local minima
        freq_terms = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Nested multimodal structure with varying scales
        nested = np.sum((x_norm**6 - 3 * x_norm**4 + 3 * x_norm**2 - 1) * np.exp(-0.5 * x_norm**2))
        
        # Saddle point landscape via mixed polynomial and exponential terms
        saddle = np.sum(x_norm * np.exp(-0.5 * x_norm**2) * np.sin(3 * np.pi * x_norm))
        
        # Non-separable interaction terms between dimensions
        interaction = np.sum(np.sin(np.pi * (x_norm[0] + x_norm[1])) * np.cos(np.pi * (x_norm[0] - x_norm[1])))
        
        # Combine all components with varying weights
        return 0.5 * quadratic + 0.3 * freq_terms + 0.2 * nested + 0.1 * saddle + 0.05 * interaction
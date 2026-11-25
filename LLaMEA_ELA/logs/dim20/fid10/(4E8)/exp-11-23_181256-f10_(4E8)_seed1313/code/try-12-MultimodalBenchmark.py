import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay terms that create steep gradients
        exp_terms = np.sum(np.exp(-x_scaled**2) * np.cos(2 * np.pi * x_scaled))
        
        # Trigonometric oscillations with varying frequencies
        trig_terms = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Polynomial penalty terms that introduce local minima
        poly_terms = np.sum(x_scaled**6 - 2 * x_scaled**4 + x_scaled**2)
        
        # Cross-terms that create dependencies between dimensions
        cross_terms = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(np.pi * x_scaled[:-1]))
        
        return exp_terms + 0.5 * trig_terms + 0.1 * poly_terms + 0.05 * cross_terms
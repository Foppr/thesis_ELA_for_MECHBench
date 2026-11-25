import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(x_scaled**6) + 0.5 * np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**2)
        
        # Trigonometric components with multiple frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled)**2) + np.sum(np.cos(3 * np.pi * x_scaled)**2)
        
        # Exponential interaction terms
        exp_term = np.sum(np.exp(-x_scaled**2)) + 0.5 * np.sum(np.exp(-(x_scaled - 0.5)**2))
        
        # Cross-dimensional interaction using pairwise products
        cross_term = 0.1 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Add a global scaling factor and noise
        result = 2.0 * poly_term + 1.5 * trig_term + exp_term + cross_term
        
        # Add small random noise for landscape variation
        noise = 0.01 * np.random.random()
        
        return result + noise
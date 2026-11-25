import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_terms = np.sum(np.exp(-np.abs(x_scaled)) * np.cos(2 * np.pi * x_scaled))
        
        # Trigonometric oscillations with different frequencies
        trig_terms = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Quadratic penalty term
        quad_penalty = 0.5 * np.sum(x_scaled**2)
        
        # Chaotic component using sine of squared terms
        chaotic = np.sum(np.sin(x_scaled**2) * np.exp(-x_scaled**2))
        
        return exp_terms + trig_terms + quad_penalty + chaotic
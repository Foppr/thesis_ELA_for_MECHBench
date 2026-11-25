import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with exponential growth and sinusoidal modulation
        chaotic_term = np.sum(np.exp(2 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm))
        
        # Saddle point structure with hyperbolic tangents for complex curvature
        saddle_term = np.sum(np.tanh(3 * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Variable conditioning with dimension-dependent scaling
        condition_term = np.sum((x_norm ** 2) * (1 + 0.5 * np.sin(self.dim * np.pi * x_norm)))
        
        # Cross-term correlations creating non-linear dependencies
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Global minimum at origin with additional chaotic oscillations
        result = chaotic_term + saddle_term - condition_term + cross_term
        
        return result
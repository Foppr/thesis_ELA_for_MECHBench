import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic component using sine and exponential functions
        chaotic_term = np.sum(np.exp(2 * np.sin(np.pi * x_norm)) * np.cos(3 * np.pi * x_norm))
        
        # Saddle-point inducing term with multiple interacting variables
        saddle_term = 0.5 * np.sum(x_norm[:-1]**2 * x_norm[1:]**2)
        
        # Add noise with exponential decay to create irregularity
        noise = 0.1 * np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * x_norm))
        
        # Combine all components with varying weights
        return f1 + 0.3 * chaotic_term + 0.2 * saddle_term + noise
import numpy as np

class HybridRuggedBowlBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical bowl component
        sphere = np.sum(x_norm**2)
        
        # Exponential decay with sinusoidal modulation
        exp_decay = np.sum(np.exp(-x_norm**2) * (1 + 0.5 * np.sin(10 * x_norm)))
        
        # Sinusoidal oscillation with varying frequency
        sin_oscillation = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Adaptive conditioning based on distance from origin
        adaptive_cond = np.sum((1 + 0.3 * np.abs(x_norm)) * np.exp(-0.5 * x_norm**2))
        
        # Local ruggedness with multiple small peaks
        ruggedness = np.sum(0.5 * np.sin(20 * x_norm) * np.cos(15 * x_norm) + 
                           0.3 * np.sin(30 * x_norm) * np.cos(25 * x_norm))
        
        # Cross-dimensional interaction with power-law scaling
        cross_dim = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(1.5 + 0.5 * np.sin(5 * x_norm[:-1])))
        
        # Asymmetric barrier structure
        barrier = np.sum(10 * (np.exp(-0.5 * (x_norm - 0.5)**2) - 
                              np.exp(-0.5 * (x_norm + 0.5)**2)))
        
        # Combined function with weighted components
        return 0.8 * sphere + 1.2 * exp_decay + 0.9 * sin_oscillation + \
               1.1 * adaptive_cond + 0.7 * ruggedness + 0.6 * cross_dim + 0.5 * barrier
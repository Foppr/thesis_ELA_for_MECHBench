import numpy as np

class RuggedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic conditioning term
        quadratic = np.sum(x_norm**2)
        
        # Periodic oscillatory components with varying amplitudes and frequencies
        oscillations = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Correlated variables with interaction terms
        correlated = np.sum((x_norm[:-1] + x_norm[1:])**2 * np.sin(2 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]))
        
        # Central global minimum with rugged surrounding landscape
        center_distance = np.sum((x_norm - 0.3)**2)
        rugged = np.sum(np.exp(-center_distance) * np.sin(15 * np.pi * x_norm)**2)
        
        # Multi-scale periodic structure
        multi_scale = np.sum(np.sin(30 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.8 * oscillations + 1.2 * correlated + 2.0 * rugged + 0.7 * multi_scale
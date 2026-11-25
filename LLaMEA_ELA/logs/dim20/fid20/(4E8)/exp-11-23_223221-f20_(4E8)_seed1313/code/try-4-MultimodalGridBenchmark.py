import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create a grid of global minima at positions that are multiples of 1/3
        grid_positions = np.array([i/3 for i in range(-15, 16)] * self.dim).reshape(self.dim, -1)
        
        # Calculate distance to nearest grid point
        distances = np.abs(x_norm[:, None] - grid_positions).min(axis=0)
        
        # Base function: sum of squared distances to grid points
        base_value = np.sum(distances**2)
        
        # Add sinusoidal modulation with varying frequencies
        modulation = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Add a quadratic penalty term for being far from the origin
        penalty = 0.1 * np.sum(x**2)
        
        return base_value + modulation + penalty
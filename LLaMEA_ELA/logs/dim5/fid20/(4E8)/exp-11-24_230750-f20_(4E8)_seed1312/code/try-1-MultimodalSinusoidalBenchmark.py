import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Main sinusoidal grid component with multiple global minima
        grid_term = np.sum(np.sin(scaled_x) * np.cos(scaled_x))
        
        # Quadratic basin term to create wider optima regions
        basin_term = 0.1 * np.sum(x**2)
        
        # Additional harmonic terms for increased complexity
        harmonic_term = 0.05 * np.sum(np.sin(3 * scaled_x) + np.cos(2 * scaled_x))
        
        # Combine all terms with different weights
        result = grid_term + basin_term + harmonic_term
        
        # Add a small constant to ensure function is bounded below
        return result + 10.0
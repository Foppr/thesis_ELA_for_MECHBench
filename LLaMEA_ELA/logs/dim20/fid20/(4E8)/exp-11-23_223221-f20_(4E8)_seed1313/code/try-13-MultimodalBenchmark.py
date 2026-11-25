import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with multiple frequencies
        sinusoidal = np.sum(np.sin(3.0 * x) * np.sin(7.0 * x)) * np.exp(-0.05 * np.sum(x**2))
        
        # Cross-term interactions with exponential decay
        cross_terms = np.sum(x[:-1] * x[1:] * np.exp(-0.1 * np.sum(np.abs(x[:-1] - x[1:])))) * 0.3
        
        # Grid-like global minima pattern
        grid_pattern = np.sum(np.sin(2.0 * np.pi * x) * np.cos(2.0 * np.pi * x))
        
        # Exponential decay term to create basins
        basin_term = np.exp(-0.5 * np.sum((x - 1.0)**2)) + np.exp(-0.5 * np.sum((x + 1.0)**2))
        
        return polynomial + sinusoidal + cross_terms + grid_pattern + basin_term
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree and additional complexity
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with multiple frequencies and grid-based modulation
        freq1 = np.sin(5.0 * x)
        freq2 = np.sin(3.0 * x)
        grid_modulation = np.prod(np.sin(0.5 * x) + 1.0) + 1.0
        
        sinusoidal = (np.sum(freq1) + np.sum(freq2)) * np.exp(-0.1 * np.sum(x**2)) * grid_modulation
        
        # Cross-term interactions with additional coupling
        cross_terms = np.sum(x[:-1] * x[1:]) * 0.5 + 0.1 * np.sum(x**2 * x[::-1]**2)
        
        # Add a grid of local minima using cosine modulation
        grid_minima = np.sum(np.cos(2.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        return polynomial + sinusoidal + cross_terms + grid_minima
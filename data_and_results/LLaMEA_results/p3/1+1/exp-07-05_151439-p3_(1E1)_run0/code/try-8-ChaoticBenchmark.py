import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using sine waves with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(10 * x) * np.cos(7 * x)) / self.dim
        
        # Polynomial penalty terms to create rugged terrain
        poly_term = np.sum(x**4 + 0.1 * x**3 - 0.5 * x**2 + 2 * x) / self.dim
        
        # Exponential barrier terms to create sharp transitions near boundaries
        barrier_term = np.sum(np.exp(-x**2 / 2.0) * np.sin(x)) / self.dim
        
        # Add a chaotic attractor component with multiple local minima
        attractor_term = np.sum(np.sin(np.exp(x)) * np.cos(np.exp(-x))) / self.dim
        
        # Combine all terms with different weights to create complex landscape
        result = 0.5 * chaotic_term + 0.3 * poly_term + 0.1 * barrier_term + 0.1 * attractor_term
        
        # Add a small noise component to increase irregularity
        noise = 0.01 * np.random.rand()
        
        return result + noise
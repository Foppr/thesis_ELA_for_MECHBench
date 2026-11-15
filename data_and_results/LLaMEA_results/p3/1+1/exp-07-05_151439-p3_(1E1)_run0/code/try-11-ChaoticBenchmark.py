import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using sine waves with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(15 * x) * np.cos(5 * x)) / self.dim
        
        # Polynomial penalty terms to create rugged terrain
        poly_term = np.sum(x**4 + 0.2 * x**3 - 0.6 * x**2 + 1.5 * x) / self.dim
        
        # Exponential barrier terms to create sharp transitions near boundaries
        barrier_term = np.sum(np.exp(-x**2 / 1.5) * np.sin(2 * x)) / self.dim
        
        # Add a chaotic attractor component with multiple local minima
        attractor_term = np.sum(np.sin(np.exp(x/2.0)) * np.cos(np.exp(-x/3.0))) / self.dim
        
        # Add cross-dimensional interaction terms
        cross_term = np.sum((x[:-1] - x[1:])**2) / (self.dim - 1) if self.dim > 1 else 0
        
        # Combine all terms with different weights to create complex landscape
        result = 0.4 * chaotic_term + 0.35 * poly_term + 0.15 * barrier_term + 0.1 * attractor_term + 0.05 * cross_term
        
        # Add a small noise component to increase irregularity
        noise = 0.01 * np.random.rand()
        
        return result + noise
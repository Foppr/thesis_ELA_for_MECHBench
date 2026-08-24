import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for basin structure
        self.weights = np.arange(1, dim + 1)
        
    def f(self, x):
        # Radial component with varying condition numbers
        r = np.sqrt(np.sum(x**2))
        radial = np.sum((x**2) * self.weights)
        
        # Sinusoidal oscillations in multiple directions
        oscillation = np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        # Exponential barriers near boundaries
        barrier = np.sum(np.exp(2 * (np.abs(x) - 2.5)) * (np.abs(x) > 2.5))
        
        # Add a global minimum at origin with additional noise
        noise = 0.05 * np.random.rand()
        
        # Combine all components
        return 0.5 * radial + 2.0 * oscillation + 1.5 * barrier + noise
import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbfs = np.sum(np.exp(-np.sum((x - np.linspace(-4, 4, self.dim))**2) / (2 * (1 + 0.1 * np.sin(self.dim * 0.5)))))
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                         np.sin(4 * np.pi * x) * np.cos(5 * np.pi * x) * 
                         np.sin(6 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Adaptive conditioning component
        conditioning = np.sum((1 + 0.5 * np.sin(self.dim * 0.3)) * x**2 + 
                             (0.8 + 0.3 * np.cos(self.dim * 0.4)) * x**3 + 
                             (0.6 + 0.2 * np.sin(self.dim * 0.5)) * x**4)
        
        # Cross-dimensional coupling with modified interaction weights
        coupling = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += (1 + 0.3 * np.sin(i * 0.7)) * np.abs(x[i] - x[i+1])**2
        coupling /= (self.dim - 1)
        
        # Add noise component
        noise = 0.01 * np.random.rand()
        
        # Combine all terms
        result = (0.5 * rbfs + 
                 0.3 * sin_term + 
                 0.1 * conditioning + 
                 0.05 * coupling + 
                 noise)
        
        return result
import numpy as np

class MultimodalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                              np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x)) / self.dim
        
        # Adaptive conditioning based on dimensionality and position
        conditioning = np.sum((1 + 0.5 * np.sin(self.dim)) * x**2 + 
                             (2 + 0.3 * np.cos(self.dim)) * x**4 + 
                             (1.5 + 0.4 * np.sin(self.dim)) * x**6) / self.dim
        
        # Saddle point structure with hyperbolic tangent components
        saddle_term = np.sum(np.tanh(x) * np.tanh(2 * x) * 
                            np.sinh(x) * np.cosh(x)) / self.dim
        
        # Multi-scale fractal-like structure with recursive self-similarity
        fractal_term = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * 
                             np.sin(2 * np.pi * x) * np.cos(2 * np.pi * x) * 
                             np.sin(4 * np.pi * x) * np.cos(4 * np.pi * x)) / self.dim
        
        # Cross-dimensional interaction with adaptive coupling strength
        coupling = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += (1 + 0.3 * np.sin(i + self.dim * 0.5)) * np.abs(x[i] - x[i+1]) * 
                           np.exp(-0.5 * (x[i] - x[i+1])**2)
        coupling /= (self.dim - 1)
        
        # Add noise with adaptive amplitude based on dimensionality
        noise = 0.01 * np.random.rand() * (1 + 0.1 * np.sin(self.dim)) * np.sum(np.sin(x))
        
        # Combine all terms with dynamic weights
        weights = [0.35 + 0.05 * np.sin(self.dim), 
                  0.25 + 0.03 * np.cos(self.dim), 
                  0.20 + 0.04 * np.sin(self.dim), 
                  0.15 + 0.02 * np.cos(self.dim), 
                  0.05 + 0.01 * np.sin(self.dim)]
        
        result = (weights[0] * periodic_term + 
                 weights[1] * conditioning + 
                 weights[2] * saddle_term + 
                 weights[3] * fractal_term + 
                 weights[4] * coupling)
        
        return result + noise
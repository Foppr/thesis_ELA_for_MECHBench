import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay potential wells
        potential = 0.0
        for i in range(self.dim):
            potential += np.exp(-0.5 * (x_normalized[i] - 0.3)**2) + \
                        0.5 * np.exp(-0.5 * (x_normalized[i] + 0.7)**2) + \
                        0.3 * np.exp(-0.5 * (x_normalized[i] - 0.9)**2)
        
        # Trigonometric coupling between variables
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.sin(3 * x_normalized[i]) * np.cos(2 * x_normalized[j]) * \
                           np.exp(-0.1 * (x_normalized[i] - x_normalized[j])**2)
        
        # Adaptive conditioning based on variable position
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 3.0 * np.abs(x_normalized[i])
            conditioning += cond_factor * x_normalized[i]**4
        
        # Cross-terms creating complex interaction patterns
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_normalized[i] * x_normalized[j])**2 * \
                              np.sin(0.5 * (x_normalized[i] + x_normalized[j]))
        
        # Gaussian noise component with varying intensity
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.01) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Combine all components with different weights
        return (0.3 * potential + 0.4 * coupling + 0.2 * conditioning + 
                0.08 * cross_terms + 0.02 * noise)
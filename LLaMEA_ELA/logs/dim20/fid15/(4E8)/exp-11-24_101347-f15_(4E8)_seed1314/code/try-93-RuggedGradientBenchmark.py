import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay corridors
        corridor_term = 0.0
        for i in range(self.dim):
            corridor_term += np.exp(-np.abs(x_scaled[i]) * 2.0) * np.sin(5.0 * x_scaled[i])
        
        # Gaussian hill structures with adaptive heights
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 1.0 + 0.5 * np.sin(3.0 * x_scaled[i])
            width = 0.5 + 0.3 * np.cos(2.0 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Adaptive gradient modulation based on position
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.3 * np.sin(4.0 * x_scaled[i]))
        
        # Cross-dimensional interaction with varying coupling strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.cos(3.0 * (x_scaled[i] + x_scaled[j]))
                coupling_term += coupling_strength * np.sin(7.0 * (x_scaled[i] - x_scaled[j]))
        
        # Ruggedness through high-frequency oscillations
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(20.0 * x_scaled[i]) * np.cos(15.0 * x_scaled[i])
        
        # Combined result with dynamic weighting
        result = (0.4 * corridor_term + 
                 0.3 * gaussian_term + 
                 0.2 * coupling_term + 
                 0.1 * ruggedness) * grad_mod
        
        return result
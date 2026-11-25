import numpy as np

class RuggedGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay corridors with modified decay rate
        corridor_term = 0.0
        for i in range(self.dim):
            corridor_term += np.exp(-np.abs(x_scaled[i]) * 3.5) * np.sin(6.5 * x_scaled[i])
        
        # Gaussian hill structures with altered heights and widths
        gaussian_term = 0.0
        for i in range(self.dim):
            height = 1.6 + 0.2 * np.sin(4.5 * x_scaled[i])
            width = 0.35 + 0.35 * np.cos(3.5 * x_scaled[i])
            gaussian_term += height * np.exp(-0.5 * (x_scaled[i] / width)**2)
        
        # Enhanced adaptive gradient modulation
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1.0 + 0.35 * np.sin(5.5 * x_scaled[i]))
        
        # Cross-dimensional interaction with modified coupling strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.65 + 0.35 * np.cos(4.5 * (x_scaled[i] + x_scaled[j]))
                coupling_term += coupling_strength * np.sin(8.5 * (x_scaled[i] - x_scaled[j]))
        
        # Enhanced ruggedness through higher frequency oscillations
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(26.0 * x_scaled[i]) * np.cos(21.0 * x_scaled[i])
        
        # Combined result with modified dynamic weighting
        result = (0.32 * corridor_term + 
                 0.38 * gaussian_term + 
                 0.22 * coupling_term + 
                 0.08 * ruggedness) * grad_mod
        
        return result
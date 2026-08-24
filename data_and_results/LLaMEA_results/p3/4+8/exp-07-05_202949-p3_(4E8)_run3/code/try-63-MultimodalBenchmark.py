import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Asymmetric bell-shaped components with varying widths and heights
        result = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i)
            height = 2.0 + 0.3 * np.cos(i)
            result += height * np.exp(-0.5 * ((x[i] - 1.0) / width)**2) + \
                      0.5 * np.exp(-0.5 * ((x[i] + 1.0) / (width * 0.5))**2)
        
        # Coupled sine-wave modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                freq = 1.0 + 0.2 * (i + j)
                amp = 0.8 + 0.2 * np.sin(i * j)
                result += amp * np.sin(freq * x[i]) * np.cos(freq * x[j])
        
        # Dynamic global minimum based on dimensionality
        global_min_shift = np.sum(np.sin(np.arange(self.dim) * 0.5))
        result += 0.1 * np.sum((x - global_min_shift)**2)
        
        # Add a complex interaction term with polynomial and exponential components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.05 * interaction
        
        # Add periodicity with non-uniform frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + \
                      0.2 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Add a small noise component to increase robustness testing
        result += 0.001 * np.sum(np.random.rand(self.dim) * x**2)
        
        return result
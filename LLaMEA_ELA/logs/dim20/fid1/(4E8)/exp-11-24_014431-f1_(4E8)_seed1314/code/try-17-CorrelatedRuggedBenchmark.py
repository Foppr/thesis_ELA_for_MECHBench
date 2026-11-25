import numpy as np

class CorrelatedRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Rugged component with exponentially decaying correlation structure
        ruggedness = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation between dimensions
                decay = np.exp(-0.1 * (j - i))
                ruggedness += decay * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j])
        
        # Additional multimodal component with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            f3 += (np.sin(7 * np.pi * x_norm[i]) ** 4) + (np.cos(5 * np.pi * x_norm[i]) ** 3)
        
        return f1 + 0.2 * ruggedness + 0.05 * f3
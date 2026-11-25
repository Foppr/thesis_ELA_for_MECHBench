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
                decay = np.exp(-0.15 * (j - i))
                ruggedness += decay * np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j])
        
        # Additional multimodal component with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            f3 += (np.sin(9 * np.pi * x_norm[i]) ** 4) + (np.cos(7 * np.pi * x_norm[i]) ** 3)
        
        # Cross-term interaction enhancement
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.5 * np.sin(4 * np.pi * x_norm[i]) * np.sin(4 * np.pi * x_norm[j])
        
        return f1 + 0.3 * ruggedness + 0.08 * f3 + 0.1 * cross_term
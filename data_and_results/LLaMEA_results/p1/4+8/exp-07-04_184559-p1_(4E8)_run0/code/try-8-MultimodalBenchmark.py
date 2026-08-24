import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.5 * np.sin(3 * np.pi * x_norm)))**2)
        
        # Polynomial interaction term with high degree
        f3 = np.sum((x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)**2)
        
        # Exponentially scaled component to create steep gradients
        f4 = np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # Cross-term interaction creating complex landscape
        f5 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * x_norm[:-1]))
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5
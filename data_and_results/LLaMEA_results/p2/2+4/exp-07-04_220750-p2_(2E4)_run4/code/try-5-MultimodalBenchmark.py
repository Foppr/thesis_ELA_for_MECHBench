import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with multiple local minima
        f2 = 0.1 * np.sum(np.cos(5 * np.pi * x_norm))
        
        # Additional challenging term with exponential decay
        f3 = np.sum(np.abs(x_norm) ** 1.5) * np.exp(-0.5 * np.sum(x_norm**2))
        
        # Add a sinusoidal modulation to increase landscape complexity
        f4 = 0.05 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        return f1 + f2 + f3 + f4
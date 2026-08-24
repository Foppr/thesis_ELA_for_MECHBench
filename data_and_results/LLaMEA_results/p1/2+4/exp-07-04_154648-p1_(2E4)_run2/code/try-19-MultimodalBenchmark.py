import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Enhanced multimodal terms with modified frequencies and exponents
        f2 = 0.35 * np.sum(np.sin(11 * np.pi * x_norm)**12)
        f3 = 0.28 * np.sum(np.cos(6 * np.pi * x_norm)**10)
        f4 = 0.18 * np.sum(np.sin(4 * np.pi * x_norm)**7)
        f5 = 0.12 * np.sum((x_norm + 0.15)**7)
        f6 = 0.09 * np.sum(np.cos(8 * np.pi * x_norm)**5)
        
        # Cross-terms with modified interaction pattern
        cross_term = 0.06 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * x_norm[:-1]))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + cross_term
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with increased frequency and amplitude
        f2 = 0.2 * np.sum(np.cos(7 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.02 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + f4
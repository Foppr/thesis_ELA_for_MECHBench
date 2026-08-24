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
        f2 = 0.3 * np.sum(np.cos(9 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.03 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.05 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.01 * np.sum(np.abs(x_norm)**5)
        
        return f1 + f2 + f3 + f4 + f5 + f6
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
        f2 = 0.5 * np.sum(np.cos(10 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.05 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.15 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.08 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.02 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 0.2 * np.sum(np.sin(8 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.01 * np.sum(x_norm**6)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
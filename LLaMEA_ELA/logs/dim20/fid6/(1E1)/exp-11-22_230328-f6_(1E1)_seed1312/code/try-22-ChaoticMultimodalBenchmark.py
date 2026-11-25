import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Chaotic component using logistic map-like behavior
        f3 = 0.2 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                          np.sin(2 * np.pi * x_norm)**2)
        
        # Cross-terms creating intricate interaction patterns
        f4 = 0.1 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * np.sin(3 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # High-order polynomial for increased non-convexity
        f5 = 0.05 * np.sum(x_norm**6)
        
        # Add a complex interaction between all dimensions
        f6 = 0.15 * np.sum(np.sin(7 * np.pi * x_norm) * 
                           np.cos(5 * np.pi * x_norm) * 
                           np.sin(2 * np.pi * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6
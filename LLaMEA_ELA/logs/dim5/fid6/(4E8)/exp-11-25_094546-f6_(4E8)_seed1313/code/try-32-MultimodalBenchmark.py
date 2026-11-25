import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with chaotic sine waves and radial symmetry
        f2 = 0.3 * np.sum(np.cos(15 * np.pi * x_norm) * np.sin(12 * np.pi * x_norm) * 
                          np.exp(-0.5 * np.sum(x_norm**2, axis=0, keepdims=True)))
        
        # Additional higher-order polynomial terms with adaptive weights
        f3 = 0.05 * np.sum((x_norm**6 + 0.2 * x_norm**7 + 0.05 * x_norm**8))
        
        # Composite multimodal term with varying frequencies and amplitude modulation
        f4 = 0.25 * np.sum(np.sin(25 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) * 
                           (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Radial penalty term with exponential decay
        f5 = 0.1 * np.sum(np.exp(-2 * np.sum(x_norm**2, axis=0, keepdims=True)) * 
                          np.abs(x_norm)**3)
        
        return f1 + f2 + f3 + f4 + f5
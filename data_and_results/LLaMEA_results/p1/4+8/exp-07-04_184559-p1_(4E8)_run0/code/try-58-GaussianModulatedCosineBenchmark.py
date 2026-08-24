import numpy as np

class GaussianModulatedCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multimodal cosine waves with varying frequencies
        f2 = np.sum(np.cos(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Gaussian hills to create local optima
        f3 = np.sum(np.exp(-5.0 * (x_norm**2)))
        
        # Cross-term interactions to increase complexity
        f4 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Modulation term that varies across dimensions
        modulation = np.prod(1 + 0.5 * np.sin(np.pi * x_norm))
        
        # Combine all terms with different weights
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 * modulation
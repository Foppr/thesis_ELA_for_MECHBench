import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with exponential scaling
        f2 = np.sum(np.sin(10 * np.pi * x_norm**3) ** 2)
        
        # Multi-modal component with multiple peaks and valleys
        f3 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Saddle point inducing term with polynomial interaction
        f4 = np.sum(x_norm**4 - 2 * x_norm**2)
        
        # Exponentially increasing complexity term
        f5 = np.sum(np.exp(2 * np.abs(x_norm)) * np.sin(5 * np.pi * x_norm)**2)
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5
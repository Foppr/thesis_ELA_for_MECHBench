import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for global convergence
        f1 = np.sum(x_norm**2)
        
        # Multiple overlapping sinusoidal terms with varying frequencies
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        f3 = np.sum(np.sin(3 * np.pi * x_norm) ** 4)
        f4 = np.sum(np.cos(7 * np.pi * x_norm) ** 2)
        
        # Polynomial conditioning term to create varied curvature
        f5 = np.sum(x_norm**4)
        
        # Adaptive noise based on input magnitude
        noise = 0.2 * np.mean(np.abs(x_norm)) * np.random.random()
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.1 * f5 + noise
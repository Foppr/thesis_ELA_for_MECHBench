import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm)**4)
        
        # Additional sinusoidal term with different frequency and amplitude
        f3 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Cubic term for non-convexity and saddle points
        f4 = np.sum(x_norm**3)
        
        # Exponential barrier terms to create challenging landscape near boundaries
        barrier = np.sum(np.exp(-1.0 / (1.0 - x_norm**2 + 1e-10)))
        
        return f1 + 0.2 * f2 + 0.15 * f3 + 0.02 * f4 + 0.5 * barrier
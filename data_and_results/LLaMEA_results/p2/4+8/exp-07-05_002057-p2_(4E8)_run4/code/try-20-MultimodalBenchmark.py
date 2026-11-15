import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with adaptive scaling
        f1 = 0.5 * np.sum(x**2)
        
        # Chaotic oscillatory term with exponential modulation
        f2 = 0.3 * np.sum(np.sin(15 * x) * np.exp(-0.3 * np.abs(x)) * np.cos(7 * x))
        
        # High-frequency sine-cosine coupled term
        f3 = 0.25 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.exp(-0.15 * x**2))
        
        # Modified Gaussian-modulated cosine term
        f4 = 0.2 * np.sum(np.cos(20 * x) * np.exp(-0.2 * np.abs(x)) * (1 + 0.1 * np.sin(3 * x)))
        
        # Cross-dimensional interaction with chaotic coupling
        f5 = 0.1 * np.sum(np.sin(x[:-1] * x[1:] * 3.14159) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Adaptive exponential damping term
        f6 = 0.15 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(18 * x))
        
        # Combined chaotic and oscillatory term
        f7 = 0.1 * np.sum(np.sin(10 * x) * np.cos(13 * x) * np.exp(-0.25 * x**2) * np.sin(5 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
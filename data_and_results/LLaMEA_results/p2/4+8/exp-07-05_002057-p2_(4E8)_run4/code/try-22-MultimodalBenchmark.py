import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # Multimodal term with chaotic modulation and shifted sinusoidal component
        f2 = 0.2 * np.sum(np.sin(10 * x + 1.0) * np.exp(-0.2 * x**2))
        
        # Additional high-frequency oscillatory term with different decay and shift
        f3 = 0.15 * np.sum(np.cos(15 * x + 0.5) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction with chaotic modulation
        f4 = 0.05 * np.sum(np.sin(3 * x + 0.7) * np.cos(7 * x + 0.3) * np.exp(-0.05 * x**2))
        
        # Chaotic modulation term to increase landscape irregularity
        f5 = 0.1 * np.sum(np.sin(20 * np.sin(x)) * np.exp(-0.02 * x**2))
        
        return f1 + f2 + f3 + f4 + f5
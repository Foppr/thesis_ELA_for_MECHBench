import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced multimodal component with varying frequencies and amplitudes
        f2 = 0.2 * np.sum(np.sin(7.0 * x) * np.cos(4.0 * x) * np.sin(2.0 * x))
        
        # Additional sinusoidal interference to increase complexity
        f3 = 0.15 * np.sum(np.sin(12.0 * x) + np.cos(9.0 * x))
        
        # Adaptive scaling term to control landscape difficulty
        f4 = 0.05 * np.sum((x**4) * np.sin(3.0 * x))
        
        # Combine all terms
        return f1 + f2 + f3 + f4
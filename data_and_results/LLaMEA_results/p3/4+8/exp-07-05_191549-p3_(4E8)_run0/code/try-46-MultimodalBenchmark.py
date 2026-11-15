import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced multimodal component with chaotic sine waves and radial symmetry
        f2 = 0.2 * np.sum(np.sin(8.0 * x) * np.cos(5.0 * x) * np.sin(3.0 * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Additional sinusoidal interference with varying frequencies
        f3 = 0.15 * np.sum(np.sin(13.0 * x) + np.cos(10.0 * x) + np.sin(6.0 * x))
        
        # Adaptive scaling term with exponential barrier
        f4 = 0.05 * np.sum((x**4) * np.sin(4.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Mixed exponential-barrier terms to increase complexity
        f5 = 0.1 * np.sum(np.exp(-0.5 * x**2) * np.sin(2.0 * x)**2)
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5
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
        f2 = 0.3 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Additional chaotic interference with varying frequencies
        f3 = 0.2 * np.sum(np.sin(15.0 * x) + np.cos(11.0 * x) + np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Adaptive conditioning with radial scaling
        r = np.sqrt(np.sum(x**2))
        f4 = 0.1 * np.sum((x**3) * np.sin(4.0 * x) * np.exp(-0.1 * r))
        
        # Mixed exponential-barrier terms to create rugged terrain
        f5 = 0.15 * np.sum(np.exp(-0.5 * x**2) * np.sin(6.0 * x) + np.exp(-0.3 * x**2) * np.cos(5.0 * x))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5
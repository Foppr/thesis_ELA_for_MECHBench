import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin with multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = 12 * np.exp(-0.15 * np.sum((x - 1)**2))
        term3 = 6 * np.exp(-0.03 * np.sum((x + 1)**2))
        term4 = 3 * np.sin(0.5 * np.sum(x**2))  # Added sinusoidal perturbation
        term5 = 2 * np.cos(0.3 * np.sum((x - 2)**2))  # Additional cosine term
        
        return term1 + term2 + term3 + term4 + term5 - 23
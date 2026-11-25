import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin terms
        poly_term = np.sum(x**4) / self.dim
        
        # Sinusoidal perturbations creating chaotic behavior
        sin_term = np.sum(np.sin(5 * x)) / self.dim
        
        # Chaotic component with exponential decay
        chaotic_term = np.exp(-0.1 * np.sum(x**2)) * np.sin(10 * np.sum(x))
        
        # Add noise-like structure
        noise_term = 0.5 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        return poly_term + sin_term + chaotic_term + noise_term + 2.0
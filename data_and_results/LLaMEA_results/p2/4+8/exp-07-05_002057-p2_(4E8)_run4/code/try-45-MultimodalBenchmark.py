import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term with logarithmic conditioning
        f1 = np.sum(x**2 * (1.0 + 0.1 * np.log(1.0 + x**2)))
        
        # Enhanced chaotic multimodal term with sine-wave perturbations
        f2 = 0.3 * np.sum(np.sin(15 * x) * np.exp(-0.3 * x**2) * np.sin(3 * x**2))
        
        # Additional high-frequency chaotic term
        f3 = 0.25 * np.sum(np.sin(30 * x) * np.exp(-0.2 * x**2) * np.cos(5 * x))
        
        # Modified cosine term with logarithmic barrier
        f4 = 0.2 * np.sum(np.cos(20 * x) * np.exp(-0.15 * x**2) * (1.0 + 0.05 * np.log(1.0 + x**2)))
        
        # Cross-term interaction with chaotic sine-wave perturbations
        f5 = 0.1 * np.sum(x[:-1] * x[1:] * np.sin(8 * (x[:-1] + x[1:])) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Additional nonlinear interaction with logarithmic conditioning
        f6 = 0.15 * np.sum((x[:-1]**2) * (x[1:]**2) * np.sin(4 * (x[:-1] + x[1:])) * np.log(1.0 + x[:-1]**2 + x[1:]**2))
        
        # Chaotic logarithmic conditioning term
        f7 = 0.05 * np.sum(np.log(1.0 + x**2) * np.sin(10 * x) * np.exp(-0.25 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
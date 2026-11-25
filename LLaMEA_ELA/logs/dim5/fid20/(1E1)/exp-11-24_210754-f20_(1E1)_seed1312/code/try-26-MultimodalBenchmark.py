import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal oscillations with exponential growth and adaptive scaling
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x) * np.exp(-0.1 * np.abs(x)))
        
        # Polynomial corruption with varying degrees and cross-dimensional interactions
        f3 = 0.01 * np.sum(x**7 + 0.6 * x**6 + 0.3 * x**5 + 0.1 * x**4 + 
                          0.05 * np.prod(x.reshape(-1, 1), axis=0) * np.ones_like(x))
        
        # Add saddle point structure with stronger interaction and directional bias
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)) * 
                         np.sin(0.5 * np.sum(x**2)))
        
        # Introduce additional chaotic component with dynamic frequency modulation
        f5 = 0.08 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * 
                          np.sin(2.0 * np.sqrt(np.sum(x**2))))
        
        # Cross-dimensional interaction term for increased complexity
        f6 = 0.1 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # Combine all terms with adaptive weights based on dimensionality
        weight_factor = 1.0 + 0.1 * np.log(self.dim)
        return weight_factor * (f1 + f2 + f3 + f4 + f5 + f6)
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos components
        term1 = np.sum(x**2)
        term2 = 0.5 * np.sum(x**4)
        term3 = 0.3 * np.sum(x**6)
        
        # Trigonometric coupling
        term4 = 0.4 * np.sum(np.sin(2 * x) * np.cos(3 * x))
        term5 = 0.3 * np.sum(np.sin(5 * x) * np.cos(7 * x))
        
        # Adaptive radial barriers
        barrier = 0.2 * np.sum(1.0 / (1.0 + np.exp(-10 * (np.linalg.norm(x) - 2.0))))
        
        # Dynamic conditioning
        cond = 0.1 * np.sum(x**2 * np.sin(10 * x))
        
        # Noise injection
        noise = 0.05 * np.sum(np.random.normal(0, 1, self.dim))
        
        # Multi-scale sinusoidal modulation
        modulation = 0.2 * np.sum(np.sin(15 * x) * np.cos(8 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Higher-order polynomial interactions
        interaction = 0.1 * np.sum((x[:-1] - x[1:]) ** 4)
        
        result = term1 + term2 + term3 + term4 + term5 + barrier + cond + noise + modulation + interaction
        
        return result
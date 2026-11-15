import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos components
        term1 = np.sum(x**4)
        term2 = 0.5 * np.sum(x**3 * np.sin(x))
        term3 = 0.3 * np.sum(x**2 * np.cos(2 * x))
        
        # Trigonometric coupling
        coupling = 0.4 * np.sum(np.sin(x) * np.cos(3 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Adaptive radial barriers
        radial = 0.6 * np.sum(np.exp(-0.5 * (x**2 - np.mean(x**2))**2) * np.sin(10 * x))
        
        # Dynamic conditioning
        condition = 0.2 * np.sum((x**2 + 1) * np.sin(5 * x) * np.cos(2 * x))
        
        # Noise injection
        noise = 0.1 * np.sum(np.random.normal(0, 1, self.dim) * np.sin(x))
        
        # Additional chaotic components
        chaotic = 0.15 * np.sum(np.sin(10 * np.sin(x)) * np.cos(5 * np.cos(x)))
        
        result = term1 + term2 + term3 + coupling + radial + condition + noise + chaotic
        
        return result
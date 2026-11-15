import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal components
        term1 = np.sum(x**2)
        term2 = 0.5 * np.sum(np.sin(5 * x) * np.cos(3 * x))
        term3 = 0.1 * np.sum(x**4 * np.sin(2 * x))
        term4 = 0.3 * np.sum(np.exp(-x**2) * np.sin(10 * x))
        term5 = 0.05 * np.sum(np.abs(x) ** 3.5)
        
        # Add interaction terms between dimensions
        interaction = 0.02 * np.sum((x[:-1] - x[1:]) ** 2 * np.sin(5 * (x[:-1] + x[1:])))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result
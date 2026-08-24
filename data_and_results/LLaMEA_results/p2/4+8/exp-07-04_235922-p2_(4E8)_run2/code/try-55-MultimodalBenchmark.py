import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal components with modified parameters
        term1 = np.sum(x**2)
        term2 = 0.7 * np.sum(np.sin(6 * x) * np.cos(4 * x))
        term3 = 0.15 * np.sum(x**4 * np.sin(3 * x))
        term4 = 0.4 * np.sum(np.exp(-0.5 * x**2) * np.sin(12 * x))
        term5 = 0.08 * np.sum(np.abs(x) ** 3.8)
        
        # Enhanced interaction terms between dimensions
        interaction = 0.03 * np.sum((x[:-1] - x[1:]) ** 2 * np.sin(6 * (x[:-1] + x[1:])))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal components with modified parameters
        term1 = np.sum(x**2)
        term2 = 0.75 * np.sum(np.sin(7 * x) * np.cos(3 * x))
        term3 = 0.18 * np.sum(x**4 * np.sin(4 * x))
        term4 = 0.35 * np.sum(np.exp(-0.4 * x**2) * np.sin(10 * x))
        term5 = 0.09 * np.sum(np.abs(x) ** 3.5)
        
        # Enhanced interaction terms between dimensions
        interaction = 0.04 * np.sum((x[:-1] - x[1:]) ** 2 * np.sin(7 * (x[:-1] + x[1:])))
        
        # Cross-dimensional coupling with higher-order interactions
        cross_dim = 0.02 * np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(5 * (x[:-2] + x[1:-1] + x[2:])))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + cross_dim
        
        # Add a small noise term to make it more challenging
        result += 0.0015 * np.random.random()
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        # Combines quadratic, quartic, and high-frequency sinusoidal terms
        # Plus cross-term interactions to create a more challenging landscape
        result = (np.sum(x**2) + 
                 0.1 * np.sum(np.sin(10 * x)) + 
                 0.05 * np.sum(x**4) +
                 0.02 * np.sum(x**6) +
                 0.3 * np.sum(np.sin(3 * x) * np.cos(7 * x)) +
                 0.01 * np.sum(x * np.roll(x, 1)) +  # Cross-term interaction
                 0.005 * np.sum((x - np.mean(x))**2))
        
        return result
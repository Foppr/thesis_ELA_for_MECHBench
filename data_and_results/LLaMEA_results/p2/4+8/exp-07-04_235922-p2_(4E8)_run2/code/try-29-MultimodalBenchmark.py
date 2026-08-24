import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with higher frequency sinusoids, 
        # quartic interactions, and a shifted global minimum
        result = np.sum(x**2) + 0.3 * np.sum(np.sin(5 * x)) + 0.03 * np.sum(x**4) + 0.1 * np.sum(x[:-1] * x[1:]) + 0.01 * np.sum((x - 1)**4)
        
        # Add small noise for additional challenge
        result += 0.001 * np.random.random()
        
        return result
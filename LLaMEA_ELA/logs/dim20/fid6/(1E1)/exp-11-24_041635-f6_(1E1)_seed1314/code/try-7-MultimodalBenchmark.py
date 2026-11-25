import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        result = (np.sum(x**2) + 
                 0.5 * np.sum(np.sin(15.0 * x)) + 
                 0.6 * np.sum(np.exp(0.4 * np.abs(x))) + 
                 0.05 * np.sum(x**3) + 
                 0.08 * np.sum(x**6) + 
                 0.3 * np.sum(np.cos(8.0 * x)) + 
                 0.2 * np.sum(np.sin(20.0 * x)**2) + 
                 0.1 * np.sum(np.exp(-0.2 * x**2)))
        
        return result
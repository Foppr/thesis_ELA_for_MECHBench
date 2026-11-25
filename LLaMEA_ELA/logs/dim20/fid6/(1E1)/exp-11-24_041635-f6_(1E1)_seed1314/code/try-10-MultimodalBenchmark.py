import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        result = (np.sum(x**2) + 
                 0.8 * np.sum(np.sin(12.0 * x)) + 
                 0.7 * np.sum(np.exp(0.3 * np.abs(x))) + 
                 0.1 * np.sum(x**3) + 
                 0.15 * np.sum(x**6) + 
                 0.4 * np.sum(np.cos(10.0 * x)) + 
                 0.25 * np.sum(np.sin(25.0 * x)**2) + 
                 0.15 * np.sum(np.exp(-0.3 * x**2)) +
                 0.05 * np.sum(np.sin(30.0 * x) * np.cos(5.0 * x)) +
                 0.3 * np.sum((x**4) * np.exp(-0.1 * np.abs(x))))
        
        return result
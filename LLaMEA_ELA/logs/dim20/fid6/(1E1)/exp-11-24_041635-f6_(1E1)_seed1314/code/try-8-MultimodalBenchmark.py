import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Shifted enhanced multimodal function with modified interactions
        shifted_x = x - 0.5 * np.sin(0.3 * x)
        
        result = (np.sum(shifted_x**2) + 
                 0.7 * np.sum(np.sin(18.0 * shifted_x)) + 
                 0.5 * np.sum(np.exp(0.3 * np.abs(shifted_x))) + 
                 0.06 * np.sum(shifted_x**3) + 
                 0.1 * np.sum(shifted_x**6) + 
                 0.4 * np.sum(np.cos(9.0 * shifted_x)) + 
                 0.25 * np.sum(np.sin(25.0 * shifted_x)**2) + 
                 0.15 * np.sum(np.exp(-0.3 * shifted_x**2)) + 
                 0.02 * np.sum(shifted_x[:-1] * shifted_x[1:]))
        
        return result
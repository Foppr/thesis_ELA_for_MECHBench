import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Highly complex multimodal function with chaotic interactions
        result = (np.sum(x**2) + 
                 2.5 * np.sum(np.sin(27.0 * x)**3) + 
                 1.8 * np.sum(np.exp(-0.35 * x**2)) + 
                 0.9 * np.sum(x**4) + 
                 0.7 * np.sum(np.cos(13.0 * x)**2) + 
                 1.1 * np.sum(np.sin(32.0 * x) * np.cos(16.0 * x)) + 
                 0.6 * np.sum(np.exp(-0.12 * np.abs(x))) + 
                 0.5 * np.sum(np.sin(52.0 * x)**4) + 
                 0.35 * np.sum(x**7) + 
                 0.25 * np.sum(np.exp(-0.06 * x**4)) + 
                 1.3 * np.sum(np.sin(11.0 * x) * np.exp(-0.22 * x**2)))
        
        return result
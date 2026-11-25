import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Highly complex multimodal function with chaotic interactions
        result = (np.sum(x**2) + 
                 2.0 * np.sum(np.sin(25.0 * x)**3) + 
                 1.5 * np.sum(np.exp(-0.3 * x**2)) + 
                 0.8 * np.sum(x**4) + 
                 0.6 * np.sum(np.cos(12.0 * x)**2) + 
                 1.2 * np.sum(np.sin(30.0 * x) * np.cos(15.0 * x)) + 
                 0.5 * np.sum(np.exp(-0.1 * np.abs(x))) + 
                 0.4 * np.sum(np.sin(50.0 * x)**4) + 
                 0.3 * np.sum(x**7) + 
                 0.2 * np.sum(np.exp(-0.05 * x**4)) + 
                 1.0 * np.sum(np.sin(10.0 * x) * np.exp(-0.2 * x**2)) +
                 0.7 * np.sum(np.sin(35.0 * x)**2 * np.cos(7.0 * x)) +
                 0.9 * np.sum(np.exp(-0.4 * x**3) * np.sin(20.0 * x)) +
                 0.6 * np.sum(x**(1.5)) +
                 1.1 * np.sum(np.cos(8.0 * x) * np.exp(-0.1 * x**3)) +
                 0.5 * np.sum(np.sin(40.0 * x)**2 * np.exp(-0.05 * x**2)))
        
        return result
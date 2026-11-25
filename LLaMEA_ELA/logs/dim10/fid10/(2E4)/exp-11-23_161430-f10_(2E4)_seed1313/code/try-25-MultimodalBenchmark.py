import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle-point landscape with modified dynamics
        result = (np.sum(np.exp(-0.15 * x**2)) + 
                 0.6 * np.sum(np.sin(4 * x) * np.cos(2 * x)) +
                 0.4 * np.sum(np.exp(-0.03 * (x - 1.5)**2) * np.sin(8 * x)) +
                 0.3 * np.sum(np.exp(-0.01 * (x + 2.5)**2) * np.cos(6 * x)) +
                 0.2 * np.sum(x**4 * np.sin(1.5 * x)) +
                 0.1 * np.sum(np.abs(x) * np.exp(-0.08 * x**2)) +
                 0.08 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.03 * x**2)) +
                 0.05 * np.sum((x - np.mean(x))**5) +
                 0.03 * np.sum(np.sin(3 * x) * np.exp(-0.02 * x**2)) +
                 0.02 * np.sum(np.cos(4 * x) * np.exp(-0.04 * x**2)))
        
        return result
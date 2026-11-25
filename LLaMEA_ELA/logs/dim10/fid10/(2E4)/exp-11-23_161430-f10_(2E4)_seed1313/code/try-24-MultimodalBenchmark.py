import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle-point landscape with higher-order terms
        result = (np.sum(np.exp(-0.1 * x**2)) + 
                 0.5 * np.sum(np.sin(5 * x) * np.cos(3 * x)) +
                 0.3 * np.sum(np.exp(-0.05 * (x - 1)**2) * np.sin(10 * x)) +
                 0.2 * np.sum(np.exp(-0.02 * (x + 2)**2) * np.cos(8 * x)) +
                 0.1 * np.sum(x**3 * np.sin(2 * x)) +
                 0.05 * np.sum(np.abs(x) * np.exp(-0.1 * x**2)) +
                 0.03 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.05 * x**2)) +
                 0.01 * np.sum((x - np.mean(x))**4) +
                 0.02 * np.sum(np.sin(7 * x) * np.cos(4 * x) * np.exp(-0.03 * x**2)) +
                 0.015 * np.sum(x**4 * np.cos(3 * x)) +
                 0.01 * np.sum((x**2 - 1)**3) +
                 0.005 * np.sum(np.exp(-0.2 * (x - np.mean(x))**2) * np.sin(15 * x)) +
                 0.008 * np.sum(np.abs(x)**1.5 * np.cos(6 * x)))
        
        return result
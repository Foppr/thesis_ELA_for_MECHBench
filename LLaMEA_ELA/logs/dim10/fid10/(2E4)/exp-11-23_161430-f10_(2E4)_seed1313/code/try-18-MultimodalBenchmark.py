import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point landscape with exponential decay and sinusoidal modulations
        result = (np.sum(np.exp(-0.1 * x**2)) + 
                 0.5 * np.sum(np.sin(5 * x) * np.cos(3 * x)) +
                 0.3 * np.sum(np.exp(-0.05 * (x - 1)**2) * np.sin(10 * x)) +
                 0.2 * np.sum(np.exp(-0.02 * (x + 2)**2) * np.cos(8 * x)) +
                 0.1 * np.sum(x**3 * np.sin(2 * x)) +
                 0.05 * np.sum(np.abs(x) * np.exp(-0.1 * x**2)) +
                 0.03 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.05 * x**2)) +
                 0.01 * np.sum((x - np.mean(x))**4))
        
        return result
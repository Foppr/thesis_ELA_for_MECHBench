import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-r / 2.0) * (1.0 + 0.5 * np.sin(r))
        
        # Trigonometric interference terms
        interference = np.sum(np.cos(3.0 * x) * np.sin(7.0 * x)) + 0.3 * np.sum(np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Polynomial scaling with chaotic perturbation
        polynomial = np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Combine all components
        return radial + interference + polynomial + 0.05 * np.sum(np.abs(x)**3.5)
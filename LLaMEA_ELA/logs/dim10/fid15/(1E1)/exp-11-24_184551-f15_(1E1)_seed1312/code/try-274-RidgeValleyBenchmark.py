import numpy as np

class RidgeValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Global minimum at center
        center = np.zeros(self.dim)
        
        # Base quadratic term for basin
        quadratic = 0.1 * np.sum((x - center)**2)
        
        # Ridge and valley terms with exponential decay
        ridge_valley = 0.0
        for i in range(self.dim):
            # Create exponentially decaying ridges/valleys
            decay_factor = np.exp(-0.5 * i)
            ridge_valley += decay_factor * (np.sin(x[i]) + 0.5 * np.sin(2 * x[i]))
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.exp(-0.1 * (x[i] - x[j])**2) * (x[i]**2 + x[j]**2)
        
        # Add noise to make it non-trivial
        noise = 0.01 * np.sum(np.sin(5 * x))
        
        return quadratic - ridge_valley + interaction + noise
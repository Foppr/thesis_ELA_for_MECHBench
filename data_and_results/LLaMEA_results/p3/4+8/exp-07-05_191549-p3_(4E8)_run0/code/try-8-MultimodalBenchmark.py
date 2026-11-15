import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_val = np.sum(x**2)
        
        # Add radial symmetry with exponentially decaying sinusoidal terms
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            f_val += 2.0 * np.exp(-r/2.0) * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Add multiple local minima using high-frequency sinusoids
        for i in range(self.dim):
            f_val += 0.5 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
        
        # Add a challenging landscape with multiple peaks and valleys
        for i in range(self.dim):
            f_val += 0.3 * np.sin(15.0 * x[i])**2 * np.cos(5.0 * x[i])
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        return f_val
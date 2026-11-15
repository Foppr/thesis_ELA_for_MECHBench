import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_value = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified frequencies
        for i in range(self.dim):
            f_value += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[i])
            
        # Add a more challenging landscape with multiple peaks and stronger interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.08 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - 3 * x[j])
        
        # Add a cubic term to increase nonlinearity
        for i in range(self.dim):
            f_value += 0.03 * x[i]**3
        
        return f_value
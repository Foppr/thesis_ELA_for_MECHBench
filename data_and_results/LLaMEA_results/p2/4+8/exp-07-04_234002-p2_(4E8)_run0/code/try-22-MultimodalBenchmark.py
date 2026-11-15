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
            f_value += 0.2 * np.sin(8 * x[i]) * np.cos(5 * x[i]) + 0.1 * np.sin(3 * x[i])**2
        
        # Add a more challenging landscape with multiple peaks and stronger interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.12 * np.sin(4 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 4 * x[j]) + 0.05 * np.sin(2 * x[i] * x[j])
        
        # Add higher-order polynomial terms to increase nonlinearity and create more complex landscape
        for i in range(self.dim):
            f_value += 0.05 * x[i]**4 + 0.02 * x[i]**3
        
        # Add cross-dimensional interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.03 * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(5 * x[i] + 4 * x[j])
        
        return f_value
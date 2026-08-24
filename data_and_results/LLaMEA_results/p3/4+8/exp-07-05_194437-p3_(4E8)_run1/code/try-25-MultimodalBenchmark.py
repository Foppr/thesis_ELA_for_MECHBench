import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add exponential conditioning term
        for i in range(self.dim):
            result += (i + 1) * np.exp(0.1 * x[i]**2)
        
        # Add nested saddle points with varying scales
        for i in range(self.dim):
            result += 10 * np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(0.5 * x[i])
        
        # Add interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                result += 5 * np.exp(-0.1 * distance**2) * np.sin(x[i]) * np.cos(x[j])
        
        # Add a global shaping term with polynomial growth
        result += 0.05 * np.sum(x**4)
        
        # Add periodic modulation with adaptive frequency
        for i in range(self.dim):
            freq = 1 + 0.5 * np.sin(i)
            result += 3 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        return result
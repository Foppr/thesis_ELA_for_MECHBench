import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly oscillatory sinusoidal components with exponential frequency growth
        for i in range(self.dim):
            freq_factor = 2 ** (i % 4 + 1)
            result += 0.5 * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.5)
            
        # Add complex polynomial barriers with varying exponents
        for i in range(self.dim):
            result += 0.1 * (x[i] - 1)**(2 + i % 3) + 0.05 * (x[i] + 2)**(3 + i % 4)
            
        # Add a global minimum with intricate structure
        for i in range(self.dim):
            result += 0.02 * np.exp(-0.5 * ((x[i] - 1.5) / 0.5)**2) * np.sin(10 * x[i])
            
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.01 * x[i] * x[j] * np.sin(x[i] + x[j])
                
        return result
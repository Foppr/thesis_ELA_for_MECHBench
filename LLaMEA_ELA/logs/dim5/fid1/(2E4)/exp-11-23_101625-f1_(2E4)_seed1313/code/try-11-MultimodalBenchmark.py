import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # High-frequency cosine terms with exponential growth
        for i in range(self.dim):
            freq = 2 ** (i + 1)
            result += 0.2 * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Complex interaction terms with varying coefficients
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                coeff = 0.1 / (1 + abs(i - j))
                result += coeff * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Multi-modal global structure with multiple valleys
        for i in range(self.dim):
            result += 0.15 * (np.cos(5 * x[i]) + 0.5 * np.sin(8 * x[i])) * np.exp(-0.2 * (x[i] - 2)**2)
            
        # Add a complex penalty term for being far from the global minimum
        result += 0.05 * np.sum((x - 1.5)**4)
        
        return result
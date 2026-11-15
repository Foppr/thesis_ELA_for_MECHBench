import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly chaotic trigonometric terms with exponential frequency growth
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add complex interaction terms with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for computational efficiency
                scale = 2 ** (i + j)
                result += scale * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add polynomial chaos with high-order terms
        for i in range(self.dim):
            result += 0.05 * (x[i]**6 + x[i]**5 + x[i]**4) * np.sin(3 * x[i])
            
        # Add a global minimum with strong penalty for deviation from origin
        result += 0.01 * np.sum(np.abs(x)**3) + 0.005 * np.sum(x**6)
        
        # Add a complex oscillatory component that varies dramatically with dimension
        result += 0.2 * np.sin(np.sum(x**2)) * np.cos(np.sum(x**3))
        
        return result
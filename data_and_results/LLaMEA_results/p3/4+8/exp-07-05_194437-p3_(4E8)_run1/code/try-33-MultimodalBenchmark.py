import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add quadratic term for conditioning
        result += 0.3 * np.sum(x**2)
        
        # Add periodic terms with varying frequencies and increased complexity
        for i in range(self.dim):
            result += 5 * np.sin(3.0 * np.pi * x[i] / (1 + 0.2 * i)) * np.cos(4.0 * np.pi * x[i] / (1 + 0.3 * i)) * np.sin(2.0 * np.pi * x[i] / (1 + 0.1 * i))
        
        # Add a more complex interaction term with stronger coupling and longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased cross-interaction range
                result += 2.5 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.03 * (x[i] - x[j])**2) * np.sin(0.5 * (x[i] + x[j]))
        
        # Add a global shaping term with higher-order polynomial
        result += 0.03 * np.sum(np.abs(x)**4.0)
        
        # Add a noise-like component with higher frequency and amplitude
        for i in range(self.dim):
            result += 0.8 * np.sin(15 * x[i]) * np.cos(8 * x[i]) * np.sin(4 * x[i])
        
        # Add a chaotic interaction term to increase complexity
        for i in range(self.dim):
            if i > 0:
                result += 1.2 * np.sin(x[i]) * np.cos(x[i-1]) * np.exp(-0.01 * (x[i] - x[i-1])**2) * np.sin(10 * x[i])
        
        return result
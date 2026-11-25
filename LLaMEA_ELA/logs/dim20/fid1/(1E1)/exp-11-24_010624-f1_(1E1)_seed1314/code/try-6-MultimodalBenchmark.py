import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add highly oscillatory sinusoidal terms with exponential decay
        for i in range(self.dim):
            frequency = 10.0 * (1.0 + 0.5 * np.sin(i))
            amplitude = 0.5 * np.exp(-0.2 * i)
            result += amplitude * np.sin(frequency * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Add complex interaction terms with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension interaction
                strength = 0.3 * np.exp(-0.1 * (i + j))
                result += strength * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Add a high-frequency noise component
        for i in range(self.dim):
            result += 0.05 * np.sin(20 * x[i]) * np.cos(15 * x[i])
            
        # Add cubic terms for increased complexity
        for i in range(self.dim):
            result += 0.02 * x[i]**3 * np.sin(5 * x[i])
            
        return result
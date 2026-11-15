import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add hyperbolic tangent modulation terms
        for i in range(self.dim):
            xi = x[i]
            result += np.tanh(0.5 * xi) * np.sin(2 * xi) + 0.3 * np.tanh(0.3 * xi) * np.cos(3 * xi)
        
        # Add polynomial coupling terms with dynamic frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic frequency based on variable values
                freq = 1.0 + 0.5 * np.sin(x[i] * x[j])
                result += 0.2 * np.sin(freq * x[i] * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.02 * np.random.random())
        
        return result
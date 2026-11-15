import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute the multimodal function with sinusoidal grid pattern
        # This creates multiple local minima in a structured grid
        result = 0.0
        
        # Base quadratic term
        result += np.sum(x**2)
        
        # Add sinusoidal modulation to create multiple local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            
        # Add grid-based sinusoidal pattern for additional complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(0.2 * x[i]) * np.sin(0.4 * x[j])
                
        # Add a global minimum at the origin with additional penalty terms
        result += 0.01 * np.sum(np.abs(x))
        
        return result
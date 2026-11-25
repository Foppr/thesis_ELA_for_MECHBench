import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Main quadratic term (global minimum at origin)
        result += np.sum(x**2)
        
        # Add multiple global minima in radial pattern
        distances = np.sqrt(np.sum(x**2))
        result += 2.0 * np.sin(3.0 * distances) * np.cos(2.0 * distances)
        
        # Add chaotic interactions using sine waves with different frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
            
        # Add cross-dimension interactions with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                result += 0.3 * np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
                
        # Add a saddle-point basin around the origin to create complex terrain
        saddle_term = 0.1 * np.sum(x**4) - 0.2 * np.sum(x**2)
        result += saddle_term
        
        # Add a highly oscillatory component to increase complexity
        result += 0.8 * np.sum(np.sin(15 * x) * np.cos(10 * x))
        
        return result
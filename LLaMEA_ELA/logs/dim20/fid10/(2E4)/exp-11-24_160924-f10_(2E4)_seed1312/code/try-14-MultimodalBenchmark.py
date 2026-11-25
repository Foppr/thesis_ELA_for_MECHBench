import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add highly oscillatory component with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Create complex multimodal structure using multiple sine waves
            result += (xi**2 - 10 * np.cos(2 * np.pi * xi) + 5 * np.cos(4 * np.pi * xi))**2
            
        # Add non-separable cross-terms to increase difficulty
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce coupling between dimensions
                result += 0.5 * np.sin(3 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
                
        # Add a global attractive force towards the origin with additional noise
        result += 0.1 * np.sum(x**4) + 0.05 * np.sum(np.sin(10 * x))
        
        return result
import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial terms with varying degrees
        for i in range(self.dim):
            result += 0.5 * x[i]**2 + 0.1 * x[i]**4 + 0.02 * x[i]**6
            
        # Trigonometric components with adaptive frequencies
        for i in range(self.dim):
            result += 1.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.8 * np.sin(5.0 * x[i])
            
        # Radial basis function components
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.5 * (x[i] - 1.0)**2) + 0.2 * np.exp(-0.5 * (x[i] + 2.0)**2)
            
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j]))
                
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * self.dim + 0.01 * np.sum(x**2)
        result = result * scale_factor
        
        # Add noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.03 * np.sin(15.0 * x[i])
        result = result + noise
        
        return result
import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with enhanced frequencies and cubic terms
        for i in range(self.dim):
            result += 1.0 * np.sin(1.5 * x[i]) * np.cos(0.9 * x[i]) + 0.2 * x[i]**3 + 0.05 * x[i]**4
            
        # Add interaction terms between dimensions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(2.0 * x[i]) * np.sin(1.2 * x[j]) + 0.02 * x[i]**2 * x[j]**2
                
        # Add a global scaling factor with higher-order polynomial terms
        result = result * (1.0 + 0.2 * np.sum(x**2) + 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6))
        
        # Add a small noise term to break symmetry and increase difficulty
        result += 0.01 * np.sum(np.sin(3.0 * x))
        
        return result
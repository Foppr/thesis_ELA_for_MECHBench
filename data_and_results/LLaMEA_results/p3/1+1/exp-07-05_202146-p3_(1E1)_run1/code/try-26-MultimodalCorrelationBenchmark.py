import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.1 * (i - j)**2)
                result += 0.5 * decay * (x[i] - x[j])**2
                
        # Add trigonometric interactions with varying frequencies
        for i in range(self.dim):
            result += 0.3 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.2 * np.sin(5 * x[i])
            
        # Add saddle point structure
        for i in range(self.dim):
            result += 0.1 * x[i]**3 - 0.05 * x[i]**4
            
        # Add multimodal component with multiple local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(4 * x[i]) * np.cos(6 * x[i])
            
        # Add cross-term interactions that create complex topology
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                result += 0.05 * (x[i] * x[j]) * np.sin(x[i] + x[j])
                
        # Add global scaling factor to control difficulty
        result *= (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result
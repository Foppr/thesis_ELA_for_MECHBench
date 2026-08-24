import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying correlation terms
        for i in range(self.dim):
            decay = np.exp(-0.1 * i)
            result += decay * x[i]**4
        
        # Add multimodal components with different scales
        for i in range(self.dim):
            # Create multiple local minima using sine and cosine
            result += 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            result += 0.3 * np.sin(5 * x[i]) * np.cos(4 * x[i])
            
        # Add interaction terms with exponentially decaying weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.05 * (i + j))
                interaction = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                result += weight * interaction
                
        # Add saddle-point structure
        sum_x_squared = np.sum(x**2)
        result += 0.1 * sum_x_squared * np.sin(0.5 * sum_x_squared)
        
        # Add high-frequency oscillations
        for i in range(self.dim):
            result += 0.05 * np.sin(10 * x[i]) * np.cos(8 * x[i])
            
        # Add global structure enforcing term
        result += 0.01 * np.sum(np.abs(x)**3)
        
        return result
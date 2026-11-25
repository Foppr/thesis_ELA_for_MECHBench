import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add sinusoidal oscillations to create multimodal landscape
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        return result
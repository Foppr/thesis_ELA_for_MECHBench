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
            result += 0.15 * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Add interaction terms between dimensions with modified coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
                
        # Add cubic nonlinear terms to increase complexity
        for i in range(self.dim):
            result += 0.03 * x[i]**3
            
        return result
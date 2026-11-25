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
            result += 0.2 * np.sin(8 * x[i]) * np.cos(5 * x[i])
            
        # Add interaction terms between dimensions with modified coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.12 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - 3 * x[j])
                
        # Add cubic nonlinear terms to increase complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**3
            
        # Add Gaussian perturbations to increase landscape complexity
        for i in range(self.dim):
            result += 0.08 * np.exp(-0.5 * ((x[i] - 2.0) / 1.5)**2) + 0.08 * np.exp(-0.5 * ((x[i] + 2.0) / 1.5)**2)
            
        # Add higher-order polynomial interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * (x[i]**2) * (x[j]**2)
                
        return result
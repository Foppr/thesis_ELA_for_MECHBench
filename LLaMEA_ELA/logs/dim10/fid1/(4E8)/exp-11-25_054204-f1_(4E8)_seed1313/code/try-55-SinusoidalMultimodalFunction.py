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
            result += 0.3 * np.sin(8 * x[i]) * np.cos(6 * x[i])
            
        # Add interaction terms between dimensions with higher complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1 + 0.3 * np.abs(x[i]) * np.abs(x[j]))
                
        # Add polynomial interaction terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.08 * x[i]**4
            
        # Add cross-dimensional polynomial terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**2) * (x[j]**3)
                
        # Add Gaussian perturbations to increase landscape complexity
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) + 0.05 * np.exp(-0.5 * ((x[i] + 2.0) / 0.3)**2)
            
        # Add higher-order cross-dimensional terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.01 * x[i] * x[j] * x[k]
                    
        return result
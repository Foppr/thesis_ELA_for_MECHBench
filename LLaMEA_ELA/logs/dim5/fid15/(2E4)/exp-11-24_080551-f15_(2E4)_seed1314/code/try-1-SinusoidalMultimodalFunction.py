import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute the multimodal function with sinusoidal components
        # This creates multiple local minima and a complex landscape
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term
            result += (x[i] - 1.0)**2
            
            # Sinusoidal perturbations creating multiple local minima
            result += 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
            # Additional sinusoidal term for more complexity
            result += 0.3 * np.sin(5.0 * x[i])**2
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        return result
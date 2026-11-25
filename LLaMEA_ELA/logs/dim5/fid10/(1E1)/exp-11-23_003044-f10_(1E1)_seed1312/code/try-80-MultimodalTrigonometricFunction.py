import numpy as np

class MultimodalTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Base polynomial term with sinusoidal modulation
        result = np.sum(x**4) * (1 + 0.2 * np.sin(5 * np.sum(x)))
        
        # Add multiple sinusoidal components with different frequencies
        for i in range(self.dim):
            result += 3 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Add a global modulation term that depends on all variables
        result *= (1 + 0.3 * np.sum(np.sin(x_norm)))
        
        # Add a conditioning factor to increase problem difficulty
        condition_factor = 1 + 0.1 * np.sum(np.abs(x_norm)**2)
        result = result * condition_factor
        
        return result
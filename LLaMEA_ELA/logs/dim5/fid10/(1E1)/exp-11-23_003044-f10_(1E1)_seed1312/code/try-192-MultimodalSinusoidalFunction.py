import numpy as np

class MultimodalSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Create a multimodal landscape with sinusoidal components
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with sinusoidal modulation
            result += (x[i] ** 2) * (1 + 0.1 * np.sin(10 * x[i]))
            
            # Add sinusoidal modulation that creates multiple local minima
            result += 2 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
            # Add interaction terms between dimensions with varying coefficients
            for j in range(i+1, self.dim):
                # More complex interaction term
                result += 0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (1 + 0.05 * np.sin(5 * x[i]))
                
        # Add a global scaling factor and ensure proper conditioning
        result = result * (1 + 0.1 * np.sum(np.abs(x_norm)) + 0.05 * np.sum(x_norm**2))
        
        # Add a small constant to ensure the function is always positive for better conditioning
        result += 0.1
        
        return result
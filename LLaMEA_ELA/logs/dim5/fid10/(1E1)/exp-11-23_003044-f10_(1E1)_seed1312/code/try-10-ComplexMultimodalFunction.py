import numpy as np

class ComplexMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Base quadratic term with variable conditioning
        result = np.sum(x**2 * (1 + 0.1 * np.sin(5 * x)))
        
        # Add multiple sinusoidal components creating complex interactions
        for i in range(self.dim):
            result += 3 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            result += 2 * np.sin(4 * x[i]) * np.sin(2 * x[i])
            
        # Add interaction terms between dimensions creating non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.3 * np.sin(x[i] + x[j])**2
        
        # Add a global scaling factor based on the norm of the input
        norm = np.linalg.norm(x_norm)
        result *= (1 + 0.5 * norm**2)
        
        # Add a small noise term to make the function less predictable
        result += 0.01 * np.sum(np.sin(10 * x))
        
        return result
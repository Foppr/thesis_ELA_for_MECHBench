import numpy as np

class ChaoticLogisticFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        self.r = 3.9  # Logistic map parameter for chaos
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Initialize chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        for i in range(self.dim):
            # Use a simple logistic map to generate chaotic behavior
            if i == 0:
                chaotic_seq[i] = 0.5  # Initial value
            else:
                chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1])
        
        # Apply chaotic modulation to the input variables
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with chaotic modulation
            result += (x[i] ** 2) * (1 + 0.5 * chaotic_seq[i])
            
            # Add sine-based interaction terms that create multiple local minima
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add a global scaling factor based on the norm of the input
        norm = np.linalg.norm(x_norm)
        result = result * (1 + 0.2 * norm**2)
        
        return result
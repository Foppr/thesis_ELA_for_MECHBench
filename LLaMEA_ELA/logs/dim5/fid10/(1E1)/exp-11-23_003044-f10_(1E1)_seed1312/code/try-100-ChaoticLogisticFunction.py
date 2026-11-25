import numpy as np

class ChaoticLogisticFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Initialize chaotic sequence with logistic map
        result = 0.0
        r = 3.9  # Chaos parameter
        
        # Create a chaotic landscape using logistic map iterations
        for i in range(self.dim):
            # Base quadratic term
            result += x[i]**2
            
            # Add chaotic modulation using logistic map
            logistic_val = 0.5
            for _ in range(10):  # Iterate to reach chaotic regime
                logistic_val = r * logistic_val * (1 - logistic_val)
            
            # Use the chaotic value to modulate the function
            result += 2 * np.sin(logistic_val * x[i]) * np.cos(x[i]**2)
            
            # Add interaction terms between dimensions with chaotic coupling
            for j in range(i+1, self.dim):
                # Use a chaotic coupling parameter
                coupling = np.sin(logistic_val + np.cos(x[j]))
                result += 0.3 * np.sin(x[i] * x[j]) * coupling
                
        # Add a global scaling factor and ensure proper conditioning
        result = result * (1 + 0.05 * np.sum(np.abs(x_norm)) + 0.1 * np.sum(x_norm**2))
        
        return result
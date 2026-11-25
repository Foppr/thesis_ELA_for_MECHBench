import numpy as np

class ChaoticTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        for i in range(self.dim):
            # Base chaotic component with nested trigonometric functions
            term1 = np.sin(np.pi * x[i])
            term2 = np.cos(2 * np.pi * x[i])
            term3 = np.sin(3 * np.pi * x[i])
            
            # Create chaotic behavior through composition
            chaotic_component = term1 * term2 + term3 * np.sin(0.5 * np.pi * x[i])
            
            # Add interaction terms between dimensions
            interaction = 0.0
            for j in range(i+1, min(i+4, self.dim)):  # Limit interactions to avoid excessive complexity
                interaction += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
            
            # Combine components with varying weights
            result += (x[i]**2) * (1 + 0.5 * chaotic_component) + 0.3 * interaction
            
        # Add global scaling and noise-like perturbation
        result = result * (1 + 0.1 * np.sum(np.abs(x)) / self.dim)
        
        return result
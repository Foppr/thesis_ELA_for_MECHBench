import numpy as np

class ChaoticBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add chaotic sinusoidal components
        for i in range(self.dim):
            # Use a chaotic map component for each dimension
            xi = x[i]
            # Sinusoidal terms with different frequencies and amplitudes
            result += (np.sin(xi) * np.cos(2 * xi) + 
                      0.5 * np.sin(3 * xi) * np.cos(xi) +
                      0.3 * np.sin(5 * xi))
        
        # Add polynomial barrier terms to create multiple local minima
        for i in range(self.dim):
            xi = x[i]
            # Higher order polynomial barriers
            result += 0.1 * (xi**4 - 2*xi**2 + 1)  # Creates multiple wells
            
        # Add cross-term interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction terms that create complex landscape
                result += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.01 * np.sum(np.random.rand(self.dim) - 0.5))
        
        return result
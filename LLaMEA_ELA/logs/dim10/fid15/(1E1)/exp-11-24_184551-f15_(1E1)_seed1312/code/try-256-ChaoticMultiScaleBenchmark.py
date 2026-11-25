import numpy as np

class ChaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add chaotic sinusoidal components with different frequencies
        for i in range(self.dim):
            # Use each dimension in a unique way to create complexity
            xi = x[i]
            # High-frequency chaotic component
            result += np.sin(10 * xi) * np.cos(5 * xi) + 0.5 * np.sin(20 * xi)
            
        # Add polynomial penalty terms for large values
        poly_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_penalty += 0.1 * xi**4 + 0.05 * xi**6
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) * 0.3
                
        # Add a global scaling factor and noise
        result = result * 2.0 + poly_penalty - interaction + np.random.normal(0, 0.01)
        
        return result
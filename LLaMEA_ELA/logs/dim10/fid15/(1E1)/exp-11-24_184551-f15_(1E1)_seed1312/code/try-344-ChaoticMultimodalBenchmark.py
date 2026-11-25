import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add radial quadratic basin term
        radius = np.sqrt(np.sum(x**2))
        result += 0.1 * radius**2
        
        # Add chaotic sinusoidal terms with different frequencies
        for i in range(self.dim):
            # Use different frequencies for each dimension
            freq = 2**(i+1)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-term with varying strength
                cross_term = (x[i] * x[j])**2 * np.sin(x[i] + x[j])
                result += 0.05 * cross_term
                
        # Add a global minimum at the origin with noise
        result += 0.01 * np.sum(np.sin(x)**2)
        
        return result
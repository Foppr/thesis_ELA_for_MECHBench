import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add polynomial potential terms
        for i in range(self.dim):
            result += x[i]**4 - 2*x[i]**2
            
        # Add sinusoidal chaotic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create interaction between dimensions
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.5 * interaction
                
        # Add chaotic behavior with exponential decay
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.exp(-abs(x[i])) * np.sin(10 * x[i])
            
        result += 0.3 * chaotic_sum
        
        # Add a global scaling factor
        result *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        return result
import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Chaotic component using sine and cosine functions
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i])
        
        # Polynomial basin component
        polynomial_term = np.sum(x**4) - 2 * np.sum(x**2)
        
        # Add coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim-1):
            coupling_term += (x[i] - x[i+1])**2 * np.sin(x[i] + x[i+1])
        
        # Add noise to increase complexity
        noise = 0.05 * np.random.rand()
        
        return chaotic_term + polynomial_term + coupling_term + noise
import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sinusoidal base with multiple frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(4 * np.pi * x_norm))
        
        # Polynomial penalty terms to create complex landscape
        poly_term = np.sum(x_norm**4 + 0.3 * x_norm**3 - 0.1 * x_norm**2)
        
        # Add coupling between dimensions to create correlation challenges
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**2
        
        # Add a chaotic component using a simple map
        chaotic = 0.0
        if self.dim >= 2:
            # Simple chaotic dynamics in first two dimensions
            x1, x2 = x_norm[0], x_norm[1]
            chaotic = 0.5 * (x1**2 + x2**2) * np.sin(10 * np.pi * (x1 + x2))
        
        return sin_term + poly_term + 0.1 * coupling + chaotic
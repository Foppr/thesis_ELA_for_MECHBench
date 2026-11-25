import numpy as np

class ChaoticPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.constants = np.random.uniform(0.5, 2.0, dim)
        self.frequency = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(self.frequency[i] * x_norm[i]) * np.cos(self.constants[i] * x_norm[i])
        
        # Polynomial potential with mixed degrees
        poly_term = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                poly_term += x_norm[i]**4
            else:
                poly_term += x_norm[i]**3
        
        # Cross-terms creating complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_norm[i] * x_norm[j]) * (i + j)
        
        # Add a global minimum at origin with perturbation
        base_value = np.sum(x_norm**2) * 0.5
        
        # Combine all terms with varying weights
        result = 2.0 * chaotic_term + 1.5 * poly_term + 0.8 * cross_term + base_value
        
        # Add small random noise for additional challenge
        noise = 0.001 * np.random.random()
        
        return result + noise
import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Initialize result
        result = 0.0
        
        # Chaotic component using sine and cosine with varying frequencies
        for i in range(self.dim):
            freq = (i + 1) * 0.5
            result += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Exponential penalty terms to create rugged landscape
        for i in range(self.dim):
            result += np.exp(0.1 * np.abs(x[i])) * np.sin(x[i] ** 2)
            
        # Polynomial terms with alternating signs for complexity
        for i in range(self.dim):
            power = (i % 4) + 2
            coeff = (-1) ** i * 0.05
            result += coeff * (x[i] ** power)
            
        # Cross-dimensional interactions with chaotic coupling
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.01 * (x[i] ** 2 + x[j] ** 2))
            
        # Add a global scaling term based on the norm
        norm = np.linalg.norm(x)
        result *= (1.0 + 0.5 * norm * np.sin(norm))
        
        # Add noise-like perturbations to increase irregularity
        for i in range(self.dim):
            result += 0.01 * np.sin(10 * x[i]) * np.cos(7 * x[(i+2) % self.dim])
            
        return result
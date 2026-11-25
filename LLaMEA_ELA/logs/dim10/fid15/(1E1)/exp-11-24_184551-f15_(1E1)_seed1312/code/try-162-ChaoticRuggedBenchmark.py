import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal base landscape with varying frequencies
        result = 0.0
        for i in range(self.dim):
            # High frequency sinusoidal terms
            result += np.sin(10 * x[i]) * np.cos(7 * x[i])
            # Medium frequency terms
            result += 0.5 * np.sin(3 * x[i]**2) * np.cos(2 * x[i])
            
        # Add polynomial penalty terms to create ruggedness
        poly_penalty = 0.0
        for i in range(self.dim):
            poly_penalty += (x[i] ** 4) / 100.0 + (x[i] ** 3) / 10.0 + (x[i] ** 2) / 2.0
            
        # Add chaotic behavior with cross-terms
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add noise to make it non-trivial
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + poly_penalty + chaotic_term + noise
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Asymmetric hyperbolic sine interaction terms
        sinh_interaction = 0.0
        for i in range(self.dim):
            sinh_interaction += np.sinh(1.5 * x[i]) ** 2
        
        # Exponentially decaying correlation structure
        decay_corr = 0.0
        for i in range(self.dim - 1):
            decay_corr += np.exp(-0.1 * (i + 1)) * (x[i] - x[i+1])**2
        
        # Chaotic saddle-point component with multiple unstable fixed points
        chaotic_saddle = 0.0
        for i in range(self.dim):
            chaotic_saddle += np.sin(23 * x[i]) * np.cos(29 * x[i]) * np.tanh(x[i])
        
        # Asymmetric cubic interaction terms
        asym_cubic = 0.0
        for i in range(self.dim - 1):
            asym_cubic += (x[i] ** 3) * (x[i+1] ** 2)
        
        # Rugged terrain with multiple local minima using high-frequency cosine
        rugged = 0.0
        for i in range(self.dim):
            rugged += np.cos(50 * x[i]) ** 2
        
        # Combine all terms to create a complex landscape
        return quadratic + 0.25 * sinh_interaction + 0.15 * decay_corr + 0.2 * chaotic_saddle + 0.1 * asym_cubic + 0.3 * rugged
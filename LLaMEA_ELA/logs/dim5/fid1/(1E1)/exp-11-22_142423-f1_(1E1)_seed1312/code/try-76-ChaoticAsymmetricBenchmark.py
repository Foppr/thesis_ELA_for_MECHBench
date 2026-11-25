import numpy as np

class ChaoticAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric conditioning
        f = np.sum((x ** 2) * (1 + 0.1 * np.abs(x)))
        
        # Add periodic sinusoidal components with varying frequencies and phases
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[(i + 1) % self.dim])
            
        # Introduce non-separable cross-dimensional interactions with chaotic modulation
        for i in range(self.dim):
            f += 0.3 * np.sin(x[i] + x[(i + 2) % self.dim]) * np.cos(0.5 * x[(i + 3) % self.dim])
            
        # Add asymmetric penalty terms
        f += 0.2 * np.sum(np.abs(x)**1.5) + 0.1 * np.sum(x**4)
        
        # Include higher-order interaction terms with exponential scaling
        for i in range(self.dim):
            f += 0.15 * (x[i]**3) * np.exp(-0.1 * x[(i + 1) % self.dim])
            
        # Add chaotic phase-shifted sinusoidal interactions
        for i in range(self.dim):
            f += 0.2 * np.sin(4 * x[i] + 0.5 * x[(i + 2) % self.dim]) * np.cos(2 * x[(i + 3) % self.dim])
            
        # Introduce irregular local minima through non-uniform modulation
        for i in range(self.dim):
            f += 0.1 * np.sin(6 * x[i]) * np.cos(4 * x[(i + 1) % self.dim] - 1.5)
            
        return f
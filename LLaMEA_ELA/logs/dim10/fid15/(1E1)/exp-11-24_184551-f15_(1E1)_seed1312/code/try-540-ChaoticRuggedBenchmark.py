import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal wave components with varying frequencies
        wave1 = np.sum(np.sin(2 * np.pi * x) ** 2)
        wave2 = np.sum(np.cos(3 * np.pi * x) ** 2)
        
        # Polynomial penalty terms to create ruggedness
        poly1 = np.sum(x**4 * 0.1)
        poly2 = np.sum(np.abs(x)**3 * 0.05)
        
        # Chaotic component using sine of exponential
        chaotic = np.sum(np.sin(np.exp(np.abs(x))) * 0.2)
        
        # Cross-term interactions to increase complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1 + np.abs(x[i] - x[j]))
        
        # Combine all components with different weights
        return wave1 + wave2 + poly1 + poly2 + chaotic + cross_term * 0.1
import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal oscillation terms
        oscillation = np.sum(np.sin(5.0 * x), axis=1)
        
        # Exponential barrier terms
        barriers = np.sum(np.exp(2.0 * np.abs(x)), axis=1)
        
        # Chaotic mixing term using logistic map-like behavior
        chaotic = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x), axis=1)
        
        # Combine all terms with varying weights
        result = 0.5 * oscillation + 0.3 * barriers + 0.2 * chaotic
        
        # Add a quadratic basin term to ensure global optimum is bounded
        basin = 0.1 * np.sum(x**2, axis=1)
        
        return result + basin
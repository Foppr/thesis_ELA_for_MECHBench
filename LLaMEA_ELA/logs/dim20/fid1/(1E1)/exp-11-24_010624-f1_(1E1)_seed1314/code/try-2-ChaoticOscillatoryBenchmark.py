import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic exponential barrier terms
        for i in range(self.dim):
            # Exponential barrier near boundaries
            barrier = np.exp(-10 * (x[i] - 5)**2) + np.exp(-10 * (x[i] + 5)**2)
            result += barrier
            
        # Add periodic oscillatory components with varying frequencies
        for i in range(self.dim):
            # Multiple sine waves with different frequencies and amplitudes
            freqs = [1.0, 2.0, 3.0, 5.0]
            for freq in freqs:
                result += 0.5 * np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
                
        # Add coupling terms between dimensions with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                result += 0.3 * coupling
                
        # Add a global scaling factor to control the difficulty
        result *= (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result
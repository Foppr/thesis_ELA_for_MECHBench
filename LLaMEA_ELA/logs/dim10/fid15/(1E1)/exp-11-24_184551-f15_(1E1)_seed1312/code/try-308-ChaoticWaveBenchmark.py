import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add chaotic sinusoidal components
        for i in range(self.dim):
            # Use different frequencies and phases for each dimension
            freq = 2 * np.pi * (i + 1) / self.dim
            phase = np.pi * i / self.dim
            
            # Sinusoidal term with varying amplitude
            amplitude = 1.0 + 0.5 * np.sin(i)
            result += amplitude * np.sin(freq * x[i] + phase)
            
            # Add quadratic barrier terms to create local minima
            barrier_term = 0.1 * (x[i] - np.sin(x[i]))**2
            result += barrier_term
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * 0.5
                result += interaction
                
        # Add a global scaling factor and noise
        result *= 1.0 + 0.1 * np.random.rand()
        
        return result
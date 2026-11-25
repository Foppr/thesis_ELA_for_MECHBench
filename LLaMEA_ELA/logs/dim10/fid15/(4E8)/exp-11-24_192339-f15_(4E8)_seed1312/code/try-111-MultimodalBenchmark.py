import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sine-based chaotic component with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) / self.dim
            chaotic += np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
        
        # Saddle-point structure with hyperbolic tangent interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle += np.tanh(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Dimensionally adaptive penalty term
        penalty = 0
        for i in range(self.dim):
            penalty += (i + 1) * np.abs(x[i])**3
        
        # Oscillating radial component with exponential decay
        radial = 0
        for i in range(self.dim):
            radial += np.sin(np.pi * x[i] / 2.0) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interaction
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] + x[j])**4
        
        # Global scaling factor based on dimensionality
        scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components
        return scale * (0.5 * chaotic + 0.3 * saddle + 0.2 * coupling) + penalty + radial
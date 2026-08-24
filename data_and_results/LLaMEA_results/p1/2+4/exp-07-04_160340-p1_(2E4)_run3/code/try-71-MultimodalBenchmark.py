import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x_norm = x / 5.0
        
        # Chaotic component using sine map
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * x[i]) * np.cos(15 * np.pi * x[i])
        
        # Exponentially decaying harmonic terms
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 5)
            decay = np.exp(-0.1 * i)
            harmonic += decay * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive conditioning: varying condition numbers
        condition = np.array([2**(i % 3) for i in range(self.dim)])
        conditioned = np.sum(condition * x_norm**2)
        
        # Multi-scale oscillations with varying amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i)
            oscillation += scale * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Nested minima with exponential decay in depth
        nested = 0.0
        for i in range(1, 6):
            loc = np.array([i * 0.5] * self.dim)
            dist = np.sum((x - loc)**2)
            nested += np.exp(-dist / (2 * i**2)) / i
        
        # Combine all components
        result = conditioned + harmonic + oscillation + chaotic - nested
        
        return result
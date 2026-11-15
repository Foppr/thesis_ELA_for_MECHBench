import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal modulations with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            freq = 2 ** (i % 3)  # Varying frequencies
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
            
        # Exponentially decaying interaction terms
        decay_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.5 * (i + j))
                decay_interaction += decay * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                
        # Global modulation with a central attractor
        center_attractor = np.sum((x - 1.0)**2) * np.exp(-0.1 * np.sum(x**2))
        
        return quadratic + chaotic + decay_interaction + center_attractor
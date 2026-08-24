import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive scaling
        quadratic = np.sum(x_norm ** 2)
        
        # Periodic attractor components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = i * 3
            amp = 1.0 / (i * 0.5 + 1)
            periodic += amp * np.sin(freq * np.pi * x_norm) ** 2
        
        # Multi-scale interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i] ** 3) * (x_norm[j] ** 2) * np.cos(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric distortion with exponential scaling
        distortion = 0.0
        for i in range(self.dim):
            distortion += np.exp(2 * np.abs(x_norm[i])) * np.sin(np.pi * x_norm[i])
        
        # Add dimensionality-dependent noise
        noise = 0.01 * np.sum(np.random.random(self.dim) * (1 + np.abs(x_norm)))
        
        # Combine all components
        return quadratic + 2 * periodic + 0.5 * interaction + 0.3 * distortion + noise
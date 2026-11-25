import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic centers
        rbfs = 0
        for i in range(10):
            center = np.sin(i * np.pi / 5.0) * 0.8
            rbfs += np.exp(-20 * np.sum((x_norm - center)**2)) * np.sin(15 * i * x_norm[0])
        
        # Sinusoidal coupling across dimensions with adaptive frequency
        coupling = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * np.pi / self.dim)
            coupling += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 1) % self.dim])
        
        # Adaptive dimensional interaction with exponential weighting
        dim_interaction = 0
        for i in range(self.dim):
            weight = np.exp(-0.5 * i)
            dim_interaction += weight * (x_norm[i]**3) * np.sin(7 * x_norm[i])
        
        # Chaotic modulation with cross-dimensional interference
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x_norm[i] + np.cos(5 * x_norm[(i + 2) % self.dim])) * np.cos(8 * x_norm[i])
        
        # Multi-scale sinusoidal structure with frequency modulation
        multiscale = 0
        for scale in [1, 3, 7]:
            multiscale += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm**2))
        
        # Global minimum shift and non-linear transformation
        shift = 0.3
        shifted = x_norm - shift
        penalty = 0.2 * np.sum(shifted**4)
        
        result = rbfs + coupling + dim_interaction + chaotic + multiscale + penalty
        
        return result
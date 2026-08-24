import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Chaotic component with dynamic frequencies
        chaotic = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * 0.5) + 3 * np.cos(i * 0.3)
            chaotic += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Nested saddle points with radial symmetry
        saddle = 0.0
        for i in range(self.dim):
            saddle += 0.5 * (x_norm[i]**4 - 2 * x_norm[i]**2) * np.cos(5 * np.pi * x_norm[i])
        
        # Dynamic penalty with varying intensity
        penalty = 0.0
        for i in range(self.dim):
            intensity = 2.0 + 1.5 * np.sin(i * 0.7)
            penalty += intensity * (x_norm[i]**6 - 3 * x_norm[i]**4 + 3 * x_norm[i]**2 - 1)
        
        # Cross-dimensional interaction with variable coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.5 * np.sin(i * 0.3 + j * 0.4)
                interaction += coupling * np.sin(15 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(10 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Radial basis with multiple peaks
        radial = 0.0
        for i in range(self.dim):
            radial += 0.3 * np.exp(-2.0 * x_norm[i]**2) * np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])
        
        # Multi-scale oscillation with adaptive amplitude
        multiscale = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.2)
            multiscale += amp * np.sin(25 * np.pi * x_norm[i]) * np.cos(20 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Central attraction with repulsion zones
        center_attraction = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        center_attraction = 2.0 * np.exp(-0.5 * dist**2) * np.sin(10 * dist) * np.cos(5 * dist)
        
        # Return combined function value
        return quadratic + chaotic + saddle + penalty + interaction + radial + multiscale + center_attraction
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_weights = np.random.uniform(-1.0, 1.0, dim)
        self.attractors = np.random.uniform(-5.0, 5.0, (8, dim))
        self.attractor_strengths = np.random.uniform(0.5, 2.0, 8)
        self.periodic_freq = np.random.uniform(1.0, 4.0, dim)
        self.noise_level = 0.1
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with mixed terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += self.poly_weights[i] * (x_norm[i]**3 + 0.5 * x_norm[i]**5 + 0.1 * x_norm[i]**7)
        
        # Gradient-based attraction fields
        attraction = 0.0
        for i in range(8):
            dist = np.sum((x_norm - self.attractors[i])**2)
            attraction += self.attractor_strengths[i] / (1.0 + dist)
        
        # Periodic boundary interactions with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(self.periodic_freq[i] * x_norm[i]) * np.cos(self.periodic_freq[i] * x_norm[i] * 0.5)
        
        # Cross-dimensional coupling with exponential interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Noise modulation with chaotic component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+1) % self.dim]**2) * self.noise_level
        
        # Combined landscape with global minimum at origin
        return poly_chaos + attraction + periodic + coupling + noise
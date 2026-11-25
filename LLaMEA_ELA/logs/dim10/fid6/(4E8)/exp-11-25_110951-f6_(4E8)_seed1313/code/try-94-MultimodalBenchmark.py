import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine component with varying frequency
        chaotic_term = np.sum(np.sin(15 * x_norm) * np.cos(7 * x_norm))
        
        # Radial exponential decay with oscillating basin
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.3 * np.sin(4 * r) * np.cos(2 * r))
        
        # Cross-dimensional coupling creating saddle points
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] * x_norm[i+1]) * np.sin(2 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Dimensionally adaptive noise term to increase difficulty with dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
        
        # Variable curvature based on dimensionality
        curvature = 1.0 + 0.5 * (self.dim - 1) / self.dim
        
        # Combine all components with appropriate scaling and add global minimum at origin
        return curvature * (chaotic_term + radial_term + coupling + noise) + 0.1 * r**4
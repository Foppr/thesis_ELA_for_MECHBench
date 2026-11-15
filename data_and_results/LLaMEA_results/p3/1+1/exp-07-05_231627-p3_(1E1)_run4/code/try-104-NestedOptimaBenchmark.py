import numpy as np

class NestedOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial component with nested exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-5 * r) * (1 + 0.5 * np.sin(10 * r))
        
        # Angular component with multiple frequency harmonics
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = np.sum([np.sin((i+1) * angles) * np.cos((i+1) * angles) for i in range(1, min(5, self.dim))])
        else:
            angular = 0.0
        
        # Multi-scale periodic modulation
        modulated = np.sum([np.sin(2**i * np.pi * x_norm) * np.exp(-0.5 * (2**i * x_norm)**2) for i in range(1, 5)])
        
        # Nested peaks with varying scales and positions
        nested = 0.0
        for i in range(1, 6):
            scale = 1.0 / (2**i)
            offset = 0.2 * np.sin(i * np.pi / 3)
            nested += scale * np.exp(-0.5 * np.sum(((x_norm - offset) / (0.1 * scale))**2))
        
        # Cross-dimensional coupling with asymmetric interaction
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += (x_norm[i]**3 + x_norm[i+1]**3) * np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2)
        
        # Global scaling and combination
        result = 0.5 * radial + 0.3 * angular + 0.2 * modulated + 0.1 * nested + 0.05 * coupling
        
        # Add small random perturbation for robustness
        noise = 0.001 * np.random.rand()
        
        return result + noise
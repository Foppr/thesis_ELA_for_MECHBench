import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at the center
        self.global_min = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like scaling
        r = np.sqrt(np.sum(x**2))
        radial = r * (1 + 0.3 * np.sin(10 * r))
        
        # Multi-scale sinusoidal interference
        interference = 0
        for i in range(1, min(6, self.dim + 1)):
            interference += np.sin(i * x) * np.cos(i * x * 0.5) * np.exp(-0.1 * i)
        
        # Self-similar fractal structure with recursive scaling
        fractal = 0
        for i in range(1, 6):
            scale = 2**(-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x))
        
        # Cross-dimensional coupling with varying strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j]) / (1 + np.abs(x[i] - x[j]))
        
        # Exponential barrier near boundaries
        barrier = np.sum(np.exp(2 * (5 - np.abs(x))) * (np.abs(x) > 4.5))
        
        # Combine components with dimension-dependent weights
        return 0.3 * radial + 0.4 * interference + 0.2 * fractal + 0.05 * coupling + 0.05 * barrier
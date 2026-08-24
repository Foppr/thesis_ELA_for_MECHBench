import numpy as np

class FractalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        base = np.sum(x_norm**2)
        
        # Fractal-like component with recursive self-similarity
        fractal = 0.0
        for i in range(1, 6):
            scale = 2**i
            fractal += np.sum(np.sin(scale * np.pi * x_norm) * np.exp(-0.5 * scale * np.abs(x_norm)))
        
        # Exponential barrier terms creating rugged terrain
        barriers = 0.0
        for i in range(self.dim):
            barriers += np.exp(5 * np.abs(x_norm[i]) - 2.5) + np.exp(-5 * np.abs(x_norm[i]) + 2.5)
        
        # Multi-scale sinusoidal interference creating complex landscape
        interference = 0.0
        for i in range(1, 8):
            freq = i * 3
            interference += np.sum(np.sin(freq * x_norm) * np.cos(freq * x_norm**2) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with non-linear interactions
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += (x_norm[i]**3 + x_norm[i+1]**3) * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2)
        
        # Global scaling and combination
        result = 0.2 * base + 0.3 * fractal + 0.25 * barriers + 0.2 * interference + 0.05 * coupling
        
        # Add small random perturbation for robustness
        noise = 0.01 * np.random.rand()
        
        return result + noise
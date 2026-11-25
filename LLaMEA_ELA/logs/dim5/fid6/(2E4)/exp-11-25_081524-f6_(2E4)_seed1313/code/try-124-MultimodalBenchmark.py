import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute attractor positions for chaotic behavior
        np.random.seed(42)
        self.attractors = np.random.uniform(-5.0, 5.0, (10, dim))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic attractor-based component with varying basins
        chaotic = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.linalg.norm(x - self.attractors[j]) for j in range(10))
            chaotic += np.sin(min_dist * (i + 1)) * np.exp(-0.1 * min_dist)
        
        # Fractional Brownian motion-like scaling with Hurst parameter
        fbm = 0.0
        hurst = 0.3 + 0.4 * np.sin(self.dim * 0.1)
        for i in range(self.dim):
            fbm += (x[i] ** (2.0 + hurst)) * np.cos(0.5 * x[i])
        
        # Asymmetric hyperbolic tangent landscape with multi-scale modulation
        tanh_landscape = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            tanh_landscape += np.tanh(x[i] * scale) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional interaction with sine modulation and random weights
        cross_interaction = 0.0
        for i in range(self.dim-1):
            weight = 0.5 + 0.5 * np.sin(i * 0.3)
            cross_interaction += weight * np.sin(x[i] * x[i+1]) * np.cos(0.2 * (x[i] + x[i+1]))
        
        # Add a global polynomial with random coefficients for irregularity
        poly_irregular = 0.0
        for i in range(self.dim):
            coeff = np.random.uniform(-1.0, 1.0)
            poly_irregular += coeff * (x[i] ** (3 + i % 3))
        
        # Global scaling and noise injection
        scale_factor = 2.0 + 0.5 * np.cos(self.dim * 0.2)
        noise_term = 0.01 * np.random.rand()
        
        return (chaotic + fbm + tanh_landscape + cross_interaction + poly_irregular) * scale_factor + noise_term
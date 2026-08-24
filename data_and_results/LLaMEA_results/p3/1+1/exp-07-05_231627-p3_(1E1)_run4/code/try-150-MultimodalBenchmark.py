import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Exponential decay peaks with varying amplitudes and widths
        peaks = 0
        for i in range(20):
            center = np.random.uniform(-1, 1, self.dim)
            amplitude = np.random.uniform(0.5, 2.0)
            width = np.random.uniform(0.1, 0.5)
            peaks += amplitude * np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Trigonometric interference with adaptive frequencies
        interference = 0
        for i in range(15):
            freq = 2 * np.pi * (i + 1) * (1 + 0.5 * np.sin(i))
            interference += np.sin(freq * np.sum(x_norm)) * np.cos(freq * np.sum(x_norm**2))
        
        # Adaptive conditioning with dimension-dependent scaling
        conditioning = np.sum((x_norm**2) * (1 + 0.1 * np.abs(x_norm))**2)
        
        # Fractional polynomial with mixed powers to create irregular terrain
        fractional_poly = np.sum(np.abs(x_norm)**1.3 + 0.5 * np.abs(x_norm)**3.7)
        
        # Cross-dimensional coupling with non-linear interaction terms
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**3) * np.sin(x_norm[i+1]) + (x_norm[i+1]**2) * np.cos(x_norm[i])
        
        # Add noise with adaptive magnitude based on function value
        noise_magnitude = 0.01 * (1 + np.abs(np.sum(x_norm**4)))
        noise = noise_magnitude * np.random.uniform(-1, 1)
        
        # Combine all components with carefully balanced weights
        result = 0.4 * peaks + 0.3 * interference + 0.2 * conditioning + 0.1 * fractional_poly + 0.05 * coupling + noise
        
        return result
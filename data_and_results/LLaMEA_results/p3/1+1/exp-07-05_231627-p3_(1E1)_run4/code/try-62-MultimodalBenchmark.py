import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Exponentially decaying harmonic components with varying frequencies
        harmonics = np.sum(np.exp(-2 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm) * 
                          np.cos(8 * np.pi * x_norm) + 
                          np.exp(-1.5 * np.abs(x_norm)) * np.sin(15 * np.pi * x_norm**2) * 
                          np.cos(12 * np.pi * x_norm**2))
        
        # Localized attractive basins with varying depths and radii
        basin_energy = 0
        for i in range(20):
            center = np.random.uniform(-1, 1, self.dim)
            radius = 0.2 + 0.3 * np.random.random()
            depth = 0.5 + 0.8 * np.random.random()
            distance = np.sum((x_norm - center)**2)
            basin_energy += depth * np.exp(-distance / (2 * radius**2))
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**3 + x_norm[i+1]**3) * np.sin(5 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Rugged surface with controlled roughness through fractional Brownian motion approximation
        ruggedness = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.sin(20 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Multi-scale Gaussian peaks with varying amplitudes and positions
        peaks = 0
        for i in range(10):
            pos = np.random.uniform(-1, 1, self.dim)
            amp = 0.3 + 0.7 * np.random.random()
            peaks += amp * np.exp(-5 * np.sum((x_norm - pos)**2))
        
        # Combined energy landscape with nonlinear mixing
        result = 0.4 * harmonics + 0.3 * basin_energy + 0.2 * coupling + 0.1 * ruggedness + 0.05 * peaks
        
        # Add small random perturbation for robustness
        noise = 0.01 * np.random.random()
        
        return result + noise
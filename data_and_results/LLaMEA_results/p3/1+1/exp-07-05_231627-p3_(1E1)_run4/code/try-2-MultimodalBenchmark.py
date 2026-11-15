import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # High-dimensional chaotic component with exponential growth
        chaotic = np.sum(np.exp(10 * np.abs(x_norm)) * np.sin(10 * np.pi * x_norm)**2)
        
        # Polynomial chaos with multiple roots
        poly_chaos = np.sum((x_norm**3 - 3 * x_norm)**2)
        
        # Interfering sinusoidal waves with varying amplitudes
        wave_interference = np.sum(np.sin(20 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Gaussian-like peaks with random positioning
        peaks = 0
        for i in range(10):
            center = np.random.uniform(-1, 1, self.dim)
            peaks += np.exp(-5 * np.sum((x_norm - center)**2))
        
        # Fractional power component creating rugged terrain
        rugged = np.sum(np.abs(x_norm)**1.5)
        
        # Combine all components with varying weights and nonlinear interactions
        result = 0.3 * chaotic + 0.2 * poly_chaos + 0.2 * wave_interference + 0.15 * peaks + 0.15 * rugged
        
        # Add a dynamic noise term that depends on the solution's position
        dynamic_noise = 0.02 * np.random.random() * (1 + np.abs(np.sum(x_norm**3)))
        
        return result + dynamic_noise
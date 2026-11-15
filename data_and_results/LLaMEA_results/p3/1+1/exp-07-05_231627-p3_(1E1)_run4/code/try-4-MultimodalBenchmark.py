import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced chaotic component with sinusoidal modulation
        chaotic = np.sum(np.exp(5 * np.abs(x_norm)) * np.sin(15 * np.pi * x_norm)**2)
        
        # Polynomial chaos with multiple roots and higher degree terms
        poly_chaos = np.sum((x_norm**4 - 4 * x_norm**2)**2)
        
        # Interfering sinusoidal waves with varying frequencies and amplitudes
        wave_interference = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm))
        
        # Gaussian-like peaks with structured positioning to avoid randomness
        peaks = 0
        centers = np.linspace(-1, 1, 8)
        for i in range(8):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += np.exp(-3 * np.sum((x_norm - center)**2))
        
        # Fractional power component creating rugged terrain with controlled roughness
        rugged = np.sum(np.abs(x_norm)**1.3)
        
        # Additional harmonic component for increased complexity
        harmonic = np.sum(np.sin(30 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * np.sin(10 * np.pi * x_norm))
        
        # Combine all components with carefully tuned weights and nonlinear interactions
        result = 0.25 * chaotic + 0.2 * poly_chaos + 0.15 * wave_interference + 0.2 * peaks + 0.1 * rugged + 0.1 * harmonic
        
        # Add controlled noise term to improve robustness
        noise_factor = 0.01 * (1 + np.abs(np.sum(x_norm**4)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
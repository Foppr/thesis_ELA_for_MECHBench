import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multiple frequency interactions
        chaotic = np.sum(np.sin(18 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) * np.exp(6 * np.abs(x_norm)))
        
        # Polynomial chaos with multiple roots and higher degree terms
        poly_chaos = np.sum((x_norm**4 - 6 * x_norm**2 + 9)**2)
        
        # Interfering sinusoidal waves with varying amplitudes and phases
        wave_interference = np.sum(np.sin(28 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * np.exp(-3 * np.abs(x_norm)))
        
        # Gaussian-like peaks with structured positioning to avoid randomness
        peaks = 0
        centers = np.linspace(-1, 1, 10)
        for i in range(10):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += np.exp(-2.5 * np.sum((x_norm - center)**2))
        
        # Fractional power component creating rugged terrain with controlled roughness
        rugged = np.sum(np.abs(x_norm)**1.8)
        
        # Additional harmonic component for increased complexity
        harmonic = np.sum(np.sin(32 * np.pi * x_norm**2) * np.cos(24 * np.pi * x_norm**2))
        
        # Combine all components with varying weights and nonlinear interactions
        result = 0.22 * chaotic + 0.18 * poly_chaos + 0.16 * wave_interference + 0.18 * peaks + 0.14 * rugged + 0.12 * harmonic
        
        # Add controlled noise term
        noise_factor = 0.01 * (1 + np.abs(np.sum(x_norm**3)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
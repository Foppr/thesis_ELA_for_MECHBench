import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced chaotic component with modified frequency interactions
        chaotic = np.sum(np.sin(18 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * np.exp(6 * np.abs(x_norm)))
        
        # Modified polynomial chaos with different root structure
        poly_chaos = np.sum((x_norm**3 - 4 * x_norm**2 + 4)**2)
        
        # Adjusted wave interference with different amplitudes
        wave_interference = np.sum(np.sin(22 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * np.exp(-3 * np.abs(x_norm)))
        
        # Modified Gaussian peaks with different positioning
        peaks = 0
        centers = np.linspace(-1, 1, 6)
        for i in range(6):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += np.exp(-4 * np.sum((x_norm - center)**2))
        
        # Modified rugged terrain with different power
        rugged = np.sum(np.abs(x_norm)**2.1)
        
        # Additional harmonic component with altered frequency
        harmonic = np.sum(np.sin(28 * np.pi * x_norm**2) * np.cos(20 * np.pi * x_norm**2))
        
        # Combine all components with updated weights
        result = 0.3 * chaotic + 0.15 * poly_chaos + 0.2 * wave_interference + 0.1 * peaks + 0.15 * rugged + 0.1 * harmonic
        
        # Add controlled noise term
        noise_factor = 0.015 * (1 + np.abs(np.sum(x_norm**3)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
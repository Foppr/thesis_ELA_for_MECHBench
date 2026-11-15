import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multiple frequency interactions and cross-terms
        chaotic = np.sum(np.sin(30 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * np.exp(15 * np.abs(x_norm)) + 
                         np.sin(20 * np.pi * x_norm**2) * np.cos(15 * np.pi * x_norm**2) * np.exp(-8 * np.abs(x_norm)))
        
        # Higher degree polynomial chaos with multiple local minima
        poly_chaos = np.sum((x_norm**8 - 15 * x_norm**6 + 60 * x_norm**4 - 100 * x_norm**2)**2)
        
        # Interfering sinusoidal waves with varying amplitudes, phases, and spatial frequency
        wave_interference = np.sum(np.sin(40 * np.pi * x_norm) * np.cos(30 * np.pi * x_norm) * 
                                  np.exp(-5 * np.abs(x_norm)) + 
                                  np.sin(35 * np.pi * x_norm**3) * np.cos(25 * np.pi * x_norm**3) * 
                                  np.exp(-4 * np.abs(x_norm)))
        
        # Structured Gaussian-like peaks with irregular spacing and varying heights
        peaks = 0
        centers = np.linspace(-1, 1, 20)
        for i in range(20):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += 2.5 * np.exp(-6 * np.sum((x_norm - center)**2)) + 0.8 * np.exp(-4 * np.sum((x_norm - center*0.7)**2))
        
        # Fractional power component creating rugged terrain with controlled roughness and directional bias
        rugged = np.sum(np.abs(x_norm)**3.2 + 0.5 * np.sin(15 * np.pi * x_norm))
        
        # Additional harmonic component for increased complexity with non-uniform frequency distribution
        harmonic = np.sum(np.sin(50 * np.pi * x_norm**2) * np.cos(40 * np.pi * x_norm**2) + 
                          np.sin(55 * np.pi * x_norm**3) * np.cos(45 * np.pi * x_norm**3))
        
        # Cross-dimensional interaction terms to increase complexity
        cross_interaction = np.sum((x_norm[:-1] - x_norm[1:])**6) if self.dim > 1 else 0
        
        # Combine all components with varying weights and nonlinear interactions
        result = 0.4 * chaotic + 0.35 * poly_chaos + 0.2 * wave_interference + 0.15 * peaks + 0.1 * rugged + 0.06 * harmonic + 0.05 * cross_interaction
        
        # Add controlled noise term
        noise_factor = 0.04 * (1 + np.abs(np.sum(x_norm**6)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
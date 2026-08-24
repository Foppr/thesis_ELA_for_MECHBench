import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced chaotic component with modified frequency interactions and cross-terms
        chaotic = np.sum(np.sin(28 * np.pi * x_norm) * np.cos(22 * np.pi * x_norm) * np.exp(10 * np.abs(x_norm)) + 
                         np.sin(18 * np.pi * x_norm**2) * np.cos(12 * np.pi * x_norm**2) * np.exp(-5 * np.abs(x_norm)))
        
        # Higher degree polynomial chaos with altered local minima structure
        poly_chaos = np.sum((x_norm**8 - 15 * x_norm**6 + 50 * x_norm**4 - 80 * x_norm**2)**2)
        
        # Interfering sinusoidal waves with modified amplitudes, phases, and spatial frequency
        wave_interference = np.sum(np.sin(38 * np.pi * x_norm) * np.cos(28 * np.pi * x_norm) * 
                                  np.exp(-3 * np.abs(x_norm)) + 
                                  np.sin(32 * np.pi * x_norm**3) * np.cos(22 * np.pi * x_norm**3) * 
                                  np.exp(-2.5 * np.abs(x_norm)))
        
        # Structured Gaussian-like peaks with altered spacing and varying heights
        peaks = 0
        centers = np.linspace(-1, 1, 18)
        for i in range(18):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += 2.2 * np.exp(-4.5 * np.sum((x_norm - center)**2)) + 0.8 * np.exp(-2.5 * np.sum((x_norm - center*0.7)**2))
        
        # Fractional power component with modified roughness and directional bias
        rugged = np.sum(np.abs(x_norm)**2.5 + 0.5 * np.sin(15 * np.pi * x_norm))
        
        # Additional harmonic component with non-uniform frequency distribution
        harmonic = np.sum(np.sin(42 * np.pi * x_norm**2) * np.cos(32 * np.pi * x_norm**2) + 
                          np.sin(48 * np.pi * x_norm**3) * np.cos(38 * np.pi * x_norm**3))
        
        # Cross-dimensional interaction terms with modified strength
        cross_interaction = np.sum((x_norm[:-1] - x_norm[1:])**4) if self.dim > 1 else 0
        
        # Combine all components with adjusted weights and nonlinear interactions
        result = 0.33 * chaotic + 0.32 * poly_chaos + 0.23 * wave_interference + 0.19 * peaks + 0.13 * rugged + 0.09 * harmonic + 0.06 * cross_interaction
        
        # Add controlled noise term
        noise_factor = 0.025 * (1 + np.abs(np.sum(x_norm**4)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
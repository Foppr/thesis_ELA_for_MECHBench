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
        chaotic = np.sum(np.sin(30 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * np.exp(15 * np.abs(x_norm)) + 
                         np.sin(20 * np.pi * x_norm**2) * np.cos(15 * np.pi * x_norm**2) * np.exp(-8 * np.abs(x_norm)))
        
        # Higher degree polynomial chaos with modified coefficients and additional local minima
        poly_chaos = np.sum((x_norm**8 - 15 * x_norm**6 + 50 * x_norm**4 - 80 * x_norm**2)**2)
        
        # Interfering sinusoidal waves with altered amplitudes, phases, and spatial frequency
        wave_interference = np.sum(np.sin(40 * np.pi * x_norm) * np.cos(30 * np.pi * x_norm) * 
                                  np.exp(-5 * np.abs(x_norm)) + 
                                  np.sin(35 * np.pi * x_norm**3) * np.cos(25 * np.pi * x_norm**3) * 
                                  np.exp(-4 * np.abs(x_norm)))
        
        # Structured Gaussian-like peaks with altered spacing and varying heights
        peaks = 0
        centers = np.linspace(-1, 1, 12)
        for i in range(12):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += 2.5 * np.exp(-6 * np.sum((x_norm - center)**2)) + 0.8 * np.exp(-4 * np.sum((x_norm - center*0.7)**2))
        
        # Fractional power component with modified roughness and directional bias
        rugged = np.sum(np.abs(x_norm)**3.1 + 0.5 * np.sin(15 * np.pi * x_norm))
        
        # Additional harmonic component with non-uniform frequency distribution
        harmonic = np.sum(np.sin(50 * np.pi * x_norm**2) * np.cos(40 * np.pi * x_norm**2) + 
                          np.sin(55 * np.pi * x_norm**3) * np.cos(45 * np.pi * x_norm**3))
        
        # Cross-dimensional interaction terms with modified exponents
        cross_interaction = np.sum((x_norm[:-1] - x_norm[1:])**6) if self.dim > 1 else 0
        
        # Combine all components with modified weights and nonlinear interactions
        result = 0.4 * chaotic + 0.25 * poly_chaos + 0.2 * wave_interference + 0.15 * peaks + 0.1 * rugged + 0.06 * harmonic + 0.05 * cross_interaction
        
        # Add controlled noise term with modified parameters
        noise_factor = 0.025 * (1 + np.abs(np.sum(x_norm**4)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
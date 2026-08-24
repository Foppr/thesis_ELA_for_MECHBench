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
        chaotic = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * np.exp(12 * np.abs(x_norm)) + 
                         np.sin(15 * np.pi * x_norm**2) * np.cos(10 * np.pi * x_norm**2) * np.exp(-6 * np.abs(x_norm)))
        
        # Higher degree polynomial chaos with multiple local minima
        poly_chaos = np.sum((x_norm**7 - 12 * x_norm**5 + 45 * x_norm**3 - 70 * x_norm)**2)
        
        # Interfering sinusoidal waves with varying amplitudes, phases, and spatial frequency
        wave_interference = np.sum(np.sin(35 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * 
                                  np.exp(-4 * np.abs(x_norm)) + 
                                  np.sin(30 * np.pi * x_norm**3) * np.cos(20 * np.pi * x_norm**3) * 
                                  np.exp(-3 * np.abs(x_norm)))
        
        # Structured Gaussian-like peaks with irregular spacing and varying heights
        peaks = 0
        centers = np.linspace(-1, 1, 15)
        for i in range(15):
            center = np.full(self.dim, centers[i % len(centers)])
            peaks += 2.0 * np.exp(-5 * np.sum((x_norm - center)**2)) + 0.7 * np.exp(-3 * np.sum((x_norm - center*0.6)**2))
        
        # Fractional power component creating rugged terrain with controlled roughness and directional bias
        rugged = np.sum(np.abs(x_norm)**2.7 + 0.4 * np.sin(12 * np.pi * x_norm))
        
        # Additional harmonic component for increased complexity with non-uniform frequency distribution
        harmonic = np.sum(np.sin(40 * np.pi * x_norm**2) * np.cos(30 * np.pi * x_norm**2) + 
                          np.sin(45 * np.pi * x_norm**3) * np.cos(35 * np.pi * x_norm**3))
        
        # Cross-dimensional interaction terms to increase complexity
        cross_interaction = np.sum((x_norm[:-1] - x_norm[1:])**5) if self.dim > 1 else 0
        
        # Combine all components with varying weights and nonlinear interactions
        result = 0.35 * chaotic + 0.3 * poly_chaos + 0.25 * wave_interference + 0.18 * peaks + 0.12 * rugged + 0.08 * harmonic + 0.07 * cross_interaction
        
        # Add controlled noise term
        noise_factor = 0.03 * (1 + np.abs(np.sum(x_norm**5)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise
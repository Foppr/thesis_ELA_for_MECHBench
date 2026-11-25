import numpy as np

class SaddlePolynomialChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with mixed degrees and interaction terms
        poly_chaos = np.sum(x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle = np.sum(np.tanh(x_scaled[:-1] * x_scaled[1:]) * 
                       (x_scaled[:-1]**2 - x_scaled[1:]**2))
        
        # Gradient-based attraction basins with varying strength
        attraction = 0.5 * np.sum((x_scaled[:-1] - x_scaled[1:])**2 * 
                                np.exp(-0.5 * (x_scaled[:-1] + x_scaled[1:])**2))
        
        # Multimodal sinusoidal component with frequency modulation based on dimension
        freq_mod = 2 + 0.5 * np.sin(np.pi * self.dim / 4)
        multimodal = np.sum(np.sin(freq_mod * np.pi * x_scaled) * 
                           np.cos(freq_mod * np.pi * x_scaled) + 
                           0.3 * np.sin(2 * freq_mod * np.pi * x_scaled)**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.1 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                               (x_scaled[:-1] * x_scaled[1:]))
        
        # Fractal-like structure using fractional Brownian motion approximations
        fractal = 0.4 * np.sum(np.sin(3 * np.pi * x_scaled**1.5) * 
                              np.cos(2 * np.pi * x_scaled**1.5))
        
        # Noise component with controlled randomness
        noise = 0.05 * np.sum(np.random.randn(self.dim) * x_scaled)
        
        # Combined landscape with optimized weighting for complexity and structure
        return (0.3 * poly_chaos + 0.25 * saddle + 0.2 * attraction + 
                0.15 * multimodal + 0.08 * cross_coupling + 0.01 * fractal + 0.01 * noise)
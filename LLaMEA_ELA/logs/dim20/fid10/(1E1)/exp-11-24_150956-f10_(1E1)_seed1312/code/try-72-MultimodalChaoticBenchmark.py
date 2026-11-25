import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple peaks
        radial = np.sum(np.exp(-5.0 * (x_scaled**2).sum()) * np.cos(10.0 * np.pi * (x_scaled**2).sum()))
        
        # Sinusoidal waves with varying frequencies and amplitudes
        sin_wave = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.0 * x_scaled) + 
                          0.5 * np.sin(7.0 * x_scaled) * np.cos(5.0 * x_scaled))
        
        # Polynomial decay with mixed interaction terms
        poly_decay = np.sum(0.1 * x_scaled**6 + 0.3 * x_scaled**4 + 0.5 * x_scaled**2)
        
        # Cross-terms creating complex interactions between dimensions
        cross_terms = np.sum((x_scaled[:-1]**2) * np.sin(x_scaled[1:]) + 
                            (x_scaled[1:]**2) * np.cos(x_scaled[:-1]))
        
        # Additional chaotic component with non-linear transformation
        chaotic = np.sum(np.sin(5.0 * x_scaled) * np.tanh(2.0 * x_scaled) + 
                         0.2 * np.sin(9.0 * x_scaled) * np.cos(4.0 * x_scaled))
        
        # Combine all components with adaptive weights
        return 0.4 * radial + 0.3 * sin_wave + 0.15 * poly_decay + 0.1 * cross_terms + 0.05 * chaotic + 2.0
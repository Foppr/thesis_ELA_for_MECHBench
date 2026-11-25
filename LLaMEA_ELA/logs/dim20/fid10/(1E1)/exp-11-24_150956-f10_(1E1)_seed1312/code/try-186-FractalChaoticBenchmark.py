import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like self-similar structure with recursive scaling
        fractal_component = np.sum(np.sin(2.0 * np.pi * x_scaled) * 
                                 np.cos(3.0 * np.pi * x_scaled) * 
                                 np.sin(5.0 * np.pi * x_scaled))
        
        # Chaotic sinusoidal interactions with varying frequencies and amplitudes
        chaotic_component = np.sum(np.sin(10.0 * x_scaled**2 + 2.0 * np.sin(7.0 * x_scaled)) * 
                                 np.cos(8.0 * x_scaled**3 + 3.0 * np.cos(5.0 * x_scaled)))
        
        # Adaptive conditioning with exponential decay and logarithmic scaling
        conditioning = np.sum(np.exp(-np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(2.0 * np.log(np.abs(x_scaled) + 1e-8))))
        
        # Cross-dimensional coupling with recursive polynomial interactions
        cross_dim = 0.0
        for i in range(self.dim - 1):
            cross_dim += (x_scaled[i]**2 + x_scaled[i+1]**2) * np.sin(4.0 * (x_scaled[i] + x_scaled[i+1]))
        
        # Multi-scale harmonic interference with phase modulation
        harmonic_component = np.sum(np.sin(6.0 * x_scaled + 0.5 * np.sin(9.0 * x_scaled)) * 
                                  np.cos(4.0 * x_scaled + 0.3 * np.cos(8.0 * x_scaled)))
        
        # Asymmetric basin structure with piecewise polynomial behavior
        basin_component = np.sum(np.where(x_scaled > 0, 
                                        0.5 * x_scaled**4 + 0.3 * x_scaled**2,
                                        0.4 * x_scaled**3 + 0.6 * x_scaled))
        
        # Combine all components with adaptive weights
        return (0.3 * fractal_component + 
                0.25 * chaotic_component + 
                0.2 * conditioning + 
                0.15 * cross_dim + 
                0.08 * harmonic_component + 
                0.02 * basin_component + 1.8)
import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like self-similar structure with recursive scaling
        fractal_component = np.sum(np.power(np.abs(x_scaled), 1.7) * 
                                 np.sin(20.0 * np.power(np.abs(x_scaled), 0.8)) + 
                                 0.5 * np.sin(30.0 * np.power(np.abs(x_scaled), 1.2)))
        
        # Chaotic sine-wave interference with varying amplitudes and frequencies
        chaotic_component = np.sum(np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled) * 
                                 np.exp(-0.5 * x_scaled**2) + 
                                 0.7 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) * 
                                 np.exp(-0.3 * x_scaled**2))
        
        # Adaptive conditioning with exponential weighting
        condition_component = np.sum(np.exp(2.0 * np.abs(x_scaled)) * 
                                   (1.0 + 0.3 * np.sin(5.0 * x_scaled) * np.cos(4.0 * x_scaled)))
        
        # Non-separable cross-dimensional interactions with polynomial coupling
        cross_component = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                               np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                               (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                               np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic resonance with phase modulation
        resonance_component = np.sum(np.sin(8.0 * x_scaled) * np.cos(10.0 * x_scaled) * 
                                   np.sin(6.0 * x_scaled**2) + 
                                   0.6 * np.sin(12.0 * x_scaled**3) * np.cos(14.0 * x_scaled**3) * 
                                   np.exp(-0.2 * np.abs(x_scaled)))
        
        # Asymmetric landscape with weighted sum of components
        return 0.25 * fractal_component + 0.25 * chaotic_component + 0.2 * condition_component + \
               0.15 * cross_component + 0.15 * resonance_component + 2.1
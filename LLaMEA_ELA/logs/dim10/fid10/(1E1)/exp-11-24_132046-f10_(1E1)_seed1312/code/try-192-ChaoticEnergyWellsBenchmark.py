import numpy as np

class ChaoticEnergyWellsBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal energy wells with varying depths
        energy_wells = np.sum(3.0 * np.exp(-2.0 * (x_norm**2)) * 
                             (1.0 + 0.5 * np.sin(8 * np.pi * x_norm)) * 
                             (1.0 + 0.3 * np.cos(6 * np.pi * x_norm)))
        
        # Exponential decay corridors with chaotic modulation
        decay_corridors = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                                (1.0 + 0.4 * np.sin(15 * np.pi * x_norm)) * 
                                (1.0 + 0.3 * np.cos(12 * np.pi * x_norm)))
        
        # Adaptive conditioning with chaotic scaling
        adaptive_scaling = np.sum((1.0 + 0.6 * np.sin(5 * np.pi * x_norm)) * 
                                 np.exp(-0.3 * x_norm**2) * 
                                 (1.0 + 0.2 * np.cos(7 * np.pi * x_norm)))
        
        # Multi-frequency harmonic interference
        harmonic_interference = np.sum(np.sin(4 * x_norm) * np.cos(3 * x_norm) * 
                                      (1.0 + 0.5 * np.sin(2 * x_norm)) * 
                                      (1.0 + 0.4 * np.cos(5 * x_norm)))
        
        # Fractal-like energy landscape with self-similarity
        fractal_energy = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.sin(10 * x_norm))) * 
                               (1.0 + 0.3 * np.cos(9 * x_norm)))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1.0 + 0.2 * np.sin(3 * np.pi * x_norm[:-1])) * 
                               (1.0 + 0.2 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Power-law energy distribution with periodic modulation
        power_energy = np.sum(np.abs(x_norm)**1.7 * (1.0 + 0.3 * np.sin(11 * x_norm)) * 
                             (1.0 + 0.2 * np.cos(8 * x_norm)))
        
        # Combined chaotic landscape with varying curvature
        return 2.0 * (energy_wells + decay_corridors + adaptive_scaling + 
                     harmonic_interference + fractal_energy + cross_coupling + 
                     power_energy)
import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle structure with exponential growth
        chaotic_saddles = np.sum(np.exp(-5.0 * np.abs(x_norm)) * 
                                np.sin(10.0 * x_norm) * 
                                np.cos(7.0 * x_norm))
        
        # Multi-scale harmonic peaks with varying amplitudes
        harmonic_peaks = np.sum(np.sin(20.0 * x_norm) * 
                               np.cos(15.0 * x_norm) * 
                               (1.0 + 0.5 * np.sin(3.0 * x_norm)) * 
                               (1.0 + 0.3 * np.cos(5.0 * x_norm)))
        
        # Cross-dimensional coupling with non-linear interaction
        cross_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                               np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Sharp curvature regions with varying conditioning
        sharp_curvature = np.sum(np.abs(x_norm)**3.0 * 
                                np.sin(8.0 * x_norm) * 
                                np.cos(6.0 * x_norm))
        
        # Fractal-like ridge structure with self-similarity
        fractal_ridges = np.sum(np.sin(12.0 * x_norm) * 
                               np.exp(-0.5 * (x_norm**2)) * 
                               (1.0 + 0.2 * np.sin(4.0 * x_norm)))
        
        # Adaptive conditioning with dynamic scaling
        adaptive_scaling = np.sum((1.0 + 0.3 * np.sin(9.0 * x_norm)) * 
                                 np.exp(-0.2 * np.abs(x_norm)) * 
                                 (1.0 + 0.4 * np.cos(7.0 * x_norm)))
        
        # Combined landscape with chaotic transitions
        return 2.0 * (chaotic_saddles + harmonic_peaks + cross_coupling + 
                     sharp_curvature + fractal_ridges + adaptive_scaling)
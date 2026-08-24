import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Tent map chaotic component with varying parameter
        tent_map = np.sum(1.0 - 2.0 * np.abs(x_scaled - 0.5))
        
        # Spectral wave interference with multiple frequencies
        wave_interference = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled) * 
                                 np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Adaptive elliptic contour with dynamic eccentricity
        elliptic_term = np.sum((x_scaled**2 + 0.5 * np.sin(10 * x_scaled)**2) * 
                              (x_scaled**2 + 0.3 * np.cos(15 * x_scaled)**2))
        
        # Mixed Gaussian and exponential peaks with varying widths
        gaussian_peaks = np.sum(np.exp(-2.0 * x_scaled**2) * (np.sin(6 * np.pi * x_scaled)**2 + 
                                                            0.7 * np.cos(9 * np.pi * x_scaled)**2))
        
        # Hyperbolic tangent modulation for sharp transitions
        tanh_mod = np.sum(np.tanh(5 * x_scaled) * np.sin(7 * np.pi * x_scaled))
        
        # Radial sine modulation with multiple harmonics
        radial_sine = np.sum(np.sin(10 * np.pi * np.linalg.norm(x_scaled, axis=0)) * 
                            np.cos(5 * np.pi * np.linalg.norm(x_scaled, axis=0)))
        
        # Combine all terms with optimized weights
        return 0.25 * tent_map + 0.3 * wave_interference + 0.15 * elliptic_term + 0.12 * gaussian_peaks + 0.08 * tanh_mod + 0.1 * radial_sine
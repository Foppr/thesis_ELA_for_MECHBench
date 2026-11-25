import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with varying heights and widths
        peaks = np.sum(0.7 * np.exp(-3.5 * (x_scaled - 0.25)**2) + 
                      0.3 * np.exp(-2.0 * (x_scaled + 0.35)**2) + 
                      0.18 * np.exp(-5.5 * (x_scaled - 0.75)**2) + 
                      0.12 * np.exp(-1.8 * (x_scaled + 0.85)**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(13.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                        0.7 * np.sin(19.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                        0.5 * np.sin(26.0 * x_scaled**3) * np.cos(19.0 * x_scaled**3))
        
        # Adaptive dimensionality scaling with exponential decay
        dim_scaling = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(3.5 * x_scaled)))
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(2.5 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.5 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(4.5 * x_scaled) * np.cos(7.5 * x_scaled) + 
                         0.9 * np.sin(8.5 * x_scaled**2) * np.cos(10.5 * x_scaled**2) + 
                         0.6 * np.sin(14.5 * x_scaled**3) * np.cos(16.5 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.38 * peaks + 0.32 * sin_mod + 0.11 * dim_scaling + 0.11 * cross_terms + 0.08 * harmonics + 1.55
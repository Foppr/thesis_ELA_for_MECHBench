import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with varying heights and widths
        peaks = np.sum(0.65 * np.exp(-4.2 * (x_scaled - 0.3)**2) + 
                      0.28 * np.exp(-2.7 * (x_scaled + 0.4)**2) + 
                      0.16 * np.exp(-6.2 * (x_scaled - 0.8)**2) + 
                      0.11 * np.exp(-1.7 * (x_scaled + 0.9)**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(13.0 * x_scaled) * np.cos(11.0 * x_scaled) + 
                        0.62 * np.sin(19.0 * x_scaled**2) * np.cos(16.0 * x_scaled**2) + 
                        0.42 * np.sin(26.0 * x_scaled**3) * np.cos(21.0 * x_scaled**3))
        
        # Adaptive dimensionality scaling with exponential decay
        dim_scaling = np.sum(np.exp(-0.62 * np.abs(x_scaled)) * (1.0 + 0.42 * np.sin(4.2 * x_scaled)))
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(3.2 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.2 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(5.2 * x_scaled) * np.cos(7.2 * x_scaled) + 
                         0.82 * np.sin(9.2 * x_scaled**2) * np.cos(11.2 * x_scaled**2) + 
                         0.52 * np.sin(15.2 * x_scaled**3) * np.cos(17.2 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.36 * peaks + 0.34 * sin_mod + 0.11 * dim_scaling + 0.11 * cross_terms + 0.08 * harmonics + 1.6
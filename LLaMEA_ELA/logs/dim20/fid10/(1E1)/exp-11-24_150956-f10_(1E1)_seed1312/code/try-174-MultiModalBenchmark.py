import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with varying heights and widths
        peaks = np.sum(0.55 * np.exp(-3.8 * (x_scaled - 0.32)**2) + 
                      0.28 * np.exp(-2.7 * (x_scaled + 0.41)**2) + 
                      0.16 * np.exp(-5.8 * (x_scaled - 0.78)**2) + 
                      0.11 * np.exp(-1.3 * (x_scaled + 0.91)**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(11.5 * x_scaled) * np.cos(9.8 * x_scaled) + 
                        0.62 * np.sin(17.8 * x_scaled**2) * np.cos(14.5 * x_scaled**2) + 
                        0.38 * np.sin(24.5 * x_scaled**3) * np.cos(19.8 * x_scaled**3))
        
        # Adaptive dimensionality scaling with exponential decay
        dim_scaling = np.sum(np.exp(-0.55 * np.abs(x_scaled)) * (1.0 + 0.38 * np.sin(4.2 * x_scaled)))
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(3.2 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.1 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(5.2 * x_scaled) * np.cos(7.2 * x_scaled) + 
                         0.82 * np.sin(9.2 * x_scaled**2) * np.cos(11.2 * x_scaled**2) + 
                         0.52 * np.sin(15.2 * x_scaled**3) * np.cos(17.2 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.36 * peaks + 0.34 * sin_mod + 0.11 * dim_scaling + 0.11 * cross_terms + 0.08 * harmonics + 1.58
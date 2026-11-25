import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with varying heights and widths
        peaks = np.sum(0.6 * np.exp(-4.0 * (x_scaled - 0.3)**2) + 
                      0.25 * np.exp(-2.5 * (x_scaled + 0.4)**2) + 
                      0.15 * np.exp(-6.0 * (x_scaled - 0.8)**2) + 
                      0.1 * np.exp(-1.5 * (x_scaled + 0.9)**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(14.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.6 * np.sin(20.0 * x_scaled**2) * np.cos(17.0 * x_scaled**2) + 
                        0.4 * np.sin(28.0 * x_scaled**3) * np.cos(23.0 * x_scaled**3))
        
        # Adaptive dimensionality scaling with exponential decay
        dim_scaling = np.sum(np.exp(-0.6 * np.abs(x_scaled)) * (1.0 + 0.4 * np.sin(4.0 * x_scaled)))
        
        # Enhanced cross-dimensional interaction terms with polynomial coupling and additional coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(3.5 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.5 * (x_scaled[:-2] - x_scaled[2:])) + 
                           0.5 * (x_scaled[:-1]**2 * x_scaled[1:]**2) * 
                           np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(5.5 * x_scaled) * np.cos(7.5 * x_scaled) + 
                         0.8 * np.sin(9.5 * x_scaled**2) * np.cos(11.5 * x_scaled**2) + 
                         0.5 * np.sin(15.5 * x_scaled**3) * np.cos(17.5 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.35 * peaks + 0.35 * sin_mod + 0.12 * dim_scaling + 0.1 * cross_terms + 0.08 * harmonics + 1.6
import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sharper Gaussian peaks with increased contrast
        peaks = np.sum(0.8 * np.exp(-6.0 * (x_scaled - 0.3)**2) + 
                      0.4 * np.exp(-3.5 * (x_scaled + 0.4)**2) + 
                      0.25 * np.exp(-8.0 * (x_scaled - 0.8)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.9)**2))
        
        # Enhanced sinusoidal modulation with higher frequencies
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(28.0 * x_scaled**3) * np.cos(25.0 * x_scaled**3))
        
        # Modified dimensionality scaling with stronger exponential decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled)))
        
        # Enhanced cross-dimensional interaction terms with cubic coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with more complex phase relationships
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.6 * np.sin(18.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3))
        
        # Asymmetric landscape with stronger weighted components
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 1.5
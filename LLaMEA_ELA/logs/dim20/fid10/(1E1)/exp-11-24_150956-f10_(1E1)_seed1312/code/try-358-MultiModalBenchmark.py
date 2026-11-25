import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with varying heights, widths and positions
        peaks = np.sum(0.7 * np.exp(-5.0 * (x_scaled - 0.25)**2) + 
                      0.3 * np.exp(-3.0 * (x_scaled + 0.4)**2) + 
                      0.2 * np.exp(-7.0 * (x_scaled - 0.7)**2) + 
                      0.15 * np.exp(-2.0 * (x_scaled + 0.9)**2) + 
                      0.1 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Complex sinusoidal modulation with higher frequencies and amplitude variations
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(25.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3) + 
                        0.3 * np.sin(30.0 * x_scaled**4) * np.cos(28.0 * x_scaled**4))
        
        # Enhanced dimensionality scaling with exponential decay and sinusoidal modulation
        dim_scaling = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled) + 
                           0.3 * np.cos(3.0 * x_scaled)))
        
        # Advanced cross-dimensional interaction terms with higher-order polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           (x_scaled[:-3]**2 + x_scaled[3:]**2) * 
                           np.sin(2.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Multi-scale harmonic interference with phase shifts and additional frequency components
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.6 * np.sin(16.0 * x_scaled**3) * np.cos(19.0 * x_scaled**3) + 
                         0.4 * np.sin(22.0 * x_scaled**4) * np.cos(25.0 * x_scaled**4))
        
        # Asymmetric landscape with weighted sum of components and additional noise-like terms
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 1.8
import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with increased variability
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.3)**2) + 
                      0.35 * np.exp(-3.0 * (x_scaled + 0.4)**2) + 
                      0.25 * np.exp(-7.0 * (x_scaled - 0.8)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.9)**2) +
                      0.15 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Dynamic sinusoidal modulation with higher frequency components
        sin_mod = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                        0.7 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) + 
                        0.5 * np.sin(35.0 * x_scaled**3) * np.cos(30.0 * x_scaled**3) +
                        0.3 * np.sin(40.0 * x_scaled**4) * np.cos(35.0 * x_scaled**4))
        
        # Enhanced dimensionality scaling with stronger exponential decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(5.0 * x_scaled) + 
                           0.3 * np.cos(4.0 * x_scaled)))
        
        # Stronger cross-dimensional interaction terms with higher-order coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**4 + x_scaled[3:]**4) * 
                           np.sin(2.5 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Multi-scale harmonic interference with phase shifts and amplitude modulation
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.6 * np.sin(20.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3) +
                         0.4 * np.sin(25.0 * x_scaled**4) * np.cos(27.0 * x_scaled**4))
        
        # Asymmetric landscape with weighted sum of components and additional noise
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.0
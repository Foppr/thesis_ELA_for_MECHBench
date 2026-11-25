import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with higher contrast and sharper peaks
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.35 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.25 * np.exp(-7.0 * (x_scaled - 0.7)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.9)**2))
        
        # Modified sinusoidal modulation with increased frequency and amplitude
        sin_mod = np.sum(1.2 * np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.8 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.6 * np.sin(25.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3))
        
        # Enhanced dimensionality scaling with more pronounced exponential decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(5.0 * x_scaled)))
        
        # Stronger cross-dimensional interaction terms with higher-order polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Enhanced harmonic interference with additional phase shifts and frequencies
        harmonics = np.sum(1.1 * np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.7 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3))
        
        # Asymmetric landscape with modified weighted sum of components
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 1.5
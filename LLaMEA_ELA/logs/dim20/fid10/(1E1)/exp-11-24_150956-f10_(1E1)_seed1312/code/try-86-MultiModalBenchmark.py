import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sharper Gaussian peaks with more distinct local minima
        peaks = np.sum(0.8 * np.exp(-10.0 * (x_scaled - 0.3)**2) + 
                      0.5 * np.exp(-6.0 * (x_scaled + 0.4)**2) + 
                      0.3 * np.exp(-12.0 * (x_scaled - 0.8)**2) + 
                      0.2 * np.exp(-4.0 * (x_scaled + 0.9)**2))
        
        # Enhanced sinusoidal modulation with higher frequency components
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.4 * np.sin(25.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3))
        
        # Modified dimensionality scaling with stronger exponential decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.7 * np.sin(4.0 * x_scaled)))
        
        # Enhanced cross-dimensional interaction with stronger coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(3.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Improved harmonic interference with asymmetric phase shifts
        harmonics = np.sum(np.sin(5.0 * x_scaled) * np.cos(7.0 * x_scaled) + 
                         0.8 * np.sin(10.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.5 * np.sin(15.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3))
        
        # Asymmetric landscape with modified weights for better separation of optima
        return 0.5 * peaks + 0.25 * sin_mod + 0.1 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 1.2
import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic Gaussian peaks with asymmetric heights and widths
        peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * 
                      np.sin(7.0 * x_scaled) + 
                      0.3 * np.exp(-5.0 * (x_scaled + 0.5)**2) * 
                      np.cos(9.0 * x_scaled) + 
                      0.2 * np.exp(-4.0 * (x_scaled - 0.7)**2) * 
                      np.sin(11.0 * x_scaled**2) + 
                      0.15 * np.exp(-6.0 * (x_scaled + 0.9)**2) * 
                      np.cos(13.0 * x_scaled**2))
        
        # Hyper-chaotic sinusoidal modulation with fractional frequencies
        sin_mod = np.sum(np.sin(15.0 * x_scaled + 0.5 * np.sin(8.0 * x_scaled)) + 
                        0.7 * np.cos(20.0 * x_scaled**1.5 + 0.3 * np.cos(12.0 * x_scaled)) + 
                        0.5 * np.sin(25.0 * x_scaled**0.8 + 0.4 * np.sin(16.0 * x_scaled**2)))
        
        # Asymmetric dimension scaling with logistic map behavior
        dim_scaling = np.sum(1.0 + 0.5 * np.sin(3.0 * x_scaled) * 
                           (1.0 - np.exp(-0.8 * np.abs(x_scaled))) + 
                           0.3 * np.cos(5.0 * x_scaled) * 
                           np.exp(-0.5 * x_scaled**2))
        
        # Complex cross-dimensional interaction with coupled polynomial terms
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**2 + x_scaled[2:]**2) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           0.5 * (x_scaled[:-1]**4 + x_scaled[1:]**4) * 
                           np.sin(2.0 * (x_scaled[:-1] * x_scaled[1:])))
        
        # Multi-scale harmonic interference with dynamic phase shifts
        harmonics = np.sum(np.sin(6.0 * x_scaled + 0.3 * np.sin(10.0 * x_scaled)) * 
                         np.cos(8.0 * x_scaled + 0.2 * np.cos(12.0 * x_scaled)) + 
                         0.7 * np.sin(14.0 * x_scaled**2 + 0.4 * np.sin(18.0 * x_scaled**2)) * 
                         np.cos(16.0 * x_scaled**2 + 0.3 * np.cos(20.0 * x_scaled**2)) + 
                         0.4 * np.sin(22.0 * x_scaled**3 + 0.5 * np.sin(24.0 * x_scaled**3)) * 
                         np.cos(24.0 * x_scaled**3 + 0.2 * np.cos(26.0 * x_scaled**3)))
        
        # Asymmetric landscape with weighted sum of components
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
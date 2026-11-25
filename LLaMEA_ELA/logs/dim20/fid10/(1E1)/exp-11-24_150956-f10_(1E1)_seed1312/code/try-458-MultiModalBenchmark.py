import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian_peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) + 
                               0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) + 
                               0.3 * np.exp(-2.0 * (x_scaled - 0.7)**2) + 
                               0.2 * np.exp(-4.0 * (x_scaled + 0.8)**2))
        
        # Exponentially decaying sinusoidal waves with multiple frequencies
        sin_waves = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                          (np.sin(10.0 * x_scaled) + 0.5 * np.sin(15.0 * x_scaled**2) + 
                           0.3 * np.sin(20.0 * x_scaled**3)))
        
        # Cubic cross-dimensional interaction terms
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.cos(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.sin(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric landscape with polynomial and exponential components
        asymmetry = np.sum(0.5 * x_scaled**4 + 0.3 * np.exp(-1.5 * x_scaled**2) + 
                         0.2 * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled))
        
        # Multi-scale harmonic interference with varying amplitudes
        harmonics = np.sum(np.exp(-0.5 * x_scaled**2) * np.sin(12.0 * x_scaled) + 
                         0.7 * np.exp(-1.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.4 * np.exp(-2.0 * x_scaled**2) * np.sin(18.0 * x_scaled**3))
        
        # Combine all components with different weights
        return 0.4 * gaussian_peaks + 0.3 * sin_waves + 0.15 * cross_terms + 0.1 * asymmetry + 0.05 * harmonics + 2.1
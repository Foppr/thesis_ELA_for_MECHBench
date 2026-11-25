import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponentially decaying sinusoidal components with varying frequencies
        exp_sin = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                        (np.sin(8.0 * x_scaled) + 0.7 * np.sin(15.0 * x_scaled) + 
                         0.3 * np.sin(25.0 * x_scaled)))
        
        # Polynomial cross-dimensional interactions with varying degrees
        poly_cross = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           (x_scaled[:-1]**2 + x_scaled[1:]**2) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           (x_scaled[:-2]**2 + x_scaled[2:]**2))
        
        # Adaptive peak positioning with exponential weighting
        adaptive_peaks = np.sum(np.exp(-3.0 * (x_scaled - 0.5)**2) * 
                              (1.0 + 0.5 * np.sin(10.0 * x_scaled)) + 
                              np.exp(-2.5 * (x_scaled + 0.3)**2) * 
                              (1.0 + 0.3 * np.cos(12.0 * x_scaled)))
        
        # Multi-scale harmonic interference with varying amplitudes
        multi_harmonic = np.sum(0.8 * np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                              0.5 * np.sin(14.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                              0.3 * np.sin(22.0 * x_scaled**3) * np.cos(26.0 * x_scaled**3))
        
        # Asymmetric exponential decay with polynomial modulation
        asym_decay = np.sum(np.exp(-1.5 * x_scaled**2) * (x_scaled**4 + 0.5 * x_scaled**2) + 
                           np.exp(-2.0 * x_scaled**3) * (x_scaled**3 + 0.3 * x_scaled))
        
        # Combine all components with adaptive weights
        return 0.3 * exp_sin + 0.25 * poly_cross + 0.2 * adaptive_peaks + \
               0.15 * multi_harmonic + 0.1 * asym_decay + 2.1
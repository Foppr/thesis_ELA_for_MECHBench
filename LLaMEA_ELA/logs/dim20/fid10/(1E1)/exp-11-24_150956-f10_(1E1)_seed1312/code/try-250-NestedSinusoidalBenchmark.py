import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sin = np.sum(np.sin(2.0 * np.pi * x_scaled) * 
                           np.sin(4.0 * np.pi * x_scaled) * 
                           np.sin(8.0 * np.pi * x_scaled))
        
        # Asymmetric Gaussian peaks with different variances and heights
        asym_peaks = np.sum(0.5 * np.exp(-2.0 * (x_scaled - 0.2)**2) + 
                           0.3 * np.exp(-1.0 * (x_scaled + 0.3)**2) + 
                           0.2 * np.exp(-3.0 * (x_scaled - 0.7)**2) + 
                           0.4 * np.exp(-0.5 * (x_scaled + 0.8)**2))
        
        # Adaptive conditioning with exponential weighting
        condition = np.sum(np.exp(2.0 * np.abs(x_scaled)) * 
                          np.sin(3.0 * x_scaled) * 
                          np.cos(2.0 * x_scaled))
        
        # Cross-dimensional coupling with polynomial interactions
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                              np.sin(2.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                              (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                              np.cos(1.5 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Fractal-like structure with recursive pattern
        fractal = np.sum(np.sin(10.0 * x_scaled) * 
                        np.cos(5.0 * x_scaled) * 
                        np.sin(2.0 * x_scaled**2))
        
        # Asymmetric landscape with weighted combination
        return 0.4 * nested_sin + 0.3 * asym_peaks + 0.15 * condition + 0.1 * cross_coupling + 0.05 * fractal + 2.1
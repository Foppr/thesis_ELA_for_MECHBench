import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sin = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                           0.7 * np.sin(35.0 * x_scaled**2) * np.cos(25.0 * x_scaled**2) + 
                           0.4 * np.sin(50.0 * x_scaled**3) * np.cos(40.0 * x_scaled**3))
        
        # Asymmetric Gaussian peaks with different widths and heights
        asym_peaks = np.sum(0.8 * np.exp(-10.0 * (x_scaled - 0.2)**2) * (1.0 + 0.3 * np.sin(5.0 * x_scaled)) +
                           0.5 * np.exp(-5.0 * (x_scaled + 0.3)**2) * (1.0 + 0.5 * np.cos(7.0 * x_scaled)) +
                           0.3 * np.exp(-15.0 * (x_scaled - 0.7)**2) * (1.0 + 0.4 * np.sin(9.0 * x_scaled)))
        
        # Cross-dimensional polynomial interactions with asymmetric coupling
        cross_poly = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                           (x_scaled[:-2]**2 * x_scaled[2:] + x_scaled[:-2] * x_scaled[2:]**2) * 
                           np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Sharp transition regions with exponential weighting
        transitions = np.sum(np.exp(-5.0 * np.abs(x_scaled - 0.1)) * np.sin(20.0 * x_scaled) +
                           np.exp(-3.0 * np.abs(x_scaled + 0.4)) * np.cos(18.0 * x_scaled) +
                           np.exp(-7.0 * np.abs(x_scaled - 0.8)) * np.sin(25.0 * x_scaled))
        
        # Quadratic modulation with asymmetric coefficients
        quad_mod = np.sum(0.6 * x_scaled**2 + 0.4 * x_scaled**3 + 0.2 * x_scaled**4)
        
        # Combine all components with different weights and add global offset
        return 0.4 * nested_sin + 0.3 * asym_peaks + 0.15 * cross_poly + 0.1 * transitions + 0.05 * quad_mod + 2.1
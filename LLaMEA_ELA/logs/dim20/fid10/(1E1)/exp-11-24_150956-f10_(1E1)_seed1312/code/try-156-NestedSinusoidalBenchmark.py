import numpy as np

class NestedSinusoidalBenchmark:
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
        gaussian_peaks = np.sum(0.8 * np.exp(-10.0 * (x_scaled - 0.2)**2) * 
                              (1.0 + 0.5 * np.sin(5.0 * x_scaled)) + 
                              0.5 * np.exp(-5.0 * (x_scaled + 0.3)**2) * 
                              (1.0 + 0.3 * np.cos(7.0 * x_scaled)) + 
                              0.3 * np.exp(-15.0 * (x_scaled - 0.7)**2) * 
                              (1.0 + 0.4 * np.sin(9.0 * x_scaled)))
        
        # Cross-dimensional interaction with polynomial coupling and exponential decay
        cross_interaction = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                                 np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) * 
                                 np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                                 (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                                 np.exp(-0.3 * (x_scaled[:-2] - x_scaled[2:])**2) * 
                                 np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Sharp transition regions with step-like behavior
        sharp_transitions = np.sum(np.abs(x_scaled[:-1] - x_scaled[1:]) * 
                                 np.exp(-5.0 * np.abs(x_scaled[:-1] - x_scaled[1:])) + 
                                 np.abs(x_scaled[:-2] - x_scaled[2:]) * 
                                 np.exp(-3.0 * np.abs(x_scaled[:-2] - x_scaled[2:])))
        
        # Asymmetric scaling with logarithmic transformation
        asymmetric_scaling = np.sum(np.log(1.0 + 2.0 * np.abs(x_scaled)) * 
                                  np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled))
        
        # Combine all components with different weights
        return 0.4 * nested_sin + 0.35 * gaussian_peaks + 0.15 * cross_interaction + 0.08 * sharp_transitions + 0.02 * asymmetric_scaling + 2.1
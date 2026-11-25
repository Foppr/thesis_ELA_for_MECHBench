import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaos component
        logistic_chaos = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Trigonometric chaos with varying frequencies
        trig_chaos = np.sum(np.sin(10.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                           np.sin(20.0 * x_scaled**2) * np.cos(25.0 * x_scaled**2))
        
        # Radial symmetry with polynomial decay
        radial_sym = np.sum((x_scaled**2).sum() ** 0.5 * np.sin(5.0 * (x_scaled**2).sum() ** 0.5))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = np.sum(np.exp(-2.0 * np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                               np.sin(3.0 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Multi-scale fractal-like structure
        fractal = np.sum(np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.5 * np.sin(16.0 * x_scaled**2) * np.cos(24.0 * x_scaled**2) + 
                        0.3 * np.sin(32.0 * x_scaled**3) * np.cos(48.0 * x_scaled**3))
        
        # Asymmetric distortion with piecewise polynomial
        asym_distortion = np.sum(np.where(x_scaled > 0, x_scaled**3, -x_scaled**2))
        
        # Combine all components with adaptive weights
        return (0.3 * logistic_chaos + 
                0.25 * trig_chaos + 
                0.15 * radial_sym + 
                0.12 * cross_coupling + 
                0.1 * fractal + 
                0.08 * asym_distortion + 
                2.1)
import numpy as np

class OscillatoryRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying widths
        radial = np.sum(np.exp(-5.0 * (x_norm**2)) + 
                       0.5 * np.exp(-2.0 * (x_norm - 0.3)**2) + 
                       0.3 * np.exp(-3.0 * (x_norm + 0.4)**2))
        
        # Multi-frequency sine oscillations creating multiple local minima
        sine_osc = np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm) + 
                         0.7 * np.sin(15 * x_norm) * np.cos(12 * x_norm) + 
                         0.5 * np.sin(20 * x_norm) * np.cos(18 * x_norm))
        
        # Cross-dimensional interaction with adaptive coupling
        cross_dim = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                          (1 + 0.3 * np.sin(5 * x_norm[:-1])) * 
                          (1 + 0.2 * np.cos(4 * x_norm[1:])))
        
        # Adaptive conditioning based on position
        conditioning = np.sum((1 + 0.5 * np.abs(x_norm)) * 
                            np.exp(-0.5 * x_norm**2) * 
                            (1 + 0.3 * np.sin(3 * x_norm)))
        
        # Fractal-like structure with recursive pattern
        fractal = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                        (1 + 0.2 * np.sin(10 * x_norm)) * 
                        (1 + 0.1 * np.cos(8 * x_norm)))
        
        # Asymmetric peaks and valleys
        asymmetry = np.sum(np.abs(x_norm)**1.5 * (1 + 0.4 * np.sin(6 * x_norm)) + 
                          0.3 * np.exp(-2.0 * np.abs(x_norm - 0.5)))
        
        # Combined landscape
        return 2.0 * (radial + sine_osc + cross_dim + conditioning + fractal + asymmetry)
import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component with varying r parameters
        logistic = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Spherical harmonics with varying degrees and orders
        sph_harms = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.0 * x_scaled) + 
                          np.sin(5.0 * x_scaled**2) * np.cos(4.0 * x_scaled**2) + 
                          np.sin(7.0 * x_scaled**3) * np.cos(6.0 * x_scaled**3))
        
        # Asymmetric bell-shaped components with different variances
        bells = np.sum(0.5 * np.exp(-2.0 * (x_scaled - 0.2)**2) + 
                      0.3 * np.exp(-1.5 * (x_scaled + 0.3)**2) + 
                      0.2 * np.exp(-3.0 * (x_scaled - 0.7)**2))
        
        # Cross-dimensional coupling with chaotic interaction terms
        cross_coupling = np.sum(np.sin(2.0 * x_scaled[:-1]) * np.cos(3.0 * x_scaled[1:]) + 
                               np.sin(4.0 * x_scaled[:-2]) * np.cos(5.0 * x_scaled[2:]))
        
        # Multi-scale sinusoidal modulation with exponentially decaying amplitudes
        modulated = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * 
                          (np.sin(10.0 * x_scaled) + 0.5 * np.sin(20.0 * x_scaled**2)))
        
        # Asymmetric quadratic penalty with mixed signs
        quad_penalty = np.sum(0.3 * x_scaled**2 + 0.2 * np.abs(x_scaled)**1.5 - 0.1 * x_scaled**3)
        
        # Combine all components with adaptive weights
        return 0.4 * logistic + 0.3 * sph_harms + 0.15 * bells + 0.08 * cross_coupling + \
               0.05 * modulated + 0.02 * quad_penalty + 1.8
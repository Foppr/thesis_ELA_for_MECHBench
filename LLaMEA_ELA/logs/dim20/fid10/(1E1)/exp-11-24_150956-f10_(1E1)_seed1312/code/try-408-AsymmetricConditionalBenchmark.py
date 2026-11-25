import numpy as np

class AsymmetricConditionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with different widths and heights
        peak1 = 0.8 * np.exp(-3.0 * (x_scaled - 0.4)**2) * np.exp(-0.5 * (x_scaled - 0.4)**4)
        peak2 = 0.5 * np.exp(-5.0 * (x_scaled + 0.6)**2) * np.exp(-0.3 * (x_scaled + 0.6)**6)
        peak3 = 0.3 * np.exp(-2.0 * (x_scaled - 0.9)**2) * np.exp(-0.7 * (x_scaled - 0.9)**3)
        
        # Trigonometric coupling between dimensions
        trig_coupling = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                              0.7 * np.sin(12.0 * x_scaled**2) * np.cos(10.0 * x_scaled**2))
        
        # Adaptive conditioning with dimension-dependent stiffness
        condition_factors = np.exp(0.5 * np.abs(x_scaled)) * (1.0 + 0.3 * np.sin(3.0 * x_scaled))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_interaction = np.sum((x_scaled[:-1]**2 + 0.5 * x_scaled[1:]**2) * 
                                 np.sin(4.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                                 0.6 * (x_scaled[:-2]**3 - 0.3 * x_scaled[2:]**3) * 
                                 np.cos(2.5 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Nonlinear distortion with polynomial and exponential components
        distortion = np.sum(0.4 * x_scaled**5 + 0.3 * np.exp(-2.0 * np.abs(x_scaled)) + 
                           0.2 * np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled))
        
        # Weighted combination with global minimum shift
        return (0.4 * (peak1 + peak2 + peak3) + 
                0.3 * trig_coupling + 
                0.15 * np.sum(condition_factors) + 
                0.1 * cross_interaction + 
                0.05 * distortion + 
                2.1)
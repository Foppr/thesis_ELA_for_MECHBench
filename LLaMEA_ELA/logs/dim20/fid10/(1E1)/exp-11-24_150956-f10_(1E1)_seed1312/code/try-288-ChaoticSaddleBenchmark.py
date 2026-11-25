import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component with varying r parameters
        logistic = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Spherical harmonics with varying degrees and orders
        sph_harm = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.0 * x_scaled) + 
                         0.7 * np.sin(5.0 * x_scaled**2) * np.cos(4.0 * x_scaled**2) + 
                         0.3 * np.sin(7.0 * x_scaled**3) * np.cos(6.0 * x_scaled**3))
        
        # Asymmetric saddle points with exponential barriers
        saddle = np.sum(np.exp(-x_scaled**2) * (x_scaled**4 - 2.0 * x_scaled**2 + 1.0) + 
                       0.5 * np.exp(-(x_scaled + 0.5)**2) * (x_scaled**3 + x_scaled))
        
        # Multi-scale sinusoidal interference with frequency modulation
        freq_mod = np.sum(np.sin(10.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.6 * np.sin(15.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                         0.4 * np.sin(20.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3))
        
        # Cross-dimensional coupling with asymmetric interaction weights
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                              np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                              0.3 * (x_scaled[:-2]**3 - x_scaled[2:]**3) * 
                              np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric exponential decay with polynomial correction
        decay = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * (1.0 + 0.3 * x_scaled**2) + 
                     0.2 * np.exp(-x_scaled**2) * (x_scaled**4 - x_scaled**2))
        
        # Combine all components with adaptive weights
        return 0.25 * logistic + 0.3 * sph_harm + 0.15 * saddle + 0.2 * freq_mod + 0.08 * cross_coupling + 0.02 * decay + 2.1
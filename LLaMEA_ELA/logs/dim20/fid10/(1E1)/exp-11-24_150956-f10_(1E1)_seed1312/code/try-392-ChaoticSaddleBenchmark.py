import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sinusoidal components with dynamic frequencies
        chaotic_terms = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) * 
                              np.cos(18.0 * np.cos(13.0 * x_scaled)) + 
                              0.7 * np.sin(25.0 * np.tan(12.0 * x_scaled)) * 
                              np.cos(22.0 * np.tanh(14.0 * x_scaled)))
        
        # Asymmetric saddle points with exponential basins
        saddle_terms = np.sum((x_scaled**2 - 0.5 * x_scaled**4) * 
                            np.exp(-0.5 * x_scaled**2) + 
                            0.3 * (x_scaled**3 - 0.8 * x_scaled**5) * 
                            np.exp(-0.3 * x_scaled**2))
        
        # Dynamic conditioning with dimensionally dependent scaling
        cond_terms = np.sum(np.abs(x_scaled)**(1.5 + 0.5 * np.sin(5.0 * x_scaled)) + 
                          0.8 * np.abs(x_scaled)**(2.0 + 0.3 * np.cos(7.0 * x_scaled)))
        
        # Cross-dimensional coupling with polynomial interaction
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                           np.sin(4.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                           0.6 * (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Multi-scale chaotic modulation with time-varying amplitudes
        modulated_terms = np.sum(np.sin(10.0 * x_scaled + 0.5 * np.sin(25.0 * x_scaled)) * 
                               np.cos(8.0 * x_scaled + 0.3 * np.cos(30.0 * x_scaled)) + 
                               0.4 * np.sin(15.0 * x_scaled**2 + 0.6 * np.sin(20.0 * x_scaled**2)) * 
                               np.cos(12.0 * x_scaled**2 + 0.4 * np.cos(25.0 * x_scaled**2)))
        
        # Combine all components with adaptive weights
        return 0.4 * chaotic_terms + 0.3 * saddle_terms + 0.15 * cond_terms + 0.1 * cross_terms + 0.05 * modulated_terms + 2.1
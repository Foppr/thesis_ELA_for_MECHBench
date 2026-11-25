import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13.0 * x_scaled + np.sin(7.0 * x_scaled)) * 
                              np.cos(9.0 * x_scaled + np.cos(5.0 * x_scaled)) + 
                              0.7 * np.sin(17.0 * x_scaled**2 + np.sin(11.0 * x_scaled**2)) * 
                              np.cos(14.0 * x_scaled**2 + np.cos(9.0 * x_scaled**2)))
        
        # Polynomial noise with varying degrees and coefficients
        poly_noise = np.sum(0.5 * x_scaled**4 + 0.3 * x_scaled**3 - 0.8 * x_scaled**2 + 
                          0.2 * x_scaled + 0.1 * np.sin(20.0 * x_scaled))
        
        # Asymmetric basin structure with exponential decay and logarithmic scaling
        basin_terms = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * np.log(1.0 + 3.0 * x_scaled**2) + 
                           0.5 * np.exp(-1.5 * x_scaled**2) * np.sin(8.0 * x_scaled))
        
        # Cross-dimensional coupling with chaotic phase interactions
        cross_coupling = np.sum(np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                               np.cos(3.0 * (x_scaled[:-1] - x_scaled[1:])) * 
                               np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                               0.6 * np.sin(6.0 * (x_scaled[:-2] + x_scaled[2:])) * 
                               np.cos(4.0 * (x_scaled[:-2] - x_scaled[2:])) * 
                               np.exp(-0.3 * (x_scaled[:-2]**2 + x_scaled[2:]**2)))
        
        # Multi-scale chaotic interference with fractal-like behavior
        fractal_terms = np.sum(np.sin(10.0 * x_scaled) * np.cos(15.0 * x_scaled) * 
                              np.sin(25.0 * x_scaled**2) + 
                              0.8 * np.sin(20.0 * x_scaled**3) * np.cos(30.0 * x_scaled**3) * 
                              np.sin(40.0 * x_scaled**4))
        
        # Combine all components with adaptive weighting
        return 0.3 * chaotic_terms + 0.25 * poly_noise + 0.2 * basin_terms + 0.15 * cross_coupling + 0.1 * fractal_terms + 2.1
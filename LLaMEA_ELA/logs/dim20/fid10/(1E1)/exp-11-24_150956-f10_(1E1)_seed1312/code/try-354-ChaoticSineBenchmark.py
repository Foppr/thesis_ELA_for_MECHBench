import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13.0 * x_scaled) * np.cos(17.0 * x_scaled) + 
                             0.7 * np.sin(23.0 * x_scaled**2) * np.cos(29.0 * x_scaled**2) + 
                             0.4 * np.sin(37.0 * x_scaled**3) * np.cos(41.0 * x_scaled**3))
        
        # Polynomial saddle point structure with mixed degrees
        saddle_terms = np.sum(x_scaled**4 - 2.0 * x_scaled**2 + 0.5 * x_scaled**6)
        
        # Cross-dimensional coupling with chaotic interaction coefficients
        cross_coupling = np.sum(np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                              np.cos(7.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                              0.6 * np.sin(9.0 * (x_scaled[:-2]**2 + x_scaled[2:]**2)) * 
                              np.cos(11.0 * (x_scaled[:-2]**2 - x_scaled[2:]**2)))
        
        # Adaptive noise injection based on input magnitude
        noise = 0.1 * np.sum(np.random.randn(self.dim) * (1.0 + 0.5 * np.abs(x_scaled)))
        
        # Asymmetric multimodal structure with exponential modulation
        asymmetry = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * np.sin(3.0 * x_scaled)**2)
        
        # Combined function with weighted components
        return 0.4 * chaotic_terms + 0.3 * saddle_terms + 0.2 * cross_coupling + 0.05 * noise + 0.05 * asymmetry + 2.1
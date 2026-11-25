import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) * 
                              np.cos(18.0 * np.sin(13.0 * x_scaled)) + 
                              0.7 * np.sin(25.0 * np.sin(22.0 * x_scaled**2)) * 
                              np.cos(23.0 * np.sin(21.0 * x_scaled**2)))
        
        # Adaptive Gaussian peaks with dynamic widths and heights
        gaussian_terms = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.4)**2) + 
                              0.4 * np.exp(-3.0 * (x_scaled + 0.6)**2) + 
                              0.3 * np.exp(-7.0 * (x_scaled - 0.9)**2) + 
                              0.2 * np.exp(-2.0 * (x_scaled + 0.8)**2))
        
        # Asymmetric polynomial interactions with cross-dimensional coupling
        poly_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**4) * 
                           np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                           (x_scaled[:-2]**2 * x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Fractional Brownian motion inspired component with varying Hurst parameters
        fbm_like = np.sum(np.sin(10.0 * x_scaled) * np.cos(8.0 * x_scaled) * 
                         np.exp(-0.5 * np.abs(x_scaled)) + 
                         0.5 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) * 
                         np.exp(-0.3 * np.abs(x_scaled**2)))
        
        # Multi-scale chaotic interference with phase modulation
        chaos_interference = np.sum(np.sin(7.0 * x_scaled + 0.5 * np.sin(9.0 * x_scaled)) * 
                                  np.cos(6.0 * x_scaled + 0.3 * np.cos(8.0 * x_scaled)) + 
                                  0.6 * np.sin(11.0 * x_scaled**2 + 0.4 * np.sin(13.0 * x_scaled**2)) * 
                                  np.cos(10.0 * x_scaled**2 + 0.2 * np.cos(12.0 * x_scaled**2)))
        
        # Combine all components with weighted sum
        return 0.4 * chaotic_terms + 0.3 * gaussian_terms + 0.15 * poly_terms + 0.1 * fbm_like + 0.05 * chaos_interference + 1.5
import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(10.0 * np.sin(7.0 * x_scaled)) * 
                              np.cos(9.0 * np.sin(5.0 * x_scaled)) + 
                              0.7 * np.sin(15.0 * np.sin(4.0 * x_scaled**2)) * 
                              np.cos(13.0 * np.sin(6.0 * x_scaled**2)))
        
        # Polynomial noise with adaptive coefficients
        poly_noise = np.sum(0.5 * x_scaled**4 + 0.3 * x_scaled**3 - 0.8 * x_scaled**2 + 
                          0.2 * x_scaled + 1.0 * np.random.rand(self.dim))
        
        # Cross-dimensional coupling with exponential interactions
        cross_coupling = np.sum(np.exp(-2.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                               np.sin(3.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                               np.exp(-1.5 * (x_scaled[:-2]**2 + x_scaled[2:]**2)) * 
                               np.cos(2.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric multimodal peaks with dynamic positioning
        peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.5)**2) * 
                      (1.0 + 0.5 * np.sin(20.0 * x_scaled)) + 
                      0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) * 
                      (1.0 + 0.3 * np.cos(15.0 * x_scaled)))
        
        # Adaptive conditioning with dynamic scaling
        conditioning = np.sum((1.0 + 0.5 * np.sin(8.0 * x_scaled)) * 
                            (x_scaled**2 + 0.1 * np.abs(x_scaled)) + 
                            0.3 * np.cos(6.0 * x_scaled) * x_scaled)
        
        # Final composite function with weighted components
        return 0.4 * chaotic_terms + 0.25 * poly_noise + 0.15 * cross_coupling + \
               0.1 * peaks + 0.1 * conditioning + 1.8
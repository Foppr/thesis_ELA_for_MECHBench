import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13.0 * x_scaled) * np.cos(17.0 * x_scaled) + 
                             0.7 * np.sin(22.0 * x_scaled**2) * np.cos(29.0 * x_scaled**2) + 
                             0.4 * np.sin(37.0 * x_scaled**3) * np.cos(41.0 * x_scaled**3))
        
        # Polynomial coupling with asymmetric exponents
        poly_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**4) * 
                           np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                           (x_scaled[:-2]**2 + x_scaled[2:]**5) * 
                           np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric basin structure with exponential decay
        basins = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * np.sin(8.0 * x_scaled) + 
                      0.5 * np.exp(-1.5 * np.abs(x_scaled)) * np.cos(6.0 * x_scaled))
        
        # Cross-dimensional chaotic interactions with non-linear coupling
        cross_chaos = np.sum(np.sin(4.0 * x_scaled[:-1]) * np.cos(7.0 * x_scaled[1:]) * 
                           np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                           np.sin(6.0 * x_scaled[:-2]) * np.cos(9.0 * x_scaled[2:]) * 
                           np.exp(-0.3 * (x_scaled[:-2]**2 + x_scaled[2:]**2)))
        
        # Multi-scale harmonic modulation with varying phase shifts
        harmonic_mod = np.sum(np.sin(10.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                            0.6 * np.sin(25.0 * x_scaled**2) * np.cos(30.0 * x_scaled**2) + 
                            0.3 * np.sin(40.0 * x_scaled**3) * np.cos(45.0 * x_scaled**3))
        
        # Asymmetric weighting and final composition
        return 0.4 * chaotic_terms + 0.25 * poly_coupling + 0.15 * basins + 0.1 * cross_chaos + 0.1 * harmonic_mod + 2.1
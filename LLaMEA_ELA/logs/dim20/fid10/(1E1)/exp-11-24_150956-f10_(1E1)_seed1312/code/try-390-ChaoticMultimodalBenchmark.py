import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13.0 * x_scaled) * np.cos(17.0 * x_scaled) + 
                             0.7 * np.sin(23.0 * x_scaled**2) * np.cos(29.0 * x_scaled**2) + 
                             0.4 * np.sin(37.0 * x_scaled**3) * np.cos(41.0 * x_scaled**3))
        
        # Polynomial chaos with exponential weighting
        poly_chaos = np.sum((x_scaled**4 + x_scaled**3 + x_scaled**2 + x_scaled) * 
                          np.exp(-0.5 * (x_scaled**2)) + 
                          0.3 * (x_scaled**5 - x_scaled**3) * np.exp(-0.3 * (x_scaled**2)))
        
        # Adaptive conditioning with logistic map-like behavior
        condition_factors = np.sum(1.0 / (1.0 + np.exp(-5.0 * (x_scaled - 0.2))) + 
                                0.8 / (1.0 + np.exp(-4.0 * (x_scaled + 0.3))) + 
                                0.6 / (1.0 + np.exp(-6.0 * (x_scaled - 0.7))))
        
        # Cross-dimensional coupling with chaotic interaction terms
        cross_coupling = np.sum(np.sin(2.0 * x_scaled[:-1]) * np.cos(3.0 * x_scaled[1:]) + 
                             0.5 * np.sin(4.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) + 
                             0.3 * np.cos(5.0 * (x_scaled[:-2] * x_scaled[2:])))
        
        # Asymmetric multimodal structure with exponential modulation
        asym_mod = np.sum(np.exp(-2.0 * (x_scaled - 0.1)**2) * np.sin(10.0 * x_scaled) + 
                        0.5 * np.exp(-3.0 * (x_scaled + 0.4)**2) * np.cos(15.0 * x_scaled) + 
                        0.2 * np.exp(-4.0 * (x_scaled - 0.8)**2) * np.sin(20.0 * x_scaled))
        
        # Combined objective with weighted components
        return 0.4 * chaotic_terms + 0.3 * poly_chaos + 0.15 * condition_factors + 0.1 * cross_coupling + 0.05 * asym_mod + 2.1
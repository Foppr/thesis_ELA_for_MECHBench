import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Time-delayed chaotic sinusoidal components
        delayed_sine = np.sum(np.sin(10.0 * x_scaled) * np.cos(8.0 * x_scaled) * 
                             np.exp(-0.5 * (x_scaled - 0.2)**2) + 
                             np.sin(15.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) * 
                             np.exp(-0.3 * (x_scaled + 0.3)**2))
        
        # Polynomial chaos interactions with varying degrees
        poly_chaos = np.sum((x_scaled**4 + x_scaled**3 + x_scaled**2) * 
                           np.sin(5.0 * x_scaled) + 
                           (x_scaled**5 - x_scaled**3 + x_scaled) * 
                           np.cos(4.0 * x_scaled))
        
        # Asymmetric basin structures with exponential weighting
        basins = np.sum(np.exp(-2.0 * (x_scaled - 0.1)**2) * np.sin(6.0 * x_scaled) + 
                       np.exp(-1.5 * (x_scaled + 0.4)**2) * np.cos(7.0 * x_scaled))
        
        # Cross-dimensional coupling with delayed feedback
        feedback_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                                 np.sin(3.0 * (x_scaled[:-1] - 0.5 * x_scaled[1:])) + 
                                 (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                                 np.cos(2.0 * (x_scaled[:-2] + 0.3 * x_scaled[2:])))
        
        # Multi-scale chaotic modulation with phase shifts
        chaotic_mod = np.sum(np.sin(9.0 * x_scaled) * np.cos(11.0 * x_scaled) * 
                           np.exp(-0.7 * np.abs(x_scaled)) + 
                           0.7 * np.sin(14.0 * x_scaled**2) * np.cos(16.0 * x_scaled**2) * 
                           np.exp(-0.4 * np.abs(x_scaled**2)))
        
        # Asymmetric weighted sum with chaotic bias
        return 0.3 * delayed_sine + 0.25 * poly_chaos + 0.2 * basins + 0.15 * feedback_coupling + 0.1 * chaotic_mod + 2.1
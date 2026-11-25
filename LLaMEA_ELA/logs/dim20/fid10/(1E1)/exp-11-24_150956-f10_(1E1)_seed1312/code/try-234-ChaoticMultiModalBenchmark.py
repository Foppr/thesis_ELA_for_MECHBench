import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian_terms = np.sum(0.7 * np.exp(-3.0 * (x_scaled - 0.2)**2) + 
                               0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) + 
                               0.3 * np.exp(-2.0 * (x_scaled - 0.7)**2) + 
                               0.2 * np.exp(-4.0 * (x_scaled + 0.8)**2))
        
        # Chaotic sine-wave modulation with logistic map-like behavior
        chaotic_sin = np.sum(np.sin(15.0 * x_scaled * np.sin(10.0 * x_scaled)) + 
                            0.6 * np.sin(20.0 * x_scaled**2 * np.cos(15.0 * x_scaled)) + 
                            0.4 * np.sin(25.0 * x_scaled**3 * np.sin(20.0 * x_scaled)))
        
        # Adaptive polynomial cross-terms with exponential weights
        poly_cross = np.sum(np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                           (x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])))
        
        # Asymmetric cubic interactions with phase shifts
        cubic_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.cos(3.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           0.5 * (x_scaled[:-2]**4 - x_scaled[2:]**4) * 
                           np.sin(2.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with varying amplitudes
        harmonic_terms = np.sum(np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                               0.7 * np.sin(14.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                               0.3 * np.sin(22.0 * x_scaled**3) * np.cos(26.0 * x_scaled**3))
        
        # Combine all components with weighted sum and add constant offset
        return 0.4 * gaussian_terms + 0.3 * chaotic_sin + 0.15 * poly_cross + 0.1 * cubic_terms + 0.05 * harmonic_terms + 2.1
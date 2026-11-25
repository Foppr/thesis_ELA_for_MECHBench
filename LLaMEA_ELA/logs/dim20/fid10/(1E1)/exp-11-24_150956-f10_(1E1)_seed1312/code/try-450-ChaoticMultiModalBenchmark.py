import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dimensionality
        self.chaotic_seq = np.array([np.log(4 * (i + 1) * (1 - (i + 1) / self.dim)) for i in range(self.dim)])
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Logistic map chaotic component
        logistic = np.sum(np.log(4 * np.abs(x_scaled * (1 - x_scaled))) + 
                         0.5 * np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = np.sum(np.sin(10 * x_scaled**2) * np.cos(7 * x_scaled) + 
                             0.7 * np.sin(15 * x_scaled**3) * np.cos(12 * x_scaled**2))
        
        # Adaptive conditioning based on chaotic sequence
        condition = np.sum((x_scaled**2 + 0.1) * np.exp(-self.chaotic_seq * np.abs(x_scaled)))
        
        # Cross-dimensional polynomial interactions with chaotic weights
        cross_poly = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(5 * (x_scaled[:-1] + x_scaled[1:])) * 
                           self.chaotic_seq[:-1])
        
        # Multi-scale harmonic interference with dynamic phase
        harmonics = np.sum(np.sin(8 * x_scaled) * np.cos(9 * x_scaled) + 
                         0.6 * np.sin(13 * x_scaled**2) * np.cos(14 * x_scaled**2) + 
                         0.3 * np.sin(20 * x_scaled**3) * np.cos(21 * x_scaled**3))
        
        # Asymmetric exponential modulation
        asym_exp = np.sum(np.exp(-2 * np.abs(x_scaled)) * (1 + 0.5 * np.sin(6 * x_scaled)))
        
        # Final combination with chaotic weighting
        return 0.4 * logistic + 0.25 * trig_coupling + 0.15 * condition + \
               0.1 * cross_poly + 0.08 * harmonics + 0.02 * asym_exp + 2.1
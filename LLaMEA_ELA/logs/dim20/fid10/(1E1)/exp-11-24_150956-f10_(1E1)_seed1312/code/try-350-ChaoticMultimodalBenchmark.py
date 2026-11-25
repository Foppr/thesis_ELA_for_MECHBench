import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with chaotic height variations
        peak1 = 0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * (1.0 + 0.3 * np.sin(15.0 * x_scaled))
        peak2 = 0.5 * np.exp(-5.0 * (x_scaled + 0.3)**2) * (1.0 + 0.4 * np.cos(12.0 * x_scaled))
        peak3 = 0.3 * np.exp(-2.0 * (x_scaled - 0.7)**2) * (1.0 + 0.2 * np.sin(20.0 * x_scaled))
        peak4 = 0.6 * np.exp(-4.0 * (x_scaled + 0.8)**2) * (1.0 + 0.35 * np.cos(18.0 * x_scaled))
        
        # Chaotic sinusoidal modulation with fractional frequencies
        chaotic_mod = np.sum(np.sin(7.0 * x_scaled + np.sin(3.0 * x_scaled)) * 
                           np.cos(5.0 * x_scaled + np.cos(2.0 * x_scaled)) + 
                           0.5 * np.sin(9.0 * x_scaled**1.5 + np.sin(4.0 * x_scaled**1.5)) * 
                           np.cos(6.0 * x_scaled**1.5 + np.cos(3.0 * x_scaled**1.5)))
        
        # Adaptive dimensional coupling with exponential decay
        coupling = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                         (1.0 + 0.5 * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled)))
        
        # Cross-dimensional chaotic interactions with polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           0.3 * np.sin(5.0 * x_scaled[:-1] * x_scaled[1:]) * 
                           np.cos(4.0 * x_scaled[:-1] * x_scaled[1:]))
        
        # Multi-scale chaotic interference with phase shifts
        chaotic_harmonics = np.sum(np.sin(6.0 * x_scaled + 0.5 * np.sin(8.0 * x_scaled)) * 
                                np.cos(4.0 * x_scaled + 0.3 * np.cos(7.0 * x_scaled)) + 
                                0.7 * np.sin(10.0 * x_scaled**2 + 0.4 * np.sin(9.0 * x_scaled**2)) * 
                                np.cos(8.0 * x_scaled**2 + 0.3 * np.cos(6.0 * x_scaled**2)))
        
        # Asymmetric landscape with weighted sum of components
        return 0.4 * (peak1 + peak2 + peak3 + peak4) + 0.3 * chaotic_mod + 0.15 * coupling + 0.1 * cross_terms + 0.05 * chaotic_harmonics + 1.8
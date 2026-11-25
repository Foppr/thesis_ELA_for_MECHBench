import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with varying heights and widths
        gaussian_peaks = np.sum(0.7 * np.exp(-3.0 * (x_scaled - 0.2)**2) + 
                               0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) + 
                               0.2 * np.exp(-2.0 * (x_scaled - 0.8)**2) + 
                               0.3 * np.exp(-4.0 * (x_scaled + 0.9)**2))
        
        # Chaotic sine-wave interactions with frequency modulation
        chaotic_sine = np.sum(np.sin(15.0 * x_scaled + np.sin(7.0 * x_scaled)) + 
                             0.6 * np.sin(20.0 * x_scaled**2 + np.sin(10.0 * x_scaled**2)) + 
                             0.4 * np.sin(25.0 * x_scaled**3 + np.sin(12.0 * x_scaled**3)))
        
        # Adaptive polynomial coupling with exponential decay
        poly_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                              np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                              (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                              np.exp(-0.3 * (x_scaled[:-2] + x_scaled[2:])**2))
        
        # Asymmetric cross-dimensional interactions with logistic maps
        logistic_interaction = np.sum(0.5 * x_scaled[:-1] * (1 - x_scaled[:-1]) * 
                                    np.sin(8.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                                    0.3 * x_scaled[:-2] * (1 - x_scaled[:-2]) * 
                                    np.cos(6.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonic_interference = np.sum(np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                                     0.7 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                                     0.5 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.3 * gaussian_peaks + 0.3 * chaotic_sine + 0.15 * poly_coupling + 0.15 * logistic_interaction + 0.1 * harmonic_interference + 1.8
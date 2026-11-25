import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic Gaussian peaks with dynamic heights and widths
        peaks = np.sum(1.2 * np.exp(-8.0 * (x_scaled - 0.2)**2) + 
                      0.8 * np.exp(-5.0 * (x_scaled + 0.5)**2) + 
                      0.6 * np.exp(-12.0 * (x_scaled - 0.7)**2) + 
                      0.4 * np.exp(-3.0 * (x_scaled + 0.9)**2) + 
                      0.3 * np.exp(-15.0 * (x_scaled - 0.1)**2))
        
        # Chaotic sinusoidal modulation with fractional frequencies and phase shifts
        sin_mod = np.sum(np.sin(20.0 * x_scaled + np.sin(7.0 * x_scaled)) * 
                        np.cos(15.0 * x_scaled + np.cos(9.0 * x_scaled)) + 
                        0.7 * np.sin(25.0 * x_scaled**1.5 + np.sin(12.0 * x_scaled**1.5)) * 
                        np.cos(20.0 * x_scaled**1.5 + np.cos(14.0 * x_scaled**1.5)) + 
                        0.5 * np.sin(30.0 * x_scaled**2.5 + np.sin(18.0 * x_scaled**2.5)) * 
                        np.cos(25.0 * x_scaled**2.5 + np.cos(22.0 * x_scaled**2.5)))
        
        # Adaptive dimensionality scaling with chaotic decay
        dim_scaling = np.sum(np.exp(-1.2 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled)))
        
        # Cross-dimensional interaction terms with chaotic coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(4.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**4 + x_scaled[3:]**4) * 
                           np.sin(3.0 * (x_scaled[:-3] + x_scaled[3:]))
                          )
        
        # Multi-scale harmonic interference with chaotic phase shifts
        harmonics = np.sum(np.sin(8.0 * x_scaled + 0.5 * np.sin(12.0 * x_scaled)) * 
                         np.cos(10.0 * x_scaled + 0.3 * np.cos(14.0 * x_scaled)) + 
                         0.9 * np.sin(14.0 * x_scaled**2 + 0.6 * np.sin(18.0 * x_scaled**2)) * 
                         np.cos(16.0 * x_scaled**2 + 0.4 * np.cos(20.0 * x_scaled**2)) + 
                         0.7 * np.sin(20.0 * x_scaled**3 + 0.8 * np.sin(24.0 * x_scaled**3)) * 
                         np.cos(22.0 * x_scaled**3 + 0.5 * np.cos(26.0 * x_scaled**3)))
        
        # Asymmetric chaotic landscape with weighted sum of components
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
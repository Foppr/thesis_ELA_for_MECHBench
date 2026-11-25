import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic Gaussian peaks with dynamic widths and heights
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.4 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.3 * np.exp(-7.0 * (x_scaled - 0.9)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.8)**2) + 
                      0.1 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Hyper-chaotic sinusoidal modulation with fractional frequencies
        sin_mod = np.sum(np.sin(20.0 * x_scaled) * np.cos(18.0 * x_scaled) + 
                        0.7 * np.sin(25.0 * x_scaled**1.5) * np.cos(22.0 * x_scaled**1.5) + 
                        0.5 * np.sin(30.0 * x_scaled**2.5) * np.cos(28.0 * x_scaled**2.5) + 
                        0.3 * np.sin(35.0 * x_scaled**3.5) * np.cos(32.0 * x_scaled**3.5))
        
        # Adaptive dimensionality scaling with logistic map behavior
        dim_scaling = np.sum(1.0 / (1.0 + np.exp(-3.0 * x_scaled)) * (1.0 + 0.5 * np.sin(6.0 * x_scaled)))
        
        # Complex cross-dimensional interaction terms with exponential coupling
        cross_terms = np.sum(np.exp(-2.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           np.exp(-1.5 * (x_scaled[:-2]**3 + x_scaled[2:]**3)) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with time-varying phase shifts
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                         0.7 * np.sin(14.0 * x_scaled**3) * np.cos(16.0 * x_scaled**3) + 
                         0.5 * np.sin(18.0 * x_scaled**4) * np.cos(20.0 * x_scaled**4))
        
        # Asymmetric landscape with weighted sum of components and dynamic bias
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
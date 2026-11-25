import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic Gaussian peaks with dynamic heights and widths
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.3 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.2 * np.exp(-7.0 * (x_scaled - 0.9)**2) + 
                      0.1 * np.exp(-2.0 * (x_scaled + 0.8)**2) +
                      0.15 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Nested sinusoidal modulations with chaotic frequencies
        sin_mod = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                        0.7 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) + 
                        0.5 * np.sin(30.0 * x_scaled**3) * np.cos(28.0 * x_scaled**3) +
                        0.3 * np.sin(35.0 * x_scaled**4) * np.cos(32.0 * x_scaled**4))
        
        # Exponentially weighted dimensionality scaling with chaotic phase shifts
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled) + 
                           0.3 * np.cos(7.0 * x_scaled)))
        
        # Chaotic cross-dimensional interaction terms with fractional coupling
        cross_terms = np.sum((x_scaled[:-1]**2.5 + x_scaled[1:]**2.5) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3.5 + x_scaled[2:]**3.5) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**4.0 + x_scaled[3:]**4.0) * 
                           np.sin(2.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Nested harmonic interference with variable phase shifts
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.7 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3) +
                         0.5 * np.sin(24.0 * x_scaled**4) * np.cos(26.0 * x_scaled**4))
        
        # Asymmetric chaotic landscape with weighted sum of components
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
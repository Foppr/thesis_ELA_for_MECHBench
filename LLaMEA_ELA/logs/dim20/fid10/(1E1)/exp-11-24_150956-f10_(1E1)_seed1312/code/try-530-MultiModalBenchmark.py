import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with modified positions and heights
        peaks = np.sum(0.7 * np.exp(-3.5 * (x_scaled - 0.2)**2) + 
                      0.3 * np.exp(-2.0 * (x_scaled + 0.5)**2) + 
                      0.18 * np.exp(-5.5 * (x_scaled - 0.7)**2) + 
                      0.12 * np.exp(-1.8 * (x_scaled + 0.8)**2))
        
        # Sinusoidal modulation with altered frequencies and amplitudes
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(28.0 * x_scaled**3) * np.cos(24.0 * x_scaled**3))
        
        # Adaptive dimensionality scaling with modified exponential decay
        dim_scaling = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled)))
        
        # Cross-dimensional interaction terms with different polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.5 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                         0.6 * np.sin(16.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.38 * peaks + 0.32 * sin_mod + 0.13 * dim_scaling + 0.11 * cross_terms + 0.06 * harmonics + 1.55
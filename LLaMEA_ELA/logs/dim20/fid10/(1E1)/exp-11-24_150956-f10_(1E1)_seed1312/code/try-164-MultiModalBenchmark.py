import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peaks with chaotic amplitude variations
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.3)**2) * 
                      (1.0 + 0.3 * np.sin(20.0 * x_scaled)) +
                      0.3 * np.exp(-3.0 * (x_scaled + 0.4)**2) * 
                      (1.0 + 0.2 * np.cos(15.0 * x_scaled)) +
                      0.2 * np.exp(-7.0 * (x_scaled - 0.8)**2) * 
                      (1.0 + 0.4 * np.sin(25.0 * x_scaled)) +
                      0.15 * np.exp(-2.0 * (x_scaled + 0.9)**2) * 
                      (1.0 + 0.25 * np.cos(18.0 * x_scaled)))
        
        # Chaotic sinusoidal modulation with fractional frequencies
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(22.0 * x_scaled**1.5) * np.cos(18.0 * x_scaled**1.5) + 
                        0.5 * np.sin(30.0 * x_scaled**2.5) * np.cos(25.0 * x_scaled**2.5) +
                        0.3 * np.sin(35.0 * np.sqrt(np.abs(x_scaled))) * np.cos(30.0 * np.sqrt(np.abs(x_scaled))))
        
        # Enhanced dimensionality scaling with chaotic decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * 
                           (1.0 + 0.5 * np.sin(6.0 * x_scaled) * np.cos(4.0 * x_scaled)))
        
        # Complex cross-dimensional interaction terms with higher-order couplings
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**2 + x_scaled[3:]**2) * 
                           np.sin(5.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Multi-scale chaotic interference with phase coupling
        harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(10.0 * x_scaled) + 
                         0.9 * np.sin(13.0 * x_scaled**2) * np.cos(16.0 * x_scaled**2) + 
                         0.6 * np.sin(20.0 * x_scaled**3) * np.cos(23.0 * x_scaled**3) +
                         0.4 * np.sin(25.0 * np.sqrt(np.abs(x_scaled))) * np.cos(28.0 * np.sqrt(np.abs(x_scaled))))
        
        # Asymmetric landscape with chaotic weighting
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
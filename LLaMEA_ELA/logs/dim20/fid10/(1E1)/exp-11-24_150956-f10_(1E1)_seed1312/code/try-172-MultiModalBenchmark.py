import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with variable heights, widths, and positions
        peaks = np.sum(1.2 * np.exp(-8.0 * (x_scaled - 0.3)**2) + 
                      0.8 * np.exp(-5.0 * (x_scaled + 0.4)**2) + 
                      0.6 * np.exp(-10.0 * (x_scaled - 0.8)**2) + 
                      0.4 * np.exp(-3.0 * (x_scaled + 0.9)**2) +
                      0.3 * np.exp(-12.0 * (x_scaled - 0.1)**2) + 
                      0.2 * np.exp(-7.0 * (x_scaled + 0.6)**2))
        
        # Intensified sinusoidal modulation with higher frequencies and amplitudes
        sin_mod = np.sum(1.5 * np.sin(20.0 * x_scaled) * np.cos(18.0 * x_scaled) + 
                        1.2 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) + 
                        0.9 * np.sin(30.0 * x_scaled**3) * np.cos(28.0 * x_scaled**3) +
                        0.7 * np.sin(35.0 * x_scaled**4) * np.cos(32.0 * x_scaled**4))
        
        # Enhanced dimensionality scaling with exponential decay and additional harmonic terms
        dim_scaling = np.sum(np.exp(-1.2 * np.abs(x_scaled)) * (1.0 + 0.8 * np.sin(6.0 * x_scaled) + 
                           0.4 * np.cos(4.0 * x_scaled)))
        
        # Augmented cross-dimensional interaction terms with higher-order polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**2 + x_scaled[3:]**2) * 
                           np.sin(4.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Novel harmonic interference patterns with phase shifts and complex coupling
        harmonics = np.sum(1.8 * np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                         1.4 * np.sin(15.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                         1.1 * np.sin(22.0 * x_scaled**3) * np.cos(25.0 * x_scaled**3) +
                         0.9 * np.sin(28.0 * x_scaled**4) * np.cos(30.0 * x_scaled**4))
        
        # Additional asymmetric landscape features with weighted sum of components
        return 0.4 * peaks + 0.35 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
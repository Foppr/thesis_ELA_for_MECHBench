import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peaks with fractal-like height variations
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.35 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.25 * np.exp(-7.0 * (x_scaled - 0.7)**2) + 
                      0.18 * np.exp(-2.0 * (x_scaled + 0.9)**2) +
                      0.12 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Complex sinusoidal modulation with chaotic frequency ratios
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled) + 
                        0.7 * np.sin(22.0 * x_scaled**2) * np.cos(19.0 * x_scaled**2) + 
                        0.5 * np.sin(30.0 * x_scaled**3) * np.cos(27.0 * x_scaled**3) +
                        0.3 * np.sin(25.0 * x_scaled**4) * np.cos(23.0 * x_scaled**4))
        
        # Multi-scale exponential decay with chaotic phase shifts
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(5.0 * x_scaled) + 
                           0.3 * np.cos(7.0 * x_scaled)))
        
        # Novel cross-dimensional interaction with trigonometric coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**4 + x_scaled[3:]**4) * 
                           np.sin(2.5 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Higher-order harmonic interference with non-linear coupling
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.6 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3) +
                         0.4 * np.sin(24.0 * x_scaled**4) * np.cos(26.0 * x_scaled**4))
        
        # Asymmetric landscape with adaptive weighting and chaotic perturbations
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
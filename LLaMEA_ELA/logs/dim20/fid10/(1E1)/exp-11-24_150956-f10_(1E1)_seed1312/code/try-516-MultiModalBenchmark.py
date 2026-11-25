import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian peak components with perturbed positions and heights
        peaks = np.sum(0.7 * np.exp(-3.8 * (x_scaled - 0.25)**2) + 
                      0.3 * np.exp(-2.2 * (x_scaled + 0.35)**2) + 
                      0.18 * np.exp(-5.8 * (x_scaled - 0.75)**2) + 
                      0.12 * np.exp(-1.3 * (x_scaled + 0.85)**2))
        
        # Chaotic sinusoidal modulation with fractional frequencies
        sin_mod = np.sum(np.sin(13.5 * x_scaled) * np.cos(9.5 * x_scaled) + 
                        0.7 * np.sin(19.2 * x_scaled**1.5) * np.cos(14.8 * x_scaled**1.5) + 
                        0.5 * np.sin(26.3 * x_scaled**2.5) * np.cos(21.7 * x_scaled**2.5))
        
        # Dimensionality scaling with chaotic exponential decay
        dim_scaling = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(4.5 * x_scaled)))
        
        # Enhanced cross-dimensional interaction terms with cubic coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(3.5 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(2.5 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase shifts and chaos
        harmonics = np.sum(np.sin(5.5 * x_scaled) * np.cos(6.8 * x_scaled) + 
                         0.85 * np.sin(9.7 * x_scaled**2) * np.cos(11.3 * x_scaled**2) + 
                         0.55 * np.sin(14.8 * x_scaled**3) * np.cos(16.9 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.37 * peaks + 0.33 * sin_mod + 0.11 * dim_scaling + 0.11 * cross_terms + 0.08 * harmonics + 1.55
import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with chaotic height variations
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.35 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.25 * np.exp(-7.0 * (x_scaled - 0.9)**2) + 
                      0.18 * np.exp(-2.0 * (x_scaled + 0.8)**2) + 
                      0.12 * np.exp(-4.5 * (x_scaled - 0.1)**2))
        
        # Chaotic sinusoidal modulation with fractal-like frequencies
        sin_mod = np.sum(np.sin(20.0 * x_scaled + np.sin(15.0 * x_scaled)) * 
                        np.cos(18.0 * x_scaled + np.cos(13.0 * x_scaled)) + 
                        0.7 * np.sin(25.0 * x_scaled**2 + np.sin(22.0 * x_scaled**2)) * 
                        np.cos(23.0 * x_scaled**2 + np.cos(20.0 * x_scaled**2)) + 
                        0.5 * np.sin(30.0 * x_scaled**3 + np.sin(27.0 * x_scaled**3)) * 
                        np.cos(28.0 * x_scaled**3 + np.cos(25.0 * x_scaled**3)))
        
        # Dynamic dimensionality scaling with chaotic decay
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * 
                           (1.0 + 0.6 * np.sin(5.0 * x_scaled) * np.cos(4.0 * x_scaled)))
        
        # Non-linear cross-dimensional interaction terms with chaotic coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           np.sin(6.0 * (x_scaled[:-1] * x_scaled[1:])) * 
                           np.cos(5.0 * (x_scaled[:-2] * x_scaled[2:])))
        
        # Multi-scale harmonic interference with dynamic phase shifts
        harmonics = np.sum(np.sin(8.0 * x_scaled + 0.3 * np.sin(12.0 * x_scaled)) * 
                         np.cos(10.0 * x_scaled + 0.4 * np.cos(15.0 * x_scaled)) + 
                         0.9 * np.sin(12.0 * x_scaled**2 + 0.5 * np.sin(18.0 * x_scaled**2)) * 
                         np.cos(14.0 * x_scaled**2 + 0.6 * np.cos(20.0 * x_scaled**2)) + 
                         0.7 * np.sin(16.0 * x_scaled**3 + 0.8 * np.sin(24.0 * x_scaled**3)) * 
                         np.cos(18.0 * x_scaled**3 + 0.9 * np.cos(27.0 * x_scaled**3)))
        
        # Asymmetric landscape with chaotic weighted sum of components
        return 0.4 * peaks + 0.35 * sin_mod + 0.15 * dim_scaling + 0.08 * cross_terms + 0.07 * harmonics + 2.1
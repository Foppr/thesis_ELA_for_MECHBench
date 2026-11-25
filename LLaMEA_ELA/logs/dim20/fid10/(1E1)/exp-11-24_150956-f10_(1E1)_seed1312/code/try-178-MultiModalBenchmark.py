import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-density Gaussian peaks with chaotic amplitude variations
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.6 * np.exp(-3.0 * (x_scaled + 0.3)**2) + 
                      0.4 * np.exp(-7.0 * (x_scaled - 0.6)**2) + 
                      0.3 * np.exp(-4.0 * (x_scaled + 0.8)**2) +
                      0.5 * np.exp(-6.0 * (x_scaled - 0.9)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.1)**2))
        
        # Chaotic sinusoidal modulation with logistic map scaling
        chaotic_sin = np.sum(np.sin(20.0 * x_scaled) * np.cos(18.0 * x_scaled) + 
                           0.7 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) + 
                           0.5 * np.sin(30.0 * x_scaled**3) * np.cos(28.0 * x_scaled**3) +
                           0.3 * np.sin(35.0 * np.sin(10.0 * x_scaled)) * np.cos(32.0 * np.sin(8.0 * x_scaled)))
        
        # Exponentially decaying dimensionality with chaotic phase shifts
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(5.0 * x_scaled) * np.cos(4.0 * x_scaled)))
        
        # Enhanced cross-dimensional interaction with fractional polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2.5 + x_scaled[1:]**2.5) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3.5 + x_scaled[2:]**3.5) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           0.5 * (x_scaled[:-1]**1.5 + x_scaled[1:]**1.5) * 
                           np.sin(6.0 * (x_scaled[:-1] - x_scaled[1:])) )
        
        # Multi-scale chaotic harmonics with time-varying frequencies
        harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                         0.9 * np.sin(15.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                         0.7 * np.sin(22.0 * x_scaled**3) * np.cos(25.0 * x_scaled**3) +
                         0.4 * np.sin(30.0 * np.tan(5.0 * x_scaled)) * np.cos(35.0 * np.tan(4.0 * x_scaled)))
        
        # Asymmetric landscape with chaotic weighting and additional noise
        return 0.4 * peaks + 0.3 * chaotic_sin + 0.15 * dim_scaling + 0.12 * cross_terms + 0.05 * harmonics + 2.1
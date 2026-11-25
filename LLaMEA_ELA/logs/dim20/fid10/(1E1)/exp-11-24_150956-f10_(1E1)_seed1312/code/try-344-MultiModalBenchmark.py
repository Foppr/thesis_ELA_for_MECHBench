import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-frequency chaotic Gaussian peaks with dynamic heights
        peaks = np.sum(0.8 * np.exp(-8.0 * (x_scaled - 0.2)**2) + 
                      0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) + 
                      0.3 * np.exp(-10.0 * (x_scaled - 0.7)**2) + 
                      0.2 * np.exp(-3.0 * (x_scaled + 0.9)**2) +
                      0.1 * np.exp(-15.0 * (x_scaled - 0.1)**2))
        
        # Nested harmonic sinusoidal modulations with fractal-like behavior
        sin_mod = np.sum(np.sin(20.0 * x_scaled) * np.cos(18.0 * x_scaled) + 
                        0.7 * np.sin(30.0 * x_scaled**2) * np.cos(25.0 * x_scaled**2) + 
                        0.5 * np.sin(40.0 * x_scaled**3) * np.cos(35.0 * x_scaled**3) +
                        0.3 * np.sin(50.0 * x_scaled**4) * np.cos(45.0 * x_scaled**4))
        
        # Exponentially decaying dimensionality with chaotic phase shifts
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * 
                           (1.0 + 0.6 * np.sin(6.0 * x_scaled) * np.cos(5.0 * x_scaled)))
        
        # Complex cross-dimensional interaction terms with chaotic coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                           np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**4 + x_scaled[3:]**4) * 
                           np.sin(4.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Multi-scale chaotic interference with asymmetric harmonic mixing
        harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                         0.9 * np.sin(15.0 * x_scaled**2) * np.cos(20.0 * x_scaled**2) + 
                         0.7 * np.sin(25.0 * x_scaled**3) * np.cos(30.0 * x_scaled**3) +
                         0.5 * np.sin(35.0 * x_scaled**4) * np.cos(40.0 * x_scaled**4))
        
        # Asymmetric chaotic landscape with dynamic weighting
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 2.1
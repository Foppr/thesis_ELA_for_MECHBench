import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponentially decaying Gaussian peaks with varying heights and widths
        peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) + 
                      0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) + 
                      0.2 * np.exp(-7.0 * (x_scaled - 0.6)**2) + 
                      0.1 * np.exp(-9.0 * (x_scaled + 0.8)**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(25.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3))
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Exponentially decaying harmonic interference
        harmonics = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                         (np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                          0.6 * np.sin(10.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                          0.3 * np.sin(15.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3)))
        
        # Asymmetric landscape with weighted sum of components
        return 0.4 * peaks + 0.3 * sin_mod + 0.2 * cross_terms + 0.1 * harmonics + 1.5
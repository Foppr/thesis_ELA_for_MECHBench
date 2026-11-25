import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponentially decaying Gaussian peaks with varying amplitudes and widths
        peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) + 
                      0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) + 
                      0.2 * np.exp(-7.0 * (x_scaled - 0.7)**2) + 
                      0.1 * np.exp(-9.0 * (x_scaled + 0.8)**2))
        
        # Trigonometric wave interference with varying frequencies and amplitudes
        waves = np.sum(np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(25.0 * x_scaled**3) * np.cos(23.0 * x_scaled**3))
        
        # Cross-dimensional coupling with polynomial interactions
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Exponential decay with sinusoidal modulation
        decay_mod = np.sum(np.exp(-1.5 * np.abs(x_scaled)) * 
                          (1.0 + 0.5 * np.sin(6.0 * x_scaled) + 0.3 * np.cos(8.0 * x_scaled)))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(10.0 * x_scaled) + 
                         0.6 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.4 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.3 * peaks + 0.25 * waves + 0.2 * cross_terms + 0.15 * decay_mod + 0.1 * harmonics + 1.5
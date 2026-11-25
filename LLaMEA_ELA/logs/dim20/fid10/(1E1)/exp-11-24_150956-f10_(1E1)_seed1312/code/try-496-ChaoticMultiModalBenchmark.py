import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with time-delayed feedback
        chaotic_terms = np.sum(np.sin(10.0 * x_scaled + 0.5 * np.roll(x_scaled, 1)) * 
                              np.cos(8.0 * x_scaled - 0.3 * np.roll(x_scaled, 2)) + 
                              0.7 * np.sin(15.0 * x_scaled**2 + 0.4 * np.roll(x_scaled, 1)**2) * 
                              np.cos(12.0 * x_scaled**2 - 0.2 * np.roll(x_scaled, 2)**2))
        
        # Exponentially decaying cross-dimensional interactions
        decay_factor = np.exp(-0.5 * np.abs(x_scaled))
        cross_decay = np.sum(decay_factor[:-1] * decay_factor[1:] * 
                           (x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])))
        
        # Multi-scale harmonic interference with phase shifts
        harmonics = np.sum(np.sin(7.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                         0.6 * np.sin(13.0 * x_scaled**2) * np.cos(17.0 * x_scaled**2) + 
                         0.4 * np.sin(21.0 * x_scaled**3) * np.cos(25.0 * x_scaled**3))
        
        # Asymmetric Gaussian peaks with dynamic widths
        gaussian_peaks = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.4)**2) + 
                               0.5 * np.exp(-5.0 * (x_scaled + 0.6)**2) + 
                               0.3 * np.exp(-7.0 * (x_scaled - 0.9)**2))
        
        # Non-smooth discontinuous components
        discontinuous = np.sum(np.abs(x_scaled) * np.sin(10.0 * x_scaled) + 
                             0.5 * np.abs(x_scaled**2) * np.cos(8.0 * x_scaled))
        
        # Combined chaotic landscape with weighted sum
        return 0.4 * chaotic_terms + 0.25 * cross_decay + 0.2 * harmonics + 0.1 * gaussian_peaks + 0.05 * discontinuous + 2.1
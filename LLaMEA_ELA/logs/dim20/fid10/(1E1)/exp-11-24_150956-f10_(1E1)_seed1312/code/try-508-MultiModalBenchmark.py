import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussians = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * 
                          (1.0 + 0.3 * np.sin(5.0 * x_scaled)) +
                          0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) * 
                          (1.0 + 0.2 * np.cos(7.0 * x_scaled)) +
                          0.3 * np.exp(-2.0 * (x_scaled - 0.8)**2) * 
                          (1.0 + 0.4 * np.sin(9.0 * x_scaled)))
        
        # Exponentially decaying sinusoidal waves with varying frequencies
        exp_sinusoids = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                              (np.sin(8.0 * x_scaled) + 0.5 * np.cos(12.0 * x_scaled)) +
                              np.exp(-1.5 * np.abs(x_scaled**2)) * 
                              (0.7 * np.sin(10.0 * x_scaled**2) + 0.3 * np.cos(15.0 * x_scaled**2)))
        
        # Polynomial cross-dimensional interactions with asymmetric coupling
        poly_cross = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) +
                           (x_scaled[:-2]**2 * x_scaled[2:] + x_scaled[:-2] * x_scaled[2:]**2) * 
                           np.sin(4.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric harmonic interference with phase shifts
        harmonics = np.sum(np.exp(-1.0 * np.abs(x_scaled)) * 
                          (np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) +
                           0.6 * np.sin(10.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2)))
        
        # Weighted sum with global offset
        return 0.4 * gaussians + 0.3 * exp_sinusoids + 0.2 * poly_cross + 0.1 * harmonics + 1.8
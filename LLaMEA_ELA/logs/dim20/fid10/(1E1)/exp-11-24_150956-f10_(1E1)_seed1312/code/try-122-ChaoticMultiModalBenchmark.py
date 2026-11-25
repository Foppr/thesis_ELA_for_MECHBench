import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with chaotic heights
        gaussians = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * 
                          (1.0 + 0.3 * np.sin(15.0 * x_scaled)) +
                          0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) * 
                          (1.0 + 0.2 * np.cos(20.0 * x_scaled)) +
                          0.3 * np.exp(-2.0 * (x_scaled - 0.8)**2) * 
                          (1.0 + 0.4 * np.sin(10.0 * x_scaled**2)))
        
        # Chaotic sine-wave interactions with varying frequencies
        chaotic_sines = np.sum(np.sin(25.0 * x_scaled + np.sin(7.0 * x_scaled)) +
                             0.6 * np.sin(30.0 * x_scaled**2 + np.cos(8.0 * x_scaled)) +
                             0.4 * np.sin(18.0 * x_scaled**3 + np.sin(5.0 * x_scaled**2)))
        
        # Polynomial cross-dimensional interactions with exponential weights
        poly_cross = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) +
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.exp(-0.3 * (x_scaled[:-2] + x_scaled[2:])**2))
        
        # Asymmetric harmonic modulation with phase shifts
        harmonics = np.sum(0.7 * np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) +
                         0.5 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) +
                         0.3 * np.sin(16.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3))
        
        # Exponential decay landscape with sinusoidal perturbations
        decay_term = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * 
                           (1.0 + 0.5 * np.sin(12.0 * x_scaled) * np.cos(10.0 * x_scaled)))
        
        # Weighted sum of components with a global offset
        return 0.4 * gaussians + 0.3 * chaotic_sines + 0.15 * poly_cross + 0.1 * harmonics + 0.05 * decay_term + 2.1
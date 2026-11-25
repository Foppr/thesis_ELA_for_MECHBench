import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial exponential decay basins with fractal-like structure
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.7 * np.sin(12 * r) + 0.4 * np.cos(18 * r) + 0.2 * np.sin(25 * r))
        
        # Modified trigonometric wave interference pattern with higher frequencies
        wave_interference = np.sum(np.sin(9 * x_norm) * np.cos(11 * x_norm) * 
                                  np.sin(7 * x_norm) * np.cos(5 * x_norm))
        
        # Enhanced asymmetric polynomial coupling with cubic terms and cross-dimensional interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (x_norm[i]**3 * x_norm[j]**2 + 
                             0.7 * x_norm[i]**2 * x_norm[j]**3 +
                             0.3 * x_norm[i]**4 * x_norm[j])
        
        # Multi-scale sinusoidal modulation with varying amplitudes and phases
        modulated = np.sum(np.sin(15 * x_norm + 0.6) * 
                          np.cos(10 * x_norm - 0.4) * 
                          np.exp(-0.3 * np.abs(x_norm)))
        
        # Enhanced exponential decay with chaotic perturbations and fractal-like structure
        chaotic_perturbation = np.sum(np.exp(-6 * np.abs(x_norm)) * 
                                     np.sin(25 * x_norm + np.cos(12 * x_norm) + 0.1 * np.sin(30 * x_norm)))
        
        # Additional chaotic coupling with higher frequency harmonics and nonlinear interactions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 4) % self.dim
            chaotic_coupling += (np.sin(31 * x_norm[i]) * np.cos(23 * x_norm[j]) * 
                               np.sin(19 * x_norm[k]) * 
                               np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2 + x_norm[k]**2)))
        
        # Fractal basin complexity with multiple nested scales
        fractal_basin = 0.0
        for scale in [2, 4, 8]:
            fractal_basin += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * 
                                  np.exp(-0.1 * r**2) * np.sin(5 * r))
        
        # Combined function with adaptive weights
        return (0.35 * radial_term + 0.25 * wave_interference + 
                0.25 * poly_coupling + 0.1 * modulated + 0.05 * chaotic_perturbation +
                0.05 * chaotic_coupling + 0.05 * fractal_basin)
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial exponential decay basins with multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.5 * np.sin(10 * r) + 0.3 * np.cos(15 * r))
        
        # Trigonometric wave interference pattern with varying frequencies
        wave_interference = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * 
                                  np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Asymmetric polynomial coupling with cross-dimensional interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (x_norm[i]**3 * x_norm[j]**2 + 
                             0.5 * x_norm[i]**2 * x_norm[j]**3)
        
        # Multi-scale sinusoidal modulation with varying amplitudes and phases
        modulated = np.sum(np.sin(12 * x_norm + 0.5) * 
                          np.cos(8 * x_norm - 0.3) * 
                          np.exp(-0.2 * np.abs(x_norm)))
        
        # Exponential decay with chaotic perturbations and fractal-like structure
        chaotic_perturbation = np.sum(np.exp(-5 * np.abs(x_norm)) * 
                                     np.sin(20 * x_norm + np.cos(10 * x_norm)))
        
        # Combined function with adaptive weights
        return (0.4 * radial_term + 0.3 * wave_interference + 
                0.2 * poly_coupling + 0.05 * modulated + 0.05 * chaotic_perturbation)
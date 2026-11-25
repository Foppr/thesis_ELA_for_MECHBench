import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial exponential decay basins with fractal-like structure
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.7 * np.sin(15 * r) + 0.4 * np.cos(20 * r) + 
                                     0.2 * np.sin(30 * r) * np.cos(25 * r))
        
        # Multi-scale trigonometric wave interference with chaotic modulation
        wave_interference = np.sum(np.sin(12 * x_norm) * np.cos(14 * x_norm) * 
                                 np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                 np.exp(-0.3 * np.abs(x_norm)) * 
                                 (1 + 0.3 * np.sin(50 * x_norm)))
        
        # Asymmetric polynomial coupling with higher-order interactions and cross-dimensional chaos
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            poly_coupling += (x_norm[i]**4 * x_norm[j]**3 + 
                             0.6 * x_norm[i]**3 * x_norm[j]**4 +
                             0.3 * x_norm[i]**2 * x_norm[j]**5 +
                             0.2 * x_norm[i]**5 * x_norm[j]**2 +
                             0.1 * x_norm[i]**3 * x_norm[j]**3 * x_norm[k]**2)
        
        # Multi-scale sinusoidal modulation with chaotic phase perturbations and varying amplitudes
        modulated = np.sum(np.sin(20 * x_norm + 0.7 * np.sin(15 * x_norm)) * 
                          np.cos(15 * x_norm - 0.5 * np.cos(12 * x_norm)) * 
                          np.exp(-0.4 * np.abs(x_norm)) * 
                          (1 + 0.2 * np.sin(35 * x_norm)))
        
        # Enhanced exponential decay with fractal-like chaotic perturbations and spectral complexity
        chaotic_perturbation = np.sum(np.exp(-7 * np.abs(x_norm)) * 
                                     np.sin(30 * x_norm + np.cos(25 * x_norm)) * 
                                     np.cos(18 * x_norm + np.sin(22 * x_norm)))
        
        # Combined function with adaptive weights and enhanced nonlinearity
        return (0.35 * radial_term + 0.25 * wave_interference + 
                0.2 * poly_coupling + 0.1 * modulated + 0.1 * chaotic_perturbation)
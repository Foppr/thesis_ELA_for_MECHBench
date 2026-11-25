import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial exponential decay basins with fractal-like structure and adaptive scaling
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.8 * np.sin(20 * r) + 0.5 * np.cos(25 * r) + 
                                     0.3 * np.sin(40 * r) * np.cos(30 * r) + 
                                     0.1 * np.sin(50 * r)**2)
        
        # Multi-scale trigonometric wave interference with chaotic modulation and frequency coupling
        wave_interference = np.sum(np.sin(15 * x_norm) * np.cos(17 * x_norm) * 
                                 np.sin(10 * x_norm) * np.cos(8 * x_norm) * 
                                 np.exp(-0.4 * np.abs(x_norm)) * 
                                 (1 + 0.4 * np.sin(60 * x_norm) * np.cos(45 * x_norm)))
        
        # Asymmetric polynomial coupling with higher-order interactions, cross-dimensional chaos, and adaptive weights
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            l = (i + 3) % self.dim
            poly_coupling += (x_norm[i]**5 * x_norm[j]**4 + 
                             0.7 * x_norm[i]**4 * x_norm[j]**5 +
                             0.4 * x_norm[i]**3 * x_norm[j]**6 +
                             0.3 * x_norm[i]**6 * x_norm[j]**3 +
                             0.2 * x_norm[i]**4 * x_norm[j]**4 * x_norm[k]**2 +
                             0.1 * x_norm[i]**3 * x_norm[j]**3 * x_norm[k]**3 * x_norm[l]**2)
        
        # Multi-scale sinusoidal modulation with chaotic phase perturbations, varying amplitudes, and hybrid coupling
        modulated = np.sum(np.sin(25 * x_norm + 0.8 * np.sin(20 * x_norm)) * 
                          np.cos(20 * x_norm - 0.6 * np.cos(18 * x_norm)) * 
                          np.exp(-0.5 * np.abs(x_norm)) * 
                          (1 + 0.3 * np.sin(40 * x_norm) * np.cos(35 * x_norm)))
        
        # Enhanced exponential decay with fractal-like chaotic perturbations, spectral complexity, and hybrid interaction
        chaotic_perturbation = np.sum(np.exp(-8 * np.abs(x_norm)) * 
                                     np.sin(35 * x_norm + np.cos(30 * x_norm)) * 
                                     np.cos(20 * x_norm + np.sin(25 * x_norm)) * 
                                     (1 + 0.25 * np.sin(45 * x_norm)))
        
        # Additional hybrid term with complex interaction patterns and enhanced nonlinearity
        hybrid_term = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                           np.exp(-0.6 * np.abs(x_norm)) * 
                           (1 + 0.35 * np.sin(55 * x_norm) + 0.2 * np.cos(48 * x_norm)))
        
        # Combined function with adaptive weights and enhanced nonlinearity
        return (0.3 * radial_term + 0.2 * wave_interference + 
                0.15 * poly_coupling + 0.15 * modulated + 
                0.1 * chaotic_perturbation + 0.1 * hybrid_term)
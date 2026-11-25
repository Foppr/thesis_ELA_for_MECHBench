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
        
        # Additional chaotic coupling mechanism with altered trigonometric frequencies
        chaotic_coupling = np.sum(np.sin(17 * x_norm + np.cos(23 * x_norm)) * 
                                 np.cos(19 * x_norm + np.sin(29 * x_norm)) * 
                                 np.exp(-0.5 * np.abs(x_norm)))
        
        # Fractal basin complexity with nested harmonic modulations
        fractal_basin = np.sum(np.sin(31 * x_norm) * np.cos(37 * x_norm) * 
                              (1 + 0.5 * np.sin(41 * x_norm)) * 
                              np.exp(-0.2 * r**2))
        
        # Cubic interaction terms with enhanced radial sensitivity
        cubic_interaction = np.sum(x_norm**3 * np.sin(13 * x_norm) * 
                                 np.cos(17 * x_norm) * 
                                 np.exp(-0.4 * np.abs(x_norm)))
        
        # Combined function with adaptive weights
        return (0.25 * radial_term + 0.20 * wave_interference + 
                0.20 * poly_coupling + 0.15 * modulated + 0.10 * chaotic_perturbation +
                0.05 * chaotic_coupling + 0.03 * fractal_basin + 0.02 * cubic_interaction)
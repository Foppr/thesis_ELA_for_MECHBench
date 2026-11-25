import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial exponential decay basins with fractal-like structure
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.8 * np.sin(15 * r) + 0.5 * np.cos(20 * r) + 0.3 * np.sin(30 * r))
        
        # Modified trigonometric wave interference pattern with higher frequencies
        wave_interference = np.sum(np.sin(10 * x_norm) * np.cos(13 * x_norm) * 
                                  np.sin(8 * x_norm) * np.cos(6 * x_norm))
        
        # Enhanced asymmetric polynomial coupling with cubic terms and cross-dimensional interactions
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (x_norm[i]**3 * x_norm[j]**2 + 
                             0.8 * x_norm[i]**2 * x_norm[j]**3 +
                             0.4 * x_norm[i]**4 * x_norm[j] +
                             0.2 * x_norm[i] * x_norm[j]**4)
        
        # Multi-scale sinusoidal modulation with varying amplitudes and phases
        modulated = np.sum(np.sin(18 * x_norm + 0.7) * 
                          np.cos(12 * x_norm - 0.5) * 
                          np.exp(-0.4 * np.abs(x_norm)))
        
        # Enhanced exponential decay with chaotic perturbations and fractal-like structure
        chaotic_perturbation = np.sum(np.exp(-7 * np.abs(x_norm)) * 
                                     np.sin(30 * x_norm + np.cos(15 * x_norm) + 0.15 * np.sin(35 * x_norm)))
        
        # Additional harmonic modulation to increase landscape complexity
        harmonic_modulation = np.sum(np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                                   (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Combined function with adaptive weights
        return (0.3 * radial_term + 0.2 * wave_interference + 
                0.25 * poly_coupling + 0.15 * modulated + 0.08 * chaotic_perturbation + 0.07 * harmonic_modulation)
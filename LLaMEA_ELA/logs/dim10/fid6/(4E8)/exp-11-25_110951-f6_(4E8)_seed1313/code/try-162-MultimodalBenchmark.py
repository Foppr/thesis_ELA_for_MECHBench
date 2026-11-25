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
        
        # Trigonometric wave interference pattern with higher frequencies and phase shifts
        wave_interference = np.sum(np.sin(9 * x_norm + 0.3) * np.cos(11 * x_norm - 0.4) * 
                                  np.sin(6 * x_norm + 0.2) * np.cos(4 * x_norm - 0.1))
        
        # Asymmetric polynomial coupling with cubic and quartic terms
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (0.8 * x_norm[i]**3 * x_norm[j]**2 + 
                             0.3 * x_norm[i]**2 * x_norm[j]**3 +
                             0.2 * x_norm[i]**4 * x_norm[j] + 
                             0.1 * x_norm[i] * x_norm[j]**4)
        
        # Multi-scale sinusoidal modulation with varying amplitudes, phases and exponential decay
        modulated = np.sum(np.sin(15 * x_norm + 0.6) * 
                          np.cos(10 * x_norm - 0.4) * 
                          np.exp(-0.3 * np.abs(x_norm)) * 
                          (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Enhanced chaotic perturbation with higher frequency oscillations
        chaotic_perturbation = np.sum(np.exp(-6 * np.abs(x_norm)) * 
                                     np.sin(25 * x_norm + np.cos(15 * x_norm) + 0.5 * np.sin(30 * x_norm)))
        
        # Combined function with adjusted weights for better conditioning
        return (0.35 * radial_term + 0.25 * wave_interference + 
                0.2 * poly_coupling + 0.1 * modulated + 0.1 * chaotic_perturbation)
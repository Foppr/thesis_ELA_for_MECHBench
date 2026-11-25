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
        
        # Trigonometric wave interference pattern with higher frequencies and phase shifts
        wave_interference = np.sum(np.sin(10 * x_norm + 0.4) * np.cos(13 * x_norm - 0.5) * 
                                  np.sin(7 * x_norm + 0.3) * np.cos(5 * x_norm - 0.2))
        
        # Asymmetric polynomial coupling with cubic and quartic terms
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (0.9 * x_norm[i]**3 * x_norm[j]**2 + 
                             0.4 * x_norm[i]**2 * x_norm[j]**3 +
                             0.3 * x_norm[i]**4 * x_norm[j] + 
                             0.2 * x_norm[i] * x_norm[j]**4)
        
        # Multi-scale sinusoidal modulation with varying amplitudes, phases and exponential decay
        modulated = np.sum(np.sin(18 * x_norm + 0.7) * 
                          np.cos(12 * x_norm - 0.5) * 
                          np.exp(-0.4 * np.abs(x_norm)) * 
                          (1 + 0.4 * np.sin(10 * x_norm)))
        
        # Enhanced chaotic perturbation with higher frequency oscillations
        chaotic_perturbation = np.sum(np.exp(-7 * np.abs(x_norm)) * 
                                     np.sin(30 * x_norm + np.cos(20 * x_norm) + 0.6 * np.sin(35 * x_norm)))
        
        # Additional harmonic modulation to improve conditioning
        harmonic_modulation = np.sum(np.sin(25 * x_norm) * np.cos(15 * x_norm) * 
                                   (1 + 0.2 * np.sin(8 * x_norm) + 0.1 * np.cos(12 * x_norm)))
        
        # Combined function with adjusted weights for better conditioning
        return (0.3 * radial_term + 0.2 * wave_interference + 
                0.25 * poly_coupling + 0.15 * modulated + 0.1 * chaotic_perturbation + 0.05 * harmonic_modulation)
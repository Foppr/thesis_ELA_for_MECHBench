import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced separable quadratic base with dynamic conditioning
        quadratic_base = np.sum((x_norm**2) * (1 + 0.5 * np.sin(6 * x_norm) * np.cos(3 * x_norm)))
        
        # Non-separable correlation term with double chaotic interaction
        correlation_term = -30 * np.exp(-0.3 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(5 * np.pi * x_norm))) + 30 + np.e
        
        # Enhanced helicoidal chaotic distortion with multi-frequency pitch and phase modulation
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += (np.sin(10 * angle + i * 0.7) * np.cos(10 * angle + i * 0.7) +
                                0.5 * np.sin(17 * angle + i * 0.3) * np.cos(17 * angle + i * 0.3) +
                                0.2 * np.sin(23 * angle + i * 0.1) * np.cos(23 * angle + i * 0.1))
        
        # Multi-scale sinusoidal modulation with exponential decay, phase shifts and cubic harmonics
        modulated_term = np.sum(np.sin(20 * x_norm) * np.cos(16 * x_norm) * 
                               np.sin(11 * x_norm) * np.cos(8 * x_norm) * 
                               np.exp(-0.15 * np.abs(x_norm)) * (1 + 0.3 * x_norm**3))
        
        # Fractal-like basin with multiple nested minima, chaotic perturbations and multi-scale oscillations
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 1.1 * np.exp(-r**2) + 0.6 * np.sin(20 * r) * np.cos(11 * r) + \
                        0.4 * np.sin(33 * r) * np.cos(18 * r) + 0.2 * np.sin(45 * r) + \
                        0.1 * np.sin(57 * r) * np.cos(31 * r)
        
        # Cross-dimensional coupling with polynomial interaction and chaotic modulation
        coupling_term = np.sum((x_norm[i]**4 * x_norm[(i+2) % self.dim] * 
                               np.sin(7 * x_norm[i]) for i in range(self.dim))) / self.dim
        
        # Added enhanced chaotic perturbation term with higher frequency components
        chaotic_perturbation = 0.15 * np.sum(np.sin(30 * x_norm) * np.cos(22 * x_norm) * 
                                           np.exp(-0.08 * np.abs(x_norm)) * 
                                           (1 + 0.4 * np.sin(13 * x_norm)))
        
        # Combined function with adaptive scaling and added noise-like perturbations
        return 0.4 * quadratic_base + 0.45 * correlation_term + \
               0.25 * helix_distortion + 0.2 * modulated_term + fractal_basin + 0.15 * coupling_term + chaotic_perturbation
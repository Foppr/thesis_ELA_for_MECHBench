import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic base function with variable conditioning and added cubic terms
        quadratic_base = np.sum((x_norm**2) * (1 + 0.3 * np.sin(5 * x_norm) + 0.2 * x_norm**3))
        
        # Non-separable correlation term with enhanced chaotic interaction and multi-scale components
        correlation_term = -40 * np.exp(-0.15 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(5 * np.pi * x_norm))) + 40 + np.e + \
                           0.5 * np.sin(13 * np.mean(x_norm)) * np.cos(9 * np.mean(x_norm))
        
        # Enhanced helicoidal chaotic distortion with multi-frequency pitch and phase modulation
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += (np.sin(9 * angle + i * 0.8) * np.cos(9 * angle + i * 0.8) +
                                0.7 * np.sin(13 * angle + i * 0.4) * np.cos(13 * angle + i * 0.4) +
                                0.3 * np.sin(17 * angle + i * 0.2) * np.cos(17 * angle + i * 0.2))
        
        # Multi-scale sinusoidal modulation with exponential decay, phase shifts and cubic interactions
        modulated_term = np.sum(np.sin(18 * x_norm) * np.cos(15 * x_norm) * 
                               np.sin(10 * x_norm) * np.cos(7 * x_norm) * 
                               np.exp(-0.12 * np.abs(x_norm)) * (1 + 0.1 * x_norm**3))
        
        # Fractal-like basin with multiple nested minima, chaotic perturbations and multi-frequency components
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 1.0 * np.exp(-r**2) + 0.6 * np.sin(18 * r) * np.cos(10 * r) + \
                        0.3 * np.sin(28 * r) * np.cos(15 * r) + 0.15 * np.sin(38 * r) + \
                        0.2 * np.sin(23 * r) * np.cos(17 * r) * np.exp(-0.05 * r**2)
        
        # Cross-dimensional coupling with polynomial interaction and chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += x_norm[i]**3 * x_norm[(i+2) % self.dim] * np.sin(11 * x_norm[i])
        coupling_term = coupling_term / self.dim
        
        # Added chaotic perturbation term with higher frequency and stronger nonlinearity
        chaotic_perturbation = 0.15 * np.sum(np.sin(27 * x_norm) * np.cos(21 * x_norm) * 
                                            np.exp(-0.08 * np.abs(x_norm)) * (1 + 0.05 * x_norm**4))
        
        # Combined function with adaptive scaling and enhanced noise-like perturbations
        return 0.35 * quadratic_base + 0.3 * correlation_term + \
               0.2 * helix_distortion + 0.18 * modulated_term + fractal_basin + 0.12 * coupling_term + chaotic_perturbation
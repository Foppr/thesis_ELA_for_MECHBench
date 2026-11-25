import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced separable quadratic base with variable conditioning and chaotic noise
        quadratic_base = np.sum((x_norm**2) * (1 + 0.7 * np.sin(7 * x_norm) * np.cos(4 * x_norm)) * 
                               (1 + 0.3 * np.sin(13 * x_norm) * np.cos(9 * x_norm)))
        
        # Non-separable correlation term with higher frequency chaotic interaction and multi-scale modulation
        correlation_term = -40 * np.exp(-0.25 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(7 * np.pi * x_norm))) + 40 + np.e
        
        # Enhanced helicoidal chaotic distortion with multi-frequency pitch and phase modulation
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += (np.sin(15 * angle + i * 0.9) * np.cos(15 * angle + i * 0.9) +
                                0.6 * np.sin(23 * angle + i * 0.4) * np.cos(23 * angle + i * 0.4) +
                                0.4 * np.sin(31 * angle + i * 0.2) * np.cos(31 * angle + i * 0.2) +
                                0.2 * np.sin(37 * angle + i * 0.1) * np.cos(37 * angle + i * 0.1))
        
        # Multi-scale sinusoidal modulation with exponential decay, phase shifts, and cross-term interactions
        modulated_term = np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                               np.exp(-0.2 * np.abs(x_norm)) * 
                               (1 + 0.3 * np.sin(9 * x_norm)) * 
                               (1 + 0.2 * np.cos(11 * x_norm)))
        
        # Fractal-like basin with multiple nested minima, chaotic perturbations, and multi-scale structure
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 1.3 * np.exp(-r**2) + 0.8 * np.sin(25 * r) * np.cos(12 * r) + \
                        0.6 * np.sin(35 * r) * np.cos(20 * r) + 0.4 * np.sin(45 * r) + \
                        0.3 * np.sin(55 * r) * np.cos(30 * r) + 0.15 * np.sin(65 * r)
        
        # Cross-dimensional coupling with polynomial interaction and chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 5) % self.dim
            k = (i + 3) % self.dim
            coupling_term += x_norm[i]**4 * x_norm[j] * x_norm[k] * np.sin(15 * x_norm[i]) * np.cos(11 * x_norm[j])
        coupling_term /= self.dim
        
        # Added chaotic perturbation term with higher frequency components and stronger conditioning
        chaotic_perturbation = 0.2 * np.sum(np.sin(35 * x_norm) * np.cos(27 * x_norm) * 
                                           np.exp(-0.1 * np.abs(x_norm)) * 
                                           (1 + 0.4 * np.sin(18 * x_norm)) * 
                                           (1 + 0.3 * np.cos(22 * x_norm)))
        
        # Combined function with adaptive scaling, noise-like perturbations, and enhanced complexity
        return 0.35 * quadratic_base + 0.5 * correlation_term + \
               0.3 * helix_distortion + 0.25 * modulated_term + fractal_basin + 0.2 * coupling_term + chaotic_perturbation
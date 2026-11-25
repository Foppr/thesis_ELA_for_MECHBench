import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic base function with variable conditioning
        quadratic_base = np.sum((x_norm**2) * (1 + 0.5 * np.sin(3 * x_norm)))
        
        # Non-separable correlation term with enhanced chaotic interaction
        correlation_term = -30 * np.exp(-0.2 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(3 * np.pi * x_norm))) + 30 + np.e
        
        # Enhanced helicoidal chaotic distortion with multi-frequency pitch
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += (np.sin(7 * angle + i * 0.7) * np.cos(7 * angle + i * 0.7) +
                                0.5 * np.sin(11 * angle + i * 0.3) * np.cos(11 * angle + i * 0.3))
        
        # Multi-scale sinusoidal modulation with exponential decay and phase shifts
        modulated_term = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                               np.sin(8 * x_norm) * np.cos(5 * x_norm) * 
                               np.exp(-0.1 * np.abs(x_norm)))
        
        # Fractal-like basin with multiple nested minima and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.8 * np.exp(-r**2) + 0.4 * np.sin(15 * r) * np.cos(8 * r) + \
                        0.2 * np.sin(25 * r) * np.cos(13 * r) + 0.1 * np.sin(35 * r)
        
        # Cross-dimensional coupling with polynomial interaction
        coupling_term = np.sum((x_norm[i] * x_norm[(i+2) % self.dim] for i in range(self.dim))) / self.dim
        
        # Added chaotic perturbation term to increase conditioning and challenge
        chaotic_perturbation = 0.1 * np.sum(np.sin(23 * x_norm) * np.cos(17 * x_norm) * 
                                           np.exp(-0.05 * np.abs(x_norm)))
        
        # Combined function with adaptive scaling and added noise-like perturbations
        return 0.4 * quadratic_base + 0.35 * correlation_term + \
               0.25 * helix_distortion + 0.15 * modulated_term + fractal_basin + 0.1 * coupling_term + chaotic_perturbation
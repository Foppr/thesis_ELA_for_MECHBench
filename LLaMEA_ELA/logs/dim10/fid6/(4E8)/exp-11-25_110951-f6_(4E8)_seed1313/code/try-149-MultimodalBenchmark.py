import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Separable quadratic base function with variable conditioning
        quadratic_base = np.sum((x_norm**2) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Non-separable correlation term with enhanced chaotic interaction
        correlation_term = -25 * np.exp(-0.15 * np.sqrt(np.mean(x_norm**2))) - \
                           np.exp(np.mean(np.cos(4 * np.pi * x_norm))) + 25 + np.e
        
        # Enhanced helicoidal chaotic distortion with multi-frequency pitch
        helix_distortion = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[(i+1) % self.dim], x_norm[i])
            helix_distortion += (np.sin(9 * angle + i * 0.5) * np.cos(9 * angle + i * 0.5) +
                                0.6 * np.sin(13 * angle + i * 0.2) * np.cos(13 * angle + i * 0.2))
        
        # Multi-scale sinusoidal modulation with exponential decay and phase shifts
        modulated_term = np.sum(np.sin(17 * x_norm) * np.cos(14 * x_norm) * 
                               np.sin(10 * x_norm) * np.cos(6 * x_norm) * 
                               np.exp(-0.12 * np.abs(x_norm)))
        
        # Fractal-like basin with multiple nested minima and chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.9 * np.exp(-r**2) + 0.5 * np.sin(18 * r) * np.cos(9 * r) + \
                        0.3 * np.sin(30 * r) * np.cos(15 * r) + 0.15 * np.sin(40 * r)
        
        # Cross-dimensional coupling with polynomial interaction (modified)
        coupling_term = np.sum((x_norm[i]**3 * x_norm[(i+2) % self.dim] for i in range(self.dim))) / self.dim
        
        # Added chaotic perturbation term to increase conditioning and challenge
        chaotic_perturbation = 0.15 * np.sum(np.sin(25 * x_norm) * np.cos(19 * x_norm) * 
                                           np.exp(-0.06 * np.abs(x_norm)))
        
        # Combined function with adaptive scaling and added noise-like perturbations
        return 0.35 * quadratic_base + 0.4 * correlation_term + \
               0.2 * helix_distortion + 0.18 * modulated_term + fractal_basin + 0.12 * coupling_term + chaotic_perturbation
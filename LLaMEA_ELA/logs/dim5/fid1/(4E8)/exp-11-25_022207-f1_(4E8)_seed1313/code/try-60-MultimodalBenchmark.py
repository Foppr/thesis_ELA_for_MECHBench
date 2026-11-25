import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine interactions with varying frequencies
        chaotic_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                             (1 + 0.2 * np.sin(7 * np.pi * x_norm)) * 
                             np.exp(-0.1 * np.abs(x_norm)))
        
        # Adaptive polynomial coupling with dynamic exponents
        poly_coupling = np.sum((x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2) * 
                              np.cos(2 * x_norm) * np.exp(-0.05 * x_norm**2))
        
        # Dynamic repulsion field with position-dependent strength
        center_distance = np.sqrt(np.sum(x_norm**2))
        dynamic_repulsion = 1.0 / (1.0 + center_distance**3 + 0.5 * np.sin(4 * center_distance))
        
        # Cross-dimensional interactions with asymmetric coupling weights
        cross_term = 0.3 * np.sum((x_norm[:-1] - x_norm[1:])**3 * 
                                np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Add noise-like perturbations to increase robustness
        noise_perturbation = 0.05 * np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Combine all terms with appropriate scaling
        return chaotic_term + poly_coupling - dynamic_repulsion + cross_term + noise_perturbation
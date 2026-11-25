import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine interactions with varying frequencies and amplitude modulation
        chaotic_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                             (1 + 0.3 * np.sin(6 * np.pi * x_norm)) * 
                             np.exp(-0.15 * np.abs(x_norm)))
        
        # Adaptive polynomial coupling with dynamic exponents and asymmetric weights
        poly_coupling = np.sum((x_norm**5 + 0.4 * x_norm**3 - 0.2 * x_norm**2 + 0.1 * x_norm) * 
                              np.cos(3 * x_norm) * np.exp(-0.08 * x_norm**2))
        
        # Dynamic repulsion field with position-dependent strength and periodic modulation
        center_distance = np.sqrt(np.sum(x_norm**2))
        dynamic_repulsion = 1.0 / (1.0 + center_distance**4 + 0.3 * np.sin(5 * center_distance) * 
                                  np.cos(2 * center_distance))
        
        # Enhanced cross-dimensional interactions with non-linear coupling and directional bias
        cross_term = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**4 * 
                                np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                np.cos(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Improved noise-like perturbations with frequency-dependent scaling
        noise_perturbation = 0.08 * np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                                          (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Add a global shaping term to improve conditioning and fitness score
        global_shaping = 0.1 * np.sum(x_norm**6)
        
        # Combine all terms with appropriate scaling
        return chaotic_term + poly_coupling - dynamic_repulsion + cross_term + noise_perturbation + global_shaping
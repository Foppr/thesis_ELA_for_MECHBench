import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested chaotic sine-cosine interactions with multiple frequency layers
        chaotic_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                             np.cos(3 * np.pi * x_norm) * 
                             np.sin(5 * np.pi * x_norm) * 
                             (1 + 0.4 * np.sin(7 * np.pi * x_norm)) * 
                             np.exp(-0.2 * np.abs(x_norm)))
        
        # Enhanced polynomial coupling with variable degrees and adaptive weights
        poly_coupling = np.sum((x_norm**6 + 0.5 * x_norm**4 - 0.3 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm) * 
                              np.cos(4 * x_norm) * 
                              np.exp(-0.1 * x_norm**2))
        
        # Multi-center dynamic repulsion field with varying attraction/repulsion strengths
        center_distances = np.sqrt(np.sum((x_norm.reshape(1, -1) - np.linspace(-0.5, 0.5, self.dim).reshape(-1, 1))**2, axis=1))
        dynamic_repulsion = np.sum(1.0 / (1.0 + center_distances**3 + 0.4 * np.sin(6 * center_distances) * 
                                         np.cos(3 * center_distances)))
        
        # Cross-dimensional interactions with directional bias and frequency modulation
        cross_term = 0.5 * np.sum((x_norm[:-1] - x_norm[1:])**5 * 
                                np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                np.cos(0.7 * (x_norm[:-1] + x_norm[1:])) * 
                                (1 + 0.3 * np.sin(4 * (x_norm[:-1] - x_norm[1:]))))
        
        # Enhanced noise-like perturbations with multi-scale frequency components
        noise_perturbation = 0.12 * np.sum(np.sin(15 * x_norm) * np.cos(11 * x_norm) * 
                                          (1 + 0.3 * np.sin(5 * x_norm)) * 
                                          np.exp(-0.15 * np.abs(x_norm)))
        
        # Global shaping term with higher-order polynomial and directional bias
        global_shaping = 0.15 * np.sum(x_norm**7 + 0.3 * x_norm**5 - 0.2 * x_norm**4)
        
        # Combine all terms with appropriate scaling
        return chaotic_term + poly_coupling - dynamic_repulsion + cross_term + noise_perturbation + global_shaping
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine interactions with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Adaptive elliptic conditioning with dimension-dependent scaling
        elliptic_conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm)) + 
                                       0.5 * np.sum((x_norm**4) * np.exp(-0.1 * np.abs(x_norm))))
        
        # Higher-order polynomial cross-terms with mixed interactions
        poly_cross = np.sum((x_norm[0] * x_norm[1])**7) + \
                     0.3 * np.sum(x_norm**7 * np.sin(4 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm**3 * np.cos(5 * np.pi * x_norm))
        
        # Dynamic noise modulation based on input values and dimensionality
        noise_modulation = 0.02 * np.random.random() * (1 + 0.5 * np.sum(np.sin(x_norm) * np.cos(x_norm)))
        
        # Additional nonlinear coupling with exponential and trigonometric mix
        nonlinear_coupling = 0.4 * np.sum(np.exp(-0.5 * x_norm**2) * np.sin(11 * x_norm) * np.cos(14 * x_norm))
        
        # Multi-scale sinusoidal interactions for enhanced complexity
        multi_scale = 0.5 * np.sum(np.sin(15 * x_norm) * np.cos(18 * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Combine all terms to create a highly irregular multimodal landscape
        return chaotic_terms + elliptic_conditioning + poly_cross + noise_modulation + nonlinear_coupling + multi_scale
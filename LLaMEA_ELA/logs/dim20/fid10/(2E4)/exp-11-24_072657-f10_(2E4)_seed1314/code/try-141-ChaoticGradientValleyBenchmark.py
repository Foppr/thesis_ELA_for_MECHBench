import numpy as np

class ChaoticGradientValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Composite exponential-gaussian terms with chaotic modulation
        exp_gauss_terms = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(3.0 * np.pi * x_norm) * 
                                (1.0 + 0.3 * np.sin(2.5 * x_norm**2)))
        
        # Chaotic gradient interactions with adaptive frequency coupling
        grad_interactions = np.sum(np.exp(-0.3 * np.abs(x_norm)) * 
                                 np.sin(4.0 * x_norm + 0.5 * np.sin(1.7 * x_norm)) * 
                                 np.cos(2.0 * x_norm + 0.3 * np.cos(1.3 * x_norm)))
        
        # Multi-scale exponential decay with non-linear frequency modulation
        freq_mod = 2.0 + 1.5 * np.sin(0.5 * self.dim) + 0.8 * np.cos(0.3 * self.dim)
        modulated_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)**1.8) * 
                               np.sin(freq_mod * x_norm**1.5) * 
                               np.cos(freq_mod * x_norm**1.3))
        
        # Cross-dimensional interference with adaptive coupling strength
        coupling_strength = 0.7 + 0.3 * np.sin(0.4 * self.dim)
        cross_terms = np.sum(coupling_strength * np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           (x_norm[:-1] * x_norm[1:] + 0.6 * (x_norm[:-1]**2 - x_norm[1:]**2)) * 
                           np.sin(3.0 * (x_norm[:-1] - x_norm[1:])))
        
        # Adaptive dimensional conditioning with chaotic scaling
        dim_conditioning = 1.0 + 0.5 * np.sin(0.3 * self.dim) * np.cos(0.2 * self.dim)
        
        # Combined landscape with enhanced multi-modality
        result = (exp_gauss_terms + 0.7 * grad_interactions + 0.8 * modulated_terms + 
                 0.6 * cross_terms) * dim_conditioning
        
        # Add chaotic noise for increased complexity and algorithm discrimination
        noise = 0.0015 * np.random.random() * (1.0 + 0.2 * np.sin(self.dim * 0.8))
        
        return result + noise
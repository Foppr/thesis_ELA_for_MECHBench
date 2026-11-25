import numpy as np

class ChaoticGradientValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Composite exponential-gaussian terms with enhanced chaotic modulation
        exp_gauss_terms = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(3.5 * np.pi * x_norm) * 
                                (1.0 + 0.4 * np.sin(2.8 * x_norm**2)))
        
        # Enhanced chaotic gradient interactions with modified frequency coupling
        grad_interactions = np.sum(np.exp(-0.35 * np.abs(x_norm)) * 
                                 np.sin(4.5 * x_norm + 0.6 * np.sin(1.9 * x_norm)) * 
                                 np.cos(2.3 * x_norm + 0.4 * np.cos(1.5 * x_norm)))
        
        # Multi-scale exponential decay with altered frequency modulation
        freq_mod = 2.2 + 1.7 * np.sin(0.55 * self.dim) + 0.9 * np.cos(0.35 * self.dim)
        modulated_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)**1.9) * 
                               np.sin(freq_mod * x_norm**1.6) * 
                               np.cos(freq_mod * x_norm**1.4))
        
        # Enhanced cross-dimensional interference with modified coupling strength
        coupling_strength = 0.75 + 0.25 * np.sin(0.45 * self.dim)
        cross_terms = np.sum(coupling_strength * np.exp(-0.55 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           (x_norm[:-1] * x_norm[1:] + 0.7 * (x_norm[:-1]**2 - x_norm[1:]**2)) * 
                           np.sin(3.2 * (x_norm[:-1] - x_norm[1:])))
        
        # Enhanced adaptive dimensional conditioning with modified scaling
        dim_conditioning = 1.0 + 0.55 * np.sin(0.32 * self.dim) * np.cos(0.22 * self.dim)
        
        # Combined landscape with increased multi-modality
        result = (exp_gauss_terms + 0.75 * grad_interactions + 0.85 * modulated_terms + 
                 0.65 * cross_terms) * dim_conditioning
        
        # Add enhanced chaotic noise for increased complexity and algorithm discrimination
        noise = 0.0018 * np.random.random() * (1.0 + 0.25 * np.sin(self.dim * 0.85))
        
        return result + noise
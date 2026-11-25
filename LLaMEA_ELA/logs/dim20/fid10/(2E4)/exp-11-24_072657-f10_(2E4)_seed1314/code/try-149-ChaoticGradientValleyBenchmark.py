import numpy as np

class ChaoticGradientValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced composite exponential-gaussian terms with stronger chaotic modulation
        exp_gauss_terms = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(4.0 * np.pi * x_norm) * 
                                (1.0 + 0.4 * np.sin(3.0 * x_norm**2)) * 
                                (1.0 + 0.2 * np.cos(2.0 * x_norm)))
        
        # Enhanced chaotic gradient interactions with stronger adaptive coupling
        grad_interactions = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                                 np.sin(5.0 * x_norm + 0.6 * np.sin(2.0 * x_norm)) * 
                                 np.cos(3.0 * x_norm + 0.4 * np.cos(1.5 * x_norm)) * 
                                 (1.0 + 0.3 * np.sin(0.5 * self.dim)))
        
        # Improved multi-scale exponential decay with enhanced frequency modulation
        freq_mod = 2.5 + 2.0 * np.sin(0.6 * self.dim) + 1.0 * np.cos(0.4 * self.dim)
        modulated_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)**2.0) * 
                               np.sin(freq_mod * x_norm**1.7) * 
                               np.cos(freq_mod * x_norm**1.4) * 
                               (1.0 + 0.15 * np.sin(0.3 * self.dim)))
        
        # Enhanced cross-dimensional interference with stronger coupling
        coupling_strength = 0.8 + 0.4 * np.sin(0.5 * self.dim)
        cross_terms = np.sum(coupling_strength * np.exp(-0.6 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           (x_norm[:-1] * x_norm[1:] + 0.7 * (x_norm[:-1]**2 - x_norm[1:]**2)) * 
                           np.sin(4.0 * (x_norm[:-1] - x_norm[1:])) * 
                           (1.0 + 0.25 * np.cos(0.6 * self.dim)))
        
        # Improved dimensional conditioning with enhanced chaotic scaling
        dim_conditioning = 1.2 + 0.6 * np.sin(0.4 * self.dim) * np.cos(0.3 * self.dim)
        
        # Combined landscape with improved multi-modality and enhanced complexity
        result = (exp_gauss_terms + 0.8 * grad_interactions + 0.9 * modulated_terms + 
                 0.7 * cross_terms) * dim_conditioning
        
        # Enhanced chaotic noise for better algorithm discrimination
        noise = 0.002 * np.random.random() * (1.0 + 0.3 * np.sin(self.dim * 0.9))
        
        return result + noise
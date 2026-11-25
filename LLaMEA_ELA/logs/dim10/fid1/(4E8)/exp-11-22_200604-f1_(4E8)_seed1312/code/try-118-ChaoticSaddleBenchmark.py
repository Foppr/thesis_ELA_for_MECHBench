import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic logarithmic interactions with dynamic frequency modulation
        freq_mod = 1 + 0.3 * np.sin(3 * np.pi * x_norm)
        f2 = 0.6 * np.sum(np.log(np.abs(x_norm) + 1e-8) * np.cos(freq_mod * 25 * x_norm))
        
        # Asymmetric saddle point landscape with exponential penalties
        f3 = 0.4 * np.sum(np.abs(x_norm)**1.7 * np.sin(12 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Dynamic penalty term that varies with dimensionality and chaos
        dynamic_penalty = np.sum(np.exp(-0.15 * (x_norm**2 + 0.4 * x_norm**4)) * 
                                (1 + 0.2 * np.sin(7 * x_norm)))
        f4 = 0.5 * dynamic_penalty
        
        # Cross-dimensional coupling with chaotic interaction weights and adaptive scaling
        cross_term = 0.3 * np.sum(np.sin(30 * (x_norm[:-1] + x_norm[1:])) * 
                                 np.cos(20 * (x_norm[:-1] - x_norm[1:])) * 
                                 (1 + 0.1 * np.sin(5 * x_norm[:-1])))
        f5 = cross_term
        
        # Multi-scale oscillatory component with varying amplitudes and chaos
        f6 = 0.3 * np.sum(np.sin(35 * x_norm**3) * np.cos(25 * x_norm**2) * 
                         (1 + 0.15 * np.sin(8 * x_norm)))
        
        # Asymmetric Gaussian-like peaks with varying heights and chaotic modulation
        peak_heights = 1.2 + 0.4 * np.sin(6 * x_norm) * np.cos(3 * x_norm)
        f7 = 0.35 * np.sum(peak_heights * np.exp(-0.4 * (x_norm - 0.15)**2))
        
        # Enhanced resonance-based interaction with phase shifts and dynamic modulation
        phase_shift = np.pi / 3 + 0.3 * np.sin(x_norm) * np.cos(2 * x_norm)
        f8 = 0.25 * np.sum(np.sin(15 * x_norm + phase_shift) * np.cos(10 * x_norm) * 
                          (1 + 0.1 * np.sin(4 * x_norm)))
        
        # Additional chaotic polynomial coupling for increased complexity
        f9 = 0.15 * np.sum((x_norm**7 + 0.5 * x_norm**5 + 0.3 * x_norm**3) * 
                          np.sin(20 * x_norm))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result
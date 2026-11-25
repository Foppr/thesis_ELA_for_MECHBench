import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-wave interactions with dynamic frequency modulation
        freq_mod = 1 + 0.5 * np.sin(2 * np.pi * x_norm)
        f2 = 0.5 * np.sum(np.sin(freq_mod * 22 * x_norm) * np.cos(17 * x_norm))
        
        # Asymmetric saddle point landscape with exponential penalties
        f3 = 0.3 * np.sum(np.abs(x_norm)**1.7 * np.sin(12 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Dynamic penalty term that varies with dimensionality
        dynamic_penalty = np.sum(np.exp(-0.1 * (x_norm**2 + 0.5 * x_norm**4)))
        f4 = 0.4 * dynamic_penalty
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_term = 0.2 * np.sum(np.sin(27 * (x_norm[:-1] + x_norm[1:])) * 
                                 np.cos(20 * (x_norm[:-1] - x_norm[1:])))
        f5 = cross_term
        
        # Multi-scale oscillatory component with varying amplitudes
        f6 = 0.25 * np.sum(np.sin(32 * x_norm**3) * np.cos(24 * x_norm**2))
        
        # Asymmetric Gaussian-like peaks with varying heights and shifted positions
        peak_heights = 1 + 0.3 * np.sin(5 * x_norm)
        f7 = 0.3 * np.sum(peak_heights * np.exp(-0.5 * (x_norm - 0.15)**2))
        
        # Resonance-based interaction with phase shifts
        phase_shift = np.pi / 4 + 0.2 * np.sin(x_norm)
        f8 = 0.2 * np.sum(np.sin(14 * x_norm + phase_shift) * np.cos(10 * x_norm))
        
        # Enhanced chaotic logarithmic interactions
        log_interaction = np.sum(np.log(np.abs(x_norm) + 1e-8) * np.sin(37 * x_norm))
        f9 = 0.35 * log_interaction
        
        # Adaptive polynomial scaling with dynamic exponents
        adaptive_exp = 1.3 + 0.7 * np.cos(0.6 * x_norm)
        f10 = 0.2 * np.sum(np.abs(x_norm)**adaptive_exp)
        
        # Additional high-frequency cross-dimensional couplings
        high_freq_coupling = np.sum(np.sin(52 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                   np.cos(32 * (x_norm[:-1] * x_norm[1:])))
        f11 = 0.15 * high_freq_coupling
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result
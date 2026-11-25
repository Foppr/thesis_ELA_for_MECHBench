import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic logarithmic interactions with dynamic scaling
        log_interaction = np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.sin(30 * x_norm))
        f2 = 0.6 * log_interaction
        
        # Adaptive polynomial scaling with dimension-dependent exponents
        adaptive_exp = 2 + 0.3 * np.sin(np.pi * x_norm)
        f3 = 0.4 * np.sum(np.abs(x_norm)**adaptive_exp)
        
        # Dynamic cross-dimensional couplings with chaotic weights
        cross_coupling = 0.3 * np.sum(np.sin(20 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.cos(15 * (x_norm[:-1] - x_norm[1:])) * 
                                     np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        f4 = cross_coupling
        
        # Asymmetric saddle point landscape with exponential penalties
        f5 = 0.35 * np.sum(np.abs(x_norm)**1.8 * np.sin(12 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Multi-scale oscillatory component with varying amplitudes and phases
        f6 = 0.3 * np.sum(np.sin(40 * x_norm**3) * np.cos(25 * x_norm**2) * 
                         np.exp(-0.1 * np.abs(x_norm)))
        
        # Enhanced resonance-based interaction with phase shifts
        phase_shift = np.pi / 3 + 0.3 * np.sin(2 * x_norm)
        f7 = 0.25 * np.sum(np.sin(15 * x_norm + phase_shift) * np.cos(10 * x_norm))
        
        # Asymmetric Gaussian-like peaks with varying heights and widths
        peak_heights = 1 + 0.4 * np.sin(6 * x_norm)
        peak_widths = 0.8 + 0.2 * np.cos(3 * x_norm)
        f8 = 0.35 * np.sum(peak_heights * np.exp(-0.5 * ((x_norm - 0.1) / peak_widths)**2))
        
        # Dynamic penalty term that varies with dimensionality and interaction strength
        dynamic_penalty = np.sum(np.exp(-0.15 * (x_norm**2 + 0.6 * x_norm**4)) * 
                                np.sin(25 * x_norm)**2)
        f9 = 0.4 * dynamic_penalty
        
        # Combined result with additional chaotic modulation
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result
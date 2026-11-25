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
        
        # Augmented asymmetric saddle points with additional chaotic modulation
        f10 = 0.5 * np.sum(np.abs(x_norm)**2.5 * np.sin(18 * x_norm) * 
                          np.exp(-0.2 * np.abs(x_norm)) * np.cos(7 * x_norm))
        
        # Modified Gaussian peaks with dynamic widths and heights
        peak_heights_mod = 1.2 + 0.3 * np.cos(4 * x_norm)
        peak_widths_mod = 0.6 + 0.3 * np.sin(5 * x_norm)
        f11 = 0.4 * np.sum(peak_heights_mod * np.exp(-0.5 * ((x_norm + 0.2) / peak_widths_mod)**2))
        
        # New multi-scale frequency modulation component
        f12 = 0.3 * np.sum(np.sin(50 * x_norm**4) * np.cos(30 * x_norm**3) * 
                          np.exp(-0.15 * np.abs(x_norm**2)))
        
        # Additional chaotic modulation and improved scaling factors to enhance fitness
        chaotic_mod = 0.1 * np.sum(np.sin(60 * x_norm**2) * np.cos(40 * x_norm) * 
                                  np.exp(-0.1 * x_norm**2))
        
        # Combine all components with optimized weights for better performance
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + chaotic_mod
        
        return result
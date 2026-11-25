import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like self-similarity with multi-scale chaotic interactions
        fractal_term = 0.5 * np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                                   np.sin(15 * x_norm**2) * np.cos(10 * x_norm**2))
        
        # Memory-dependent penalty terms with temporal decay
        memory_penalty = 0.4 * np.sum(np.exp(-0.2 * (x_norm**2 + 0.3 * x_norm**4)) * 
                                     np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Enhanced chaotic logarithmic interactions with dynamic base
        log_interaction = np.sum(np.log(np.abs(x_norm) + 1e-6) * 
                                np.sin(40 * x_norm) * np.cos(20 * x_norm))
        
        # Asymmetric saddle point landscape with exponential penalties
        f3 = 0.3 * np.sum(np.abs(x_norm)**1.5 * np.sin(12 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Dynamic penalty term that varies with dimensionality and history
        dynamic_penalty = np.sum(np.exp(-0.1 * (x_norm**2 + 0.5 * x_norm**4)) * 
                                np.sin(8 * x_norm) * np.cos(6 * x_norm))
        f4 = 0.35 * dynamic_penalty
        
        # Cross-dimensional coupling with chaotic interaction weights and memory
        cross_term = 0.25 * np.sum(np.sin(30 * (x_norm[:-1] + x_norm[1:])) * 
                                  np.cos(20 * (x_norm[:-1] - x_norm[1:])) * 
                                  np.sin(15 * x_norm[:-1]) * np.cos(10 * x_norm[1:]))
        f5 = cross_term
        
        # Multi-scale oscillatory component with varying amplitudes and frequencies
        f6 = 0.3 * np.sum(np.sin(35 * x_norm**3) * np.cos(25 * x_norm**2) * 
                         np.sin(18 * x_norm) * np.cos(12 * x_norm))
        
        # Asymmetric Gaussian-like peaks with varying heights and memory effects
        peak_heights = 1 + 0.4 * np.sin(6 * x_norm) * np.cos(4 * x_norm)
        f7 = 0.35 * np.sum(peak_heights * np.exp(-0.5 * (x_norm - 0.2)**2))
        
        # Resonance-based interaction with phase shifts and dynamic frequency
        phase_shift = np.pi / 4 + 0.3 * np.sin(x_norm) * np.cos(0.5 * x_norm)
        f8 = 0.25 * np.sum(np.sin(15 * x_norm + phase_shift) * np.cos(10 * x_norm))
        
        # Adaptive polynomial scaling with dynamic exponents and memory
        adaptive_exp = 1.3 + 0.7 * np.cos(0.6 * x_norm) * np.sin(0.4 * x_norm)
        f10 = 0.25 * np.sum(np.abs(x_norm)**adaptive_exp)
        
        # Additional high-frequency cross-dimensional couplings with fractal characteristics
        high_freq_coupling = np.sum(np.sin(60 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                   np.cos(40 * (x_norm[:-1] * x_norm[1:])) * 
                                   np.sin(25 * x_norm[:-1]) * np.cos(20 * x_norm[1:]))
        f11 = 0.2 * high_freq_coupling
        
        # Combined result
        result = f1 + fractal_term + log_interaction + f3 + f4 + f5 + f6 + f7 + f8 + f10 + f11
        
        return result
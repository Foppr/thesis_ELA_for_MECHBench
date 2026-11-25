import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial distortion with varying exponents
        poly_term = np.sum((x**3.7 + 0.8 * x**2.9 - 0.3 * x**1.4 + 0.7 * x + 1.2)**1.3)
        
        # Cross-dimensional chaotic coupling with sine-cosine nesting
        chaotic_coupling = np.sum(np.sin(np.cos(np.exp(1.5 * x)) * np.pi) + 
                                 np.cos(np.sin(np.exp(1.2 * x)) * np.pi))
        
        # Multi-scale trigonometric modulation with adaptive frequencies
        trig_term = np.sum(np.sin(3.1 * x) * np.cos(7.3 * x) * np.sin(2.8 * x) * np.cos(4.9 * x))
        
        # Enhanced exponential decay with complex argument structure
        exp_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(0.7 * x) * np.sin(1.3 * x))
        
        # Fractional-order chaotic sine mapping with additional modulation
        frac_chaos = np.sum(np.sin(np.exp(np.sin(1.8 * x)) * 0.5) + 
                           np.cos(np.exp(np.cos(1.6 * x)) * 0.4))
        
        # Harmonic cross-term coupling between dimensions
        cross_term = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # Cosine modulation with polynomial envelope
        cos_mod_term = np.sum(np.cos(2.9 * x) * (x**2.1 + 0.5))
        
        # Combined weighted sum with adjusted coefficients
        return 0.28 * poly_term + 0.25 * chaotic_coupling + 0.20 * trig_term + 0.15 * exp_term + 0.08 * frac_chaos + 0.03 * cross_term + 0.01 * cos_mod_term + 2.1
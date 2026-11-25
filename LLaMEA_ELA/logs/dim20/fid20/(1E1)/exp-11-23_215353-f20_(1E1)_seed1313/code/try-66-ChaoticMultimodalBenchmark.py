import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial distortion with varying exponents
        poly_term = np.sum((x**3.7 + 0.8 * x**2.5 - 0.3 * x**1.3 + 0.9 * x + 1.2)**1.4)
        
        # Chaotic sine-cosine mapping with nested trigonometric functions
        chaotic_term = np.sum(np.sin(np.cos(np.exp(1.2 * x))) + np.cos(np.sin(np.exp(1.1 * x))) + 
                             np.sin(np.sin(np.cos(0.9 * x))) + np.cos(np.cos(np.sin(1.3 * x))))
        
        # Adaptive frequency modulation with multiple harmonic components
        freq_mod_term = np.sum(np.sin(3.1 * x) * np.cos(2.7 * x) * np.sin(1.8 * x) * np.cos(0.5 * x))
        
        # Fractional exponential decay with sinusoidal modulation
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(1.9 * x) * np.cos(0.7 * x))
        
        # Multi-scale chaotic component with varying coupling strengths
        multi_scale_term = np.sum(np.sin(np.exp(np.sin(2.1 * x))) * np.cos(np.exp(np.cos(1.6 * x))) + 
                                np.cos(np.exp(np.cos(1.9 * x))) * np.sin(np.exp(np.sin(1.4 * x))))
        
        # Enhanced cosine modulation with quadratic scaling
        cos_mod_term = np.sum(np.cos(4.3 * x) * np.sin(0.6 * x**2) * np.exp(-0.2 * x**2))
        
        # Combined weighted sum with adjusted coefficients for increased complexity
        return 0.25 * poly_term + 0.22 * chaotic_term + 0.18 * freq_mod_term + 0.15 * exp_term + 0.12 * multi_scale_term + 0.08 * cos_mod_term + 2.1
import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial with varying exponents for each dimension
        poly_term = np.sum((x**2.7 + 0.8 * x**3.1 - 0.6 * x**1.9 + 0.9 * x**1.3 + 1.2)**1.4)
        
        # Enhanced chaotic component with nested sine-cosine mappings
        chaotic_term = np.sum(np.sin(np.cos(np.exp(1.5 * x))) + np.cos(np.sin(np.exp(1.7 * x))) + 
                             np.sin(np.sin(np.cos(2.1 * x))) + np.cos(np.cos(np.sin(1.9 * x))))
        
        # Cross-dimensional interaction terms with trigonometric modulation
        cross_term = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.5 * (x[:-1]**2 + x[1:]**2)))
        
        # Multi-frequency harmonic distortion with exponential decay
        harm_term = np.sum(np.sin(3.8 * x) * np.cos(5.2 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Fractional chaotic sine-cosine with time-varying modulation
        frac_chaotic = np.sum(np.sin(np.exp(np.sin(1.2 * x)) + np.cos(np.exp(1.1 * x))) + 
                             np.cos(np.exp(np.cos(1.3 * x)) + np.sin(np.exp(1.4 * x))))
        
        # Additional cosine modulation with polynomial envelope
        cos_mod_term = np.sum(np.cos(4.1 * x) * (1.0 + 0.3 * x**2.5))
        
        # Combine all terms with new optimized weights
        return 0.28 * poly_term + 0.25 * chaotic_term + 0.18 * cross_term + 0.15 * harm_term + 0.10 * frac_chaotic + 0.04 * cos_mod_term + 1.3
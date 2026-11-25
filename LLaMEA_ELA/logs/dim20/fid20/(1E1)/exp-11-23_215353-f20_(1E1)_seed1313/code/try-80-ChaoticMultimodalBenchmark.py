import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-cosine mapping with nested exponentials
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.7 * x))) + np.cos(np.exp(np.cos(1.9 * x))))
        
        # Adaptive polynomial with variable exponents and cross-terms
        poly_term = np.sum((x**4.2 + 0.8 * x**3.5 - 0.6 * x**2.3 + 0.9 * x**1.7 + 1.2)**1.3)
        
        # Multi-frequency trigonometric modulation with dynamic scaling
        trig_term = np.sum(np.sin(3.1 * x) * np.cos(5.3 * x) * np.sin(2.8 * x) * np.cos(4.2 * x))
        
        # Exponential decay with cosine modulation for additional complexity
        exp_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(0.7 * x))
        
        # Novel harmonic distortion using cubic and quartic terms
        harm_term = np.sum(np.sin(6.1 * x**3) * np.cos(3.4 * x**4))
        
        # New cosine modulation with quadratic argument for increased multimodality
        cos_mod_term = np.sum(np.cos(2.9 * x**2) * np.sin(0.9 * x))
        
        # Cross-dimensional interaction terms for enhanced complexity
        cross_term = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Combine all terms with optimized weights
        return 0.28 * chaotic_term + 0.22 * poly_term + 0.20 * trig_term + 0.15 * exp_term + 0.08 * harm_term + 0.04 * cos_mod_term + 0.03 * cross_term + 1.4
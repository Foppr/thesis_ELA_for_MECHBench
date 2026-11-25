import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional polynomial with varying exponents for increased complexity
        poly_term = np.sum((x**3.7 + 0.8 * x**2.9 - 0.5 * x**1.4 + 0.9 * x + 1.2)**1.3)
        
        # Nested chaotic sine-cosine mappings with variable frequencies
        chaotic_term = np.sum(np.sin(np.cos(np.exp(1.2 * x))) + np.cos(np.sin(np.exp(1.1 * x))) + 
                              np.sin(np.sin(np.cos(1.5 * x))) + np.cos(np.cos(np.sin(1.6 * x))))
        
        # Adaptive Gaussian modulation with dynamic variance
        gauss_term = np.sum(np.exp(-0.5 * ((x - 1.0) / (0.5 + 0.3 * np.sin(2.0 * x)))**2) + 
                            np.exp(-0.5 * ((x + 1.0) / (0.6 + 0.4 * np.cos(1.8 * x)))**2))
        
        # Multi-frequency trigonometric combination with phase shifts
        trig_term = np.sum(np.sin(3.0 * x + 0.5 * np.sin(2.0 * x)) * 
                           np.cos(2.5 * x + 0.3 * np.cos(1.5 * x)) * 
                           np.sin(1.8 * x + 0.7 * np.sin(3.0 * x)))
        
        # Exponential decay with sinusoidal amplitude modulation
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * (1.0 + 0.2 * np.sin(4.0 * x)))
        
        # Additional harmonic and cosine modulation for enhanced multimodality
        harm_term = np.sum(np.sin(5.0 * x) * np.cos(0.9 * x**2) * np.exp(-0.1 * x**2))
        
        # New fractional chaotic component with modified nesting
        frac_chaotic = np.sum(np.sin(np.exp(np.sin(1.4 * x)) + np.cos(np.exp(1.3 * x))) + 
                              np.cos(np.exp(np.sin(1.6 * x)) - np.cos(np.exp(1.5 * x))))
        
        # Combine all terms with new optimized weights
        return 0.25 * poly_term + 0.20 * chaotic_term + 0.15 * gauss_term + 0.18 * trig_term + \
               0.12 * exp_term + 0.07 * harm_term + 0.03 * frac_chaotic + 1.4
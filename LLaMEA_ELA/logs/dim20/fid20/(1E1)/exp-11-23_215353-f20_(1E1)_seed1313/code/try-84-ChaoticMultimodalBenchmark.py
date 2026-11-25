import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-cosine mapping with nested exponential modulation
        chaotic_term = np.sum(np.sin(np.exp(np.cos(1.7 * x))) + np.cos(np.exp(np.sin(1.9 * x))) + 
                             np.sin(np.cos(np.exp(0.8 * x))) + np.cos(np.sin(np.exp(0.6 * x))))
        
        # Adaptive polynomial with variable exponents and cross-terms
        poly_term = np.sum((x**4.2 + 0.7 * x**3.1 - 0.5 * x**2.3 + 0.9 * x + 1.3)**1.2 + 
                          0.3 * x * np.sin(2.1 * x) * np.cos(1.4 * x))
        
        # Multi-frequency trigonometric modulation with dynamic amplitude
        trig_term = np.sum(np.sin(3.3 * x) * np.cos(5.2 * x) * np.exp(-0.15 * x**2) + 
                          np.cos(4.1 * x) * np.sin(6.7 * x) * np.exp(-0.12 * x**2))
        
        # Exponential decay with sinusoidal modulation for added complexity
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * (np.cos(0.9 * x) + 0.5 * np.sin(1.8 * x)))
        
        # Harmonic interference pattern with cosine modulation
        harm_term = np.sum(np.sin(7.4 * x) * np.cos(2.9 * x) * np.exp(-0.08 * x**2))
        
        # New quartic polynomial distortion with added sinusoidal perturbation
        quartic_term = np.sum((x**4.0 + 0.6 * x**3.5 - 0.3 * x**2.7 + 0.7 * x + 1.2)**1.3 + 
                             0.2 * np.sin(3.0 * x**2) * np.cos(1.1 * x))
        
        # Combine all terms with optimized weights
        return 0.28 * chaotic_term + 0.25 * poly_term + 0.18 * trig_term + 0.15 * exp_term + 0.07 * harm_term + 0.07 * quartic_term + 1.4
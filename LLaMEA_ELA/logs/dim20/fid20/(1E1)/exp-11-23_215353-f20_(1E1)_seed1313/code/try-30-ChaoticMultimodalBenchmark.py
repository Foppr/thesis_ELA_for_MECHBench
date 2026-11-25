import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential with double sine modulation
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(1.7 * np.pi * x) * np.cos(2.1 * np.pi * x))
        
        # Triple nested trigonometric functions with varying frequencies
        trig_term = np.sum(np.sin(3.2 * x) * np.cos(4.8 * x) * np.tan(1.9 * x))
        
        # High-order adaptive polynomial with fractional exponents and variable coefficients
        poly_term = np.sum((x**4.7 + 0.9 * x**3.8 - 0.5 * x**2.9 + 0.6 * x**1.7 + 1.4 * x + 1.1)**1.5)
        
        # Ultra-chaotic component with nested exponential and logarithmic distortions
        chaotic_term = np.sum(np.sin(np.exp(np.cos(1.8 * x))) + np.cos(np.exp(np.sin(1.6 * x))) + np.log(1.1 + np.abs(x)))
        
        # Multi-harmonic modulation with Gaussian envelope
        harm_term = np.sum(np.sin(5.3 * x) * np.cos(7.1 * x) * np.exp(-0.15 * x**2))
        
        # Additional quadratic distortion layer for increased curvature
        quad_term = np.sum(0.4 * x**2 + 0.3 * x + 0.8)
        
        # Combine all terms with new optimized weights
        return 0.32 * exp_term + 0.25 * trig_term + 0.20 * poly_term + 0.15 * chaotic_term + 0.05 * harm_term + 0.03 * quad_term + 1.7
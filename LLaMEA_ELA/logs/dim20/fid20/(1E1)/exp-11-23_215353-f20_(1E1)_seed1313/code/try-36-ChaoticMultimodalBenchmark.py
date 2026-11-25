import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling and chaotic modulation
        exp_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(0.7 * x) * np.sin(0.3 * x))
        
        # Nested trigonometric modulation with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(3.0 * np.pi * x) * np.cos(7.0 * np.pi * x) * np.sin(2.0 * np.pi * x) * np.cos(1.0 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents and chaotic coefficients
        poly_term = np.sum((x**4.0 + 0.9 * x**3.0 - 0.4 * x**2.0 + 0.8 * x + 1.5)**1.5)
        
        # Enhanced chaotic component using deeply nested sine and exponential functions
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.5 * x))) + np.cos(np.exp(np.cos(1.6 * x))) + np.tan(0.5 * x))
        
        # Additional harmonic modulation with Gaussian envelope for increased multimodality
        harm_term = np.sum(np.sin(5.0 * x) * np.exp(-0.15 * x**2) * np.cos(0.8 * x))
        
        # Cross-term interaction for higher dimensional complexity
        cross_term = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Combine all terms with optimized weights
        return 0.32 * exp_term + 0.25 * trig_term + 0.20 * poly_term + 0.15 * chaotic_term + 0.04 * harm_term + 0.04 * cross_term + 1.7
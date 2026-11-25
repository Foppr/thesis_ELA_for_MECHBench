import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(0.7 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2.8 * np.pi * x) * np.cos(5.5 * np.pi * x) * np.sin(1.8 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents
        poly_term = np.sum((x**3.7 + 0.9 * x**2.3 - 0.2 * x**1.7 + 0.6 * x + 1.1)**1.4)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.1 * x))) + np.cos(np.exp(np.cos(1.4 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.2 * x) * np.exp(-0.15 * x**2))
        
        # Add a new component: fractional Brownian motion inspired term
        fbm_term = np.sum(np.sin(3.0 * x + 0.5 * np.sin(2.0 * x)) * np.cos(0.8 * x))
        
        # Combine all terms with optimized weights
        return 0.32 * exp_term + 0.26 * trig_term + 0.24 * poly_term + 0.10 * chaotic_term + 0.04 * harm_term + 0.04 * fbm_term + 1.5
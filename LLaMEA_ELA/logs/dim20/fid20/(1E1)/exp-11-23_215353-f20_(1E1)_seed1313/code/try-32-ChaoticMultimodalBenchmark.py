import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.35 * np.abs(x)) * np.cos(0.7 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2.7 * np.pi * x) * np.cos(5.8 * np.pi * x) * np.sin(1.3 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents
        poly_term = np.sum((x**3.7 + 0.7 * x**2.3 - 0.2 * x**1.7 + 0.6 * x + 1.1)**1.2)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.1 * x))) + np.cos(np.exp(np.cos(1.4 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.2 * x) * np.exp(-0.15 * x**2))
        
        # Combine all terms with optimized weights
        return 0.37 * exp_term + 0.26 * trig_term + 0.24 * poly_term + 0.11 * chaotic_term + 0.02 * harm_term + 1.55
import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.4 * np.abs(x)) * np.cos(0.6 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2.5 * np.pi * x) * np.cos(6 * np.pi * x) * np.sin(1.5 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents
        poly_term = np.sum((x**3.5 + 0.8 * x**2.5 - 0.3 * x**1.5 + 0.7 * x + 1.2)**1.3)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.2 * x))) + np.cos(np.exp(np.cos(1.3 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.5 * x) * np.exp(-0.12 * x**2))
        
        # Combine all terms with optimized weights
        return 0.35 * exp_term + 0.28 * trig_term + 0.22 * poly_term + 0.12 * chaotic_term + 0.03 * harm_term + 1.6
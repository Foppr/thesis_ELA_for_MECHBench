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
        
        # Adaptive polynomial distortion with variable exponents (slightly modified)
        poly_term = np.sum((x**3.7 + 0.9 * x**2.7 - 0.4 * x**1.7 + 0.8 * x + 1.1)**1.2)
        
        # Enhanced chaotic component using nested sine and exponential (slightly modified)
        chaotic_term = np.sum(np.sin(np.exp(np.sin(1.3 * x))) + np.cos(np.exp(np.cos(1.4 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.7 * x) * np.exp(-0.13 * x**2))
        
        # Combine all terms with optimized weights (slightly adjusted)
        return 0.33 * exp_term + 0.30 * trig_term + 0.20 * poly_term + 0.11 * chaotic_term + 0.06 * harm_term + 1.5
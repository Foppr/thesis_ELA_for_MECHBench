import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with adaptive scaling
        exp_term = np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(0.5 * x))
        
        # Nested trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(3 * np.pi * x) * np.cos(7 * np.pi * x) * np.sin(2 * np.pi * x))
        
        # Adaptive polynomial distortion with variable exponents
        poly_term = np.sum((x**4 + 0.7 * x**3 - 0.4 * x**2 + 0.6 * x + 1.0)**1.5)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(np.sin(x))) + np.cos(np.exp(np.cos(x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(5 * x) * np.exp(-0.1 * x**2))
        
        # Combine all terms with optimized weights
        return 0.4 * exp_term + 0.25 * trig_term + 0.2 * poly_term + 0.1 * chaotic_term + 0.05 * harm_term + 1.5
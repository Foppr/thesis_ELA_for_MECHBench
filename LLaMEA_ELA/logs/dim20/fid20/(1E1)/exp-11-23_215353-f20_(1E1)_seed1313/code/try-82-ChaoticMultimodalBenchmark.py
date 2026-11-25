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
        poly_term = np.sum((x**3.9 + 0.9 * x**2.8 - 0.4 * x**1.6 + 0.8 * x + 1.1)**1.1)
        
        # Enhanced chaotic component using nested hyperbolic functions (modified)
        chaotic_term = np.sum(np.sinh(np.exp(np.cos(1.3 * x))) + np.cosh(np.exp(np.sin(1.4 * x))))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(4.7 * x) * np.exp(-0.13 * x**2))
        
        # New cosine modulation term to increase landscape complexity
        cos_mod_term = np.sum(np.cos(3.2 * x) * np.sin(0.8 * x**2))
        
        # Additional hyperbolic tangent modulation for increased complexity
        tanh_mod_term = np.sum(np.tanh(2.1 * x) * np.cos(0.5 * x**3))
        
        # Combine all terms with optimized weights (slightly adjusted)
        return 0.30 * exp_term + 0.28 * trig_term + 0.18 * poly_term + 0.14 * chaotic_term + 0.06 * harm_term + 0.03 * cos_mod_term + 0.01 * tanh_mod_term + 1.5
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
        
        # Adaptive polynomial distortion with variable exponents (slightly modified)
        poly_term = np.sum((x**4.1 + 0.8 * x**2.9 - 0.3 * x**1.7 + 0.9 * x + 1.2)**1.05)
        
        # Enhanced chaotic component using nested hyperbolic sine and cosine functions
        chaotic_term = np.sum(np.sinh(np.cos(1.4 * x)) + np.cosh(np.sin(1.5 * x)))
        
        # Additional harmonic modulation for increased multimodality
        harm_term = np.sum(np.sin(5.2 * x) * np.exp(-0.15 * x**2))
        
        # New cosine modulation term to increase landscape complexity
        cos_mod_term = np.sum(np.cos(3.5 * x) * np.sin(0.9 * x**2))
        
        # Additional hyperbolic tangent modulation for enhanced landscape curvature
        tanh_term = np.sum(np.tanh(0.6 * x) * np.cos(2.1 * x))
        
        # Introduce a new nested chaotic structure with higher frequency oscillations
        nested_chaos = np.sum(np.sin(np.cos(np.sin(3.0 * x))) * np.cos(np.sinh(1.2 * x)))
        
        # Add a fractional power component to increase conditioning difficulty
        frac_power = np.sum((np.abs(x) + 0.5)**0.7 * np.sin(4.0 * x))
        
        # Combine all terms with optimized weights (slightly adjusted)
        return 0.28 * exp_term + 0.25 * trig_term + 0.18 * poly_term + 0.12 * chaotic_term + 0.05 * harm_term + 0.03 * cos_mod_term + 0.02 * tanh_term + 0.04 * nested_chaos + 0.02 * frac_power + 1.4
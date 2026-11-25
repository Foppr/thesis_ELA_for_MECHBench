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
        
        # Introduce a new fractional polynomial term with adaptive exponents to improve conditioning
        frac_poly_term = np.sum((x**3.7 + 0.5 * x**2.3 - 0.4 * x**1.2 + 0.8 * x + 1.1)**1.1)
        
        # Add a modified Gaussian-like term to create additional local minima
        gaussian_term = np.sum(np.exp(-0.2 * x**2) * np.sin(3.0 * x))
        
        # Combine all terms with optimized weights (slightly adjusted)
        return 0.28 * exp_term + 0.25 * trig_term + 0.18 * poly_term + 0.12 * chaotic_term + 0.07 * harm_term + 0.03 * cos_mod_term + 0.02 * tanh_term + 0.04 * frac_poly_term + 0.01 * gaussian_term + 1.4
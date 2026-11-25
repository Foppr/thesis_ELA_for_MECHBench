import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with nested hyperbolic functions and fractal-like mappings
        chaotic_term = np.sum(np.sinh(np.cos(np.tanh(2.3 * x))) + np.cosh(np.sin(np.exp(-0.7 * x))))
        
        # Multi-scale trigonometric modulation with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(3.1 * x) * np.cos(4.2 * x) * np.sin(1.9 * x) * np.cos(2.8 * x))
        
        # Polynomial distortion with non-integer exponents and dynamic scaling factors
        poly_term = np.sum((x**3.7 + 0.6 * x**2.3 - 0.4 * x**1.5 + 0.8 * x + 1.1)**1.2)
        
        # Adaptive exponential decay with sinusoidal perturbations
        exp_term = np.sum(np.exp(-0.5 * np.abs(x)) * np.cos(1.3 * x) * np.sin(0.9 * x))
        
        # Additional harmonic modulation with time-varying coefficients
        harm_term = np.sum(np.sin(6.7 * x) * np.exp(-0.2 * x**2) * np.cos(1.1 * x))
        
        # Cosine modulation with quadratic phase shift for increased complexity
        cos_mod_term = np.sum(np.cos(4.3 * x + 0.5 * x**2) * np.sin(1.4 * x))
        
        # Hyperbolic tangent with multi-dimensional coupling
        tanh_term = np.sum(np.tanh(0.8 * x) * np.cos(3.2 * x) * np.sin(0.6 * x))
        
        # Nested chaotic sine-cosine mapping for enhanced multimodality
        nested_term = np.sum(np.sin(np.cos(np.sin(1.7 * x))) + np.cos(np.sin(np.cos(2.1 * x))))
        
        # Combine all terms with adjusted weights for maximum landscape complexity
        return 0.28 * exp_term + 0.22 * trig_term + 0.18 * poly_term + 0.15 * chaotic_term + 0.08 * harm_term + 0.05 * cos_mod_term + 0.03 * tanh_term + 0.01 * nested_term + 1.6
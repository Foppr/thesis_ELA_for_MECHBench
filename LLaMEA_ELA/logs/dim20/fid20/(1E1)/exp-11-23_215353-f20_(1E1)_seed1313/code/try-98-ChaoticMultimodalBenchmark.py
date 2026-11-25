import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with nested hyperbolic functions and fractal-like structure
        chaotic_term = np.sum(np.sinh(np.cos(np.tanh(1.7 * x))) + np.cosh(np.sin(np.exp(-0.5 * x))))
        
        # Multi-scale trigonometric modulation with adaptive frequencies
        trig_term = np.sum(np.sin(3.2 * np.pi * x) * np.cos(4.8 * np.pi * x) * np.sin(1.9 * np.pi * x) * np.cos(0.7 * np.pi * x))
        
        # Polynomial distortion with variable exponents and cross-dimensional coupling
        poly_term = np.sum((x**5.3 + 0.9 * x**3.8 - 0.4 * x**2.6 + 0.7 * x + 1.5)**1.15)
        
        # Adaptive exponential decay with sinusoidal perturbations
        exp_term = np.sum(np.exp(-0.4 * np.abs(x)) * np.cos(0.9 * x) * np.sin(1.3 * x))
        
        # Additional harmonic modulation with dynamic amplitude
        harm_term = np.sum(np.sin(6.1 * x) * np.exp(-0.2 * x**2) * np.cos(1.1 * x))
        
        # Cosine modulation with quadratic phase shift
        cos_mod_term = np.sum(np.cos(4.3 * x + 0.5 * x**2) * np.sin(0.8 * x))
        
        # Hyperbolic tangent with multi-frequency sinusoidal modulation
        tanh_term = np.sum(np.tanh(0.7 * x) * np.cos(2.5 * x) * np.sin(1.2 * x))
        
        # Cross-dimensional coupling term for increased complexity
        cross_term = np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        # Combine all terms with adjusted weights for enhanced multimodality
        return 0.28 * exp_term + 0.25 * trig_term + 0.18 * poly_term + 0.15 * chaotic_term + 0.07 * harm_term + 0.04 * cos_mod_term + 0.03 * tanh_term + 0.02 * cross_term + 1.6
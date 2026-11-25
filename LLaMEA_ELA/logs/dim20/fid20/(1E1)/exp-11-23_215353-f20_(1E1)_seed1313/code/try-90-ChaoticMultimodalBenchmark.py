import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with double nested hyperbolic functions
        chaotic_term = np.sum(np.sinh(np.cos(np.tanh(2.3 * x))) + np.cosh(np.sin(np.exp(0.8 * x))))
        
        # Multi-frequency trigonometric cascade with adaptive amplitudes
        trig_term = np.sum(np.sin(3.7 * x) * np.cos(4.2 * x) * np.sin(1.9 * x) * np.cos(2.8 * x))
        
        # Adaptive polynomial with variable exponents and chaotic scaling
        poly_term = np.sum((x**5.3 + 0.6 * x**3.8 - 0.4 * x**2.1 + 0.7 * x + 1.5)**1.15)
        
        # Nested exponential with sinusoidal modulation for enhanced curvature
        exp_term = np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(3.1 * x) * np.cos(1.6 * x))
        
        # Additional harmonic series with chaotic phase shifts
        harm_term = np.sum(np.sin(6.5 * x) * np.cos(2.3 * x) * np.exp(-0.2 * x**2))
        
        # Cosine modulation with quadratic distortion and chaotic frequency
        cos_mod_term = np.sum(np.cos(4.1 * x**2) * np.sin(1.2 * x) * np.tanh(0.5 * x))
        
        # Hyperbolic tangent with multi-modal sinusoidal component
        tanh_term = np.sum(np.tanh(0.7 * x) * np.sin(3.9 * x) * np.cos(1.4 * x))
        
        # Combined weighted landscape with increased complexity and multimodality
        return 0.28 * exp_term + 0.25 * trig_term + 0.22 * poly_term + 0.15 * chaotic_term + 0.07 * harm_term + 0.04 * cos_mod_term + 0.02 * tanh_term + 1.6
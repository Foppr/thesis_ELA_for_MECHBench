import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with multiple iterations
        tent_map = np.sum(np.where(x < 0, 2 * x, 2 * (1 - x)))
        
        # Enhanced nested hyperbolic functions with variable coefficients
        hyperbolic_term = np.sum(np.sinh(2.3 * np.cos(1.7 * x)) + np.cosh(1.9 * np.sin(2.1 * x)) + np.tanh(0.8 * x**3))
        
        # Multi-frequency sinusoidal modulation with exponential decay
        trig_mod = np.sum(np.sin(3.2 * np.pi * x) * np.cos(4.7 * np.pi * x) * np.exp(-0.2 * x**2) * np.sin(1.3 * np.pi * x))
        
        # Adaptive polynomial with dynamic exponents and multiple terms
        poly_term = np.sum((x**5.3 + 1.2 * x**3.8 - 0.7 * x**2.4 + 0.5 * x**1.2 + 1.8)**1.15)
        
        # Complex harmonic interference pattern
        harm_pattern = np.sum(np.sin(6.1 * x) * np.cos(3.9 * x) * np.sin(2.7 * x) * np.exp(-0.1 * x**2))
        
        # Cosine modulation with quadratic distortion
        cos_mod = np.sum(np.cos(4.3 * x) * np.sin(1.1 * x**2) * np.exp(-0.3 * x**2))
        
        # Additional chaotic sine-cosine coupling
        coupled_chn = np.sum(np.sin(np.cos(2.5 * x)) + np.cos(np.sin(1.8 * x)) + np.tanh(0.5 * x**4))
        
        # Quadratic polynomial with adaptive scaling and offset
        quad_term = np.sum(0.6 * x**2 + 0.3 * x + 0.9)
        
        # Combine all terms with new optimized weights
        return 0.28 * tent_map + 0.25 * hyperbolic_term + 0.18 * trig_mod + 0.12 * poly_term + 0.07 * harm_pattern + 0.06 * cos_mod + 0.05 * coupled_chn + 0.04 * quad_term + 1.3
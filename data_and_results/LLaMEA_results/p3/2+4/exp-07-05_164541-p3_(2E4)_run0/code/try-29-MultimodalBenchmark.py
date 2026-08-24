import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillation terms with modified fractional exponents
        chaotic_term = np.sum(np.sin(np.pi * x**1.9) * np.cos(np.pi * x**1.1) * np.exp(-0.3 * np.abs(x)))
        
        # Fractional polynomial interactions with altered non-integer powers
        frac_poly_term = np.sum(0.4 * x**3.7 - 2.3 * x**2.6 + 4.5 * x**1.8 - 2.1 * x**0.6)
        
        # Cross-dimensional coupling with modified sine and cosine products
        coupling_term = np.sum(np.sin(np.pi * (x[:-1] + x[1:]) * 1.2) * np.cos(np.pi * (x[:-1] - x[1:]) * 0.8) * 
                              (x[:-1]**2.2 + x[1:]**1.8))
        
        # Enhanced exponential decay with modified argument
        exp_decay_term = np.sum(np.exp(-0.15 * (x**2 + 0.3 * np.sin(6 * x)**2)) * np.cos(2.5 * np.pi * x))
        
        # High-frequency trigonometric oscillations with altered frequencies
        high_freq_term = np.sum(np.sin(12 * np.pi * x) * np.cos(6 * np.pi * x) + 
                               np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Combine all terms with updated weights
        return 0.25 * chaotic_term + 0.18 * frac_poly_term + 0.12 * coupling_term + 0.09 * exp_decay_term + 0.06 * high_freq_term + 2.2
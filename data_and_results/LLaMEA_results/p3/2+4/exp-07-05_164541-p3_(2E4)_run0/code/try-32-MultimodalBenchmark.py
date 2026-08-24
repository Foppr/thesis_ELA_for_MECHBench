import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillation terms with fractional exponents
        chaotic_term = np.sum(np.sin(np.pi * x**1.7) * np.cos(np.pi * x**1.3) * np.exp(-0.5 * np.abs(x)))
        
        # Fractional polynomial interactions with non-integer powers
        frac_poly_term = np.sum(0.3 * x**3.5 - 2.1 * x**2.8 + 4.2 * x**1.9 - 1.8 * x**0.7)
        
        # Cross-dimensional coupling with sine and cosine products
        coupling_term = np.sum(np.sin(np.pi * (x[:-1] + x[1:])) * np.cos(np.pi * (x[:-1] - x[1:])) * 
                              (x[:-1]**2 + x[1:]**2))
        
        # Enhanced exponential decay with complex argument
        exp_decay_term = np.sum(np.exp(-0.2 * (x**2 + 0.5 * np.sin(5 * x)**2)) * np.cos(3 * np.pi * x))
        
        # High-frequency trigonometric oscillations
        high_freq_term = np.sum(np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x) + 
                               np.sin(7 * np.pi * x) * np.cos(9 * np.pi * x))
        
        # Combine all terms with optimized weights
        return 0.2 * chaotic_term + 0.15 * frac_poly_term + 0.1 * coupling_term + 0.08 * exp_decay_term + 0.05 * high_freq_term + 2.0
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity using recursive sine and cosine combinations
        fractal_term = np.sum(np.sin(2 ** (np.arange(self.dim) + 1) * np.pi * x) * 
                             np.cos(2 ** (np.arange(self.dim) + 1) * np.pi * x))
        
        # Dynamic frequency modulation with time-varying coefficients
        freq_mod_term = np.sum(np.sin((1 + 0.5 * np.sin(0.1 * x)) * 10 * np.pi * x) * 
                              np.cos((1 + 0.3 * np.cos(0.15 * x)) * 8 * np.pi * x))
        
        # Adaptive polynomial interactions with dimension-dependent exponents
        poly_interaction = np.sum((x ** (2 + np.arange(self.dim) % 5)) * 
                                 np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Non-stationary landscape with spatially varying amplitude and frequency
        non_stationary_term = np.sum(np.exp(-0.1 * x**2) * 
                                    np.sin(15 * np.pi * x + 0.5 * np.sin(2 * np.pi * x)) * 
                                    np.cos(12 * np.pi * x + 0.3 * np.cos(1.5 * np.pi * x)))
        
        # Cross-dimensional coupling with varying interaction strengths
        coupling_term = np.sum(np.abs(x[:-1] - x[1:]) ** (1.5 + np.abs(x[:-1]) / 5.0) * 
                              np.sin(7 * np.pi * (x[:-1] + x[1:])) * 
                              np.cos(4 * np.pi * (x[:-1] - x[1:])))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.25 * fractal_term + 0.15 * freq_mod_term + 0.1 * poly_interaction + \
               0.2 * non_stationary_term + 0.1 * coupling_term + 1.8
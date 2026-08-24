import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity using recursive sine and cosine combinations
        fractal_term = np.sum(np.sin(np.pi * x * np.sin(2 * np.pi * x)) * 
                             np.cos(np.pi * x * np.cos(2 * np.pi * x)) * 
                             np.sin(np.pi * x * np.sin(3 * np.pi * x)) * 
                             np.cos(np.pi * x * np.cos(3 * np.pi * x)))
        
        # Memory-dependent interactions with delayed feedback terms
        memory_term = np.sum((x[:-1] - 0.5 * x[:-2])**4 * np.sin(15 * np.pi * x[:-1]) * 
                            np.cos(13 * np.pi * x[:-2]) * 
                            np.sin(11 * np.pi * x[:-1]) * np.cos(9 * np.pi * x[:-2]))
        
        # Hybrid chaotic-polynomial dynamics combining high-frequency oscillations with polynomial terms
        hybrid_term = np.sum(1.5 * x**12 - 12 * x**10 + 19 * x**8 - 17 * x**6 + 14 * x**4 - 11 * x**2 + 
                            8 * np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                            np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x))
        
        # Cross-dimensional correlations with varying interaction strengths and phase shifts
        cross_term = np.sum((x[:-1] * x[1:] + 0.5 * x[:-1]**2 * x[1:]**2)**3 * 
                           np.sin(17 * np.pi * x[:-1]) * np.cos(15 * np.pi * x[1:]) * 
                           np.sin(13 * np.pi * x[:-1]) * np.cos(11 * np.pi * x[1:]))
        
        # Multi-scale exponential modulation with oscillatory behavior
        exp_mod_term = np.sum(np.exp(-0.3 * x**2) * np.sin(20 * np.pi * x) * 
                             np.cos(18 * np.pi * x) * np.sin(16 * np.pi * x) * 
                             np.cos(14 * np.pi * x) * np.sin(12 * np.pi * x) * 
                             np.cos(10 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.4 * fractal_term + 0.12 * memory_term + 0.2 * hybrid_term + 0.18 * cross_term + 0.25 * exp_mod_term + 4.2
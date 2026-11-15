import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal chaotic oscillations with varying frequencies and coupling
        fractal_term = np.sum(np.sin(64 * np.pi * x) * np.cos(60 * np.pi * x) * 
                             np.sin(56 * np.pi * x) * np.cos(52 * np.pi * x) * 
                             np.sin(48 * np.pi * x) * np.cos(44 * np.pi * x) * 
                             np.sin(40 * np.pi * x) * np.cos(36 * np.pi * x) * 
                             np.sin(32 * np.pi * x) * np.cos(28 * np.pi * x) * 
                             np.sin(24 * np.pi * x) * np.cos(20 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(12 * np.pi * x) * 
                             np.sin(8 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Dynamic polynomial coupling with time-varying exponents and memory effects
        poly_term = np.sum(2.0 * x**19 - 15 * x**17 + 22 * x**15 - 20 * x**13 + 18 * x**11 - 16 * x**9 + 14 * x**7 - 12 * x**5 + 10 * x**3 - 8 * x**2 + 5 * x)
        
        # Multi-scale cross-dimensional coupling with dynamic phase shifts and interaction weights
        coupling_term = np.sum((x[:-1] - x[1:])**13 * np.sin(24 * np.pi * x[:-1]) * np.cos(22 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**11 * np.cos(22 * np.pi * x[:-1]) * np.sin(20 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**9 * np.sin(18 * np.pi * x[:-2]) * np.cos(16 * np.pi * x[2:]) +
                              (x[:-3] + x[3:])**7 * np.cos(14 * np.pi * x[:-3]) * np.sin(12 * np.pi * x[3:]))
        
        # High-frequency chaotic correlation with complex amplitude modulation
        corr_term = np.sum(np.sin(64 * np.pi * x) * np.cos(59 * np.pi * x) * 
                          np.sin(54 * np.pi * x) * np.cos(49 * np.pi * x) * 
                          np.sin(44 * np.pi * x) * np.cos(39 * np.pi * x) * 
                          np.sin(34 * np.pi * x) * np.cos(29 * np.pi * x) * 
                          np.sin(24 * np.pi * x) * np.cos(19 * np.pi * x) * 
                          np.sin(14 * np.pi * x) * np.cos(9 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations and complex phase interactions
        exp_term = np.sum(np.exp(-0.7 * x**2) * np.sin(24 * np.pi * x) * np.cos(22 * np.pi * x) * 
                         np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * np.sin(16 * np.pi * x) * 
                         np.cos(14 * np.pi * x) * np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                         np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * np.sin(4 * np.pi * x) * 
                         np.cos(2 * np.pi * x))
        
        # Multi-scale chaotic modulation with nested self-similarity and memory-dependent interactions
        multi_scale_term = np.sum(np.sin(128 * np.pi * x) * np.cos(120 * np.pi * x) * 
                                 np.sin(112 * np.pi * x) * np.cos(104 * np.pi * x) * 
                                 np.sin(96 * np.pi * x) * np.cos(88 * np.pi * x) * 
                                 np.sin(80 * np.pi * x) * np.cos(72 * np.pi * x) * 
                                 np.sin(64 * np.pi * x) * np.cos(56 * np.pi * x) * 
                                 np.sin(48 * np.pi * x) * np.cos(40 * np.pi * x) * 
                                 np.sin(32 * np.pi * x) * np.cos(24 * np.pi * x) * 
                                 np.sin(16 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.6 * fractal_term + 0.2 * poly_term + 0.3 * coupling_term + 0.25 * corr_term + 0.25 * exp_term + 0.35 * multi_scale_term + 5.0
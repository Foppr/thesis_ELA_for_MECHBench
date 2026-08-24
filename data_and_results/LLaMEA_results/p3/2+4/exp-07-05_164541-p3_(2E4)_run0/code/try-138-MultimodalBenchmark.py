import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and added sinusoidal modulation
        chaotic_term = np.sum(np.sin(32 * np.pi * x) * np.cos(30 * np.pi * x) * 
                             np.sin(28 * np.pi * x) * np.cos(26 * np.pi * x) * 
                             np.sin(24 * np.pi * x) * np.cos(22 * np.pi * x) * 
                             np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x))
        
        # Modified polynomial coupling with altered exponents and added memory-dependent terms
        poly_term = np.sum(1.5 * x**17 - 13 * x**15 + 20 * x**13 - 18 * x**11 + 16 * x**9 - 14 * x**7 + 12 * x**5 - 9 * x**3 + 6 * x**2 - 3 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**11 * np.sin(20 * np.pi * x[:-1]) * np.cos(18 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**9 * np.cos(18 * np.pi * x[:-1]) * np.sin(16 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**7 * np.sin(14 * np.pi * x[:-2]) * np.cos(12 * np.pi * x[2:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(32 * np.pi * x) * np.cos(29 * np.pi * x) * 
                          np.sin(26 * np.pi * x) * np.cos(23 * np.pi * x) * 
                          np.sin(20 * np.pi * x) * np.cos(17 * np.pi * x) * 
                          np.sin(14 * np.pi * x) * np.cos(11 * np.pi * x) * 
                          np.sin(8 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                         np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * np.sin(12 * np.pi * x) * 
                         np.cos(10 * np.pi * x) * np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Introduce new multi-scale chaotic modulation and adjust weights for better fitness
        multi_scale_term = np.sum(np.sin(64 * np.pi * x) * np.cos(58 * np.pi * x) * 
                                 np.sin(52 * np.pi * x) * np.cos(46 * np.pi * x) * 
                                 np.sin(40 * np.pi * x) * np.cos(34 * np.pi * x) * 
                                 np.sin(28 * np.pi * x) * np.cos(22 * np.pi * x) * 
                                 np.sin(16 * np.pi * x) * np.cos(10 * np.pi * x))
        
        # Introduce additional fractal-like self-similarity with recursive scaling and enhanced memory effects
        fractal_term = np.sum(np.sin(128 * np.pi * x) * np.cos(120 * np.pi * x) * 
                             np.sin(112 * np.pi * x) * np.cos(104 * np.pi * x) * 
                             np.sin(96 * np.pi * x) * np.cos(88 * np.pi * x) * 
                             np.sin(80 * np.pi * x) * np.cos(72 * np.pi * x) * 
                             np.sin(64 * np.pi * x) * np.cos(56 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.5 * chaotic_term + 0.15 * poly_term + 0.25 * coupling_term + 0.2 * corr_term + 0.2 * exp_term + 0.3 * multi_scale_term + 0.25 * fractal_term + 4.0
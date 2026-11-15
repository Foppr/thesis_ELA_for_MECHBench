import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and added sinusoidal modulation
        chaotic_term = np.sum(np.sin(64 * np.pi * x) * np.cos(60 * np.pi * x) * 
                             np.sin(56 * np.pi * x) * np.cos(52 * np.pi * x) * 
                             np.sin(48 * np.pi * x) * np.cos(44 * np.pi * x) * 
                             np.sin(40 * np.pi * x) * np.cos(36 * np.pi * x) * 
                             np.sin(32 * np.pi * x) * np.cos(28 * np.pi * x))
        
        # Modified polynomial coupling with altered exponents and added memory-dependent terms
        poly_term = np.sum(2.0 * x**19 - 15 * x**17 + 22 * x**15 - 20 * x**13 + 18 * x**11 - 16 * x**9 + 14 * x**7 - 12 * x**5 + 10 * x**3 - 7 * x**2 + 4 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**13 * np.sin(22 * np.pi * x[:-1]) * np.cos(20 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**11 * np.cos(20 * np.pi * x[:-1]) * np.sin(18 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**9 * np.sin(16 * np.pi * x[:-2]) * np.cos(14 * np.pi * x[2:]) +
                              (x[:-3] + x[3:])**7 * np.cos(12 * np.pi * x[:-3]) * np.sin(10 * np.pi * x[3:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(64 * np.pi * x) * np.cos(59 * np.pi * x) * 
                          np.sin(54 * np.pi * x) * np.cos(49 * np.pi * x) * 
                          np.sin(44 * np.pi * x) * np.cos(39 * np.pi * x) * 
                          np.sin(34 * np.pi * x) * np.cos(29 * np.pi * x) * 
                          np.sin(24 * np.pi * x) * np.cos(19 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.7 * x**2) * np.sin(22 * np.pi * x) * np.cos(20 * np.pi * x) * 
                         np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * np.sin(14 * np.pi * x) * 
                         np.cos(12 * np.pi * x) * np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Introduce new multi-scale chaotic modulation and adjust weights for better fitness
        multi_scale_term = np.sum(np.sin(128 * np.pi * x) * np.cos(122 * np.pi * x) * 
                                 np.sin(116 * np.pi * x) * np.cos(110 * np.pi * x) * 
                                 np.sin(104 * np.pi * x) * np.cos(98 * np.pi * x) * 
                                 np.sin(92 * np.pi * x) * np.cos(86 * np.pi * x) * 
                                 np.sin(80 * np.pi * x) * np.cos(74 * np.pi * x))
        
        # Introduce additional fractal-like self-similarity with recursive scaling and enhanced memory effects
        fractal_term = np.sum(np.sin(256 * np.pi * x) * np.cos(248 * np.pi * x) * 
                             np.sin(240 * np.pi * x) * np.cos(232 * np.pi * x) * 
                             np.sin(224 * np.pi * x) * np.cos(216 * np.pi * x) * 
                             np.sin(208 * np.pi * x) * np.cos(200 * np.pi * x) * 
                             np.sin(192 * np.pi * x) * np.cos(184 * np.pi * x))
        
        # Add novel memory-dependent interaction terms with complex phase coupling
        memory_term = np.sum(np.sin(32 * np.pi * x) * np.cos(30 * np.pi * x) * 
                            np.sin(28 * np.pi * x) * np.cos(26 * np.pi * x) * 
                            np.sin(24 * np.pi * x) * np.cos(22 * np.pi * x) * 
                            np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                            np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * 
                            np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.6 * chaotic_term + 0.2 * poly_term + 0.3 * coupling_term + 0.25 * corr_term + 0.25 * exp_term + 0.35 * multi_scale_term + 0.3 * fractal_term + 0.2 * memory_term + 5.0
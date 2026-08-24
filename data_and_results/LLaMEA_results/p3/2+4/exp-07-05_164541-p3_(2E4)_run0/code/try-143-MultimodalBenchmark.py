import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and added sinusoidal modulation
        chaotic_term = np.sum(np.sin(33 * np.pi * x) * np.cos(31 * np.pi * x) * 
                             np.sin(29 * np.pi * x) * np.cos(27 * np.pi * x) * 
                             np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                             np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * 
                             np.sin(17 * np.pi * x) * np.cos(15 * np.pi * x))
        
        # Modified polynomial coupling with altered exponents and added memory-dependent terms
        poly_term = np.sum(1.6 * x**18 - 13.5 * x**14 + 20.5 * x**12 - 18.5 * x**10 + 16.5 * x**8 - 14.5 * x**6 + 12.5 * x**4 - 9.5 * x**2 + 6.5 * x**1 - 3.5 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**12 * np.sin(21 * np.pi * x[:-1]) * np.cos(19 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**10 * np.cos(19 * np.pi * x[:-1]) * np.sin(17 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**8 * np.sin(15 * np.pi * x[:-2]) * np.cos(13 * np.pi * x[2:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(33 * np.pi * x) * np.cos(30 * np.pi * x) * 
                          np.sin(27 * np.pi * x) * np.cos(24 * np.pi * x) * 
                          np.sin(21 * np.pi * x) * np.cos(18 * np.pi * x) * 
                          np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) * 
                          np.sin(9 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * 
                         np.sin(17 * np.pi * x) * np.cos(15 * np.pi * x) * np.sin(13 * np.pi * x) * 
                         np.cos(11 * np.pi * x) * np.sin(9 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Introduce new multi-scale chaotic modulation and adjust weights for better fitness
        multi_scale_term = np.sum(np.sin(65 * np.pi * x) * np.cos(59 * np.pi * x) * 
                                 np.sin(53 * np.pi * x) * np.cos(47 * np.pi * x) * 
                                 np.sin(41 * np.pi * x) * np.cos(35 * np.pi * x) * 
                                 np.sin(29 * np.pi * x) * np.cos(23 * np.pi * x) * 
                                 np.sin(17 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Introduce additional fractal-like self-similarity with recursive scaling and enhanced memory effects
        fractal_term = np.sum(np.sin(129 * np.pi * x) * np.cos(121 * np.pi * x) * 
                             np.sin(113 * np.pi * x) * np.cos(105 * np.pi * x) * 
                             np.sin(97 * np.pi * x) * np.cos(89 * np.pi * x) * 
                             np.sin(81 * np.pi * x) * np.cos(73 * np.pi * x) * 
                             np.sin(65 * np.pi * x) * np.cos(57 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.55 * chaotic_term + 0.16 * poly_term + 0.26 * coupling_term + 0.21 * corr_term + 0.21 * exp_term + 0.31 * multi_scale_term + 0.26 * fractal_term + 4.1
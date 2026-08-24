import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and added sinusoidal modulation
        chaotic_term = np.sum(np.sin(34 * np.pi * x) * np.cos(32 * np.pi * x) * 
                             np.sin(30 * np.pi * x) * np.cos(28 * np.pi * x) * 
                             np.sin(26 * np.pi * x) * np.cos(24 * np.pi * x) * 
                             np.sin(22 * np.pi * x) * np.cos(20 * np.pi * x) * 
                             np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x))
        
        # Modified polynomial coupling with altered exponents and added memory-dependent terms
        poly_term = np.sum(1.7 * x**19 - 14 * x**17 + 22 * x**15 - 20 * x**13 + 18 * x**11 - 16 * x**9 + 14 * x**7 - 12 * x**5 + 10 * x**3 - 7 * x**2 + 5 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**13 * np.sin(22 * np.pi * x[:-1]) * np.cos(20 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**11 * np.cos(20 * np.pi * x[:-1]) * np.sin(18 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**9 * np.sin(16 * np.pi * x[:-2]) * np.cos(14 * np.pi * x[2:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(34 * np.pi * x) * np.cos(31 * np.pi * x) * 
                          np.sin(28 * np.pi * x) * np.cos(25 * np.pi * x) * 
                          np.sin(22 * np.pi * x) * np.cos(19 * np.pi * x) * 
                          np.sin(16 * np.pi * x) * np.cos(13 * np.pi * x) * 
                          np.sin(10 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.6 * x**2) * np.sin(22 * np.pi * x) * np.cos(20 * np.pi * x) * 
                         np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * np.sin(14 * np.pi * x) * 
                         np.cos(12 * np.pi * x) * np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Introduce new multi-scale chaotic modulation and adjust weights for better fitness
        multi_scale_term = np.sum(np.sin(68 * np.pi * x) * np.cos(62 * np.pi * x) * 
                                 np.sin(56 * np.pi * x) * np.cos(50 * np.pi * x) * 
                                 np.sin(44 * np.pi * x) * np.cos(38 * np.pi * x) * 
                                 np.sin(32 * np.pi * x) * np.cos(26 * np.pi * x) * 
                                 np.sin(20 * np.pi * x) * np.cos(14 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.55 * chaotic_term + 0.17 * poly_term + 0.27 * coupling_term + 0.22 * corr_term + 0.22 * exp_term + 0.32 * multi_scale_term + 4.2
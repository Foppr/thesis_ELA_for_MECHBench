import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and additional sine/cosine components
        chaotic_term = np.sum(np.sin(32 * np.pi * x) * np.cos(30 * np.pi * x) * 
                             np.sin(28 * np.pi * x) * np.cos(26 * np.pi * x) * 
                             np.sin(24 * np.pi * x) * np.cos(22 * np.pi * x) * 
                             np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x))
        
        # Stronger polynomial coupling with altered degrees and interaction coefficients
        poly_term = np.sum(1.5 * x**17 - 13 * x**15 + 20 * x**13 - 18 * x**11 + 16 * x**9 - 14 * x**7 + 12 * x**5 - 9 * x**3 + 6 * x**2 - 3 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts and memory-dependent weights
        coupling_term = np.sum((x[:-1] - x[1:])**11 * np.sin(20 * np.pi * x[:-1]) * np.cos(18 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**9 * np.cos(18 * np.pi * x[:-1]) * np.sin(16 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**7 * np.sin(14 * np.pi * x[:-2]) * np.cos(12 * np.pi * x[2:]) +
                              0.5 * (x[:-1] * x[1:])**3 * np.sin(10 * np.pi * x[:-1]) * np.cos(8 * np.pi * x[1:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and phase interactions
        corr_term = np.sum(np.sin(32 * np.pi * x) * np.cos(29 * np.pi * x) * 
                          np.sin(26 * np.pi * x) * np.cos(23 * np.pi * x) * 
                          np.sin(20 * np.pi * x) * np.cos(17 * np.pi * x) * 
                          np.sin(14 * np.pi * x) * np.cos(11 * np.pi * x) * 
                          np.sin(8 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                         np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * np.sin(12 * np.pi * x) * 
                         np.cos(10 * np.pi * x) * np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Novel multi-scale chaotic modulation term for enhanced ruggedness
        mod_term = np.sum(np.sin(40 * np.pi * x) * np.cos(35 * np.pi * x) * 
                         np.sin(30 * np.pi * x) * np.cos(25 * np.pi * x) * 
                         np.sin(20 * np.pi * x) * np.cos(15 * np.pi * x) * 
                         np.sin(10 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Introduce improved weighting scheme and add a global offset
        return 0.55 * chaotic_term + 0.11 * poly_term + 0.20 * coupling_term + 0.17 * corr_term + 0.27 * exp_term + 0.30 * mod_term + 4.0
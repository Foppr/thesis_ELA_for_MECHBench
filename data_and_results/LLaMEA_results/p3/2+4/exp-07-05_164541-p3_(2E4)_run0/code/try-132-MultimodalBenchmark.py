import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and additional sine/cosine components
        chaotic_term = np.sum(np.sin(35 * np.pi * x) * np.cos(33 * np.pi * x) * 
                             np.sin(31 * np.pi * x) * np.cos(29 * np.pi * x) * 
                             np.sin(27 * np.pi * x) * np.cos(25 * np.pi * x) * 
                             np.sin(23 * np.pi * x) * np.cos(21 * np.pi * x) * 
                             np.sin(19 * np.pi * x) * np.cos(17 * np.pi * x))
        
        # Stronger polynomial coupling with altered degrees and interaction coefficients
        poly_term = np.sum(1.8 * x**19 - 15 * x**17 + 22 * x**15 - 20 * x**13 + 18 * x**11 - 16 * x**9 + 14 * x**7 - 11 * x**5 + 8 * x**3 - 5 * x**2 + 3 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts and memory-dependent weights
        coupling_term = np.sum((x[:-1] - x[1:])**13 * np.sin(22 * np.pi * x[:-1]) * np.cos(20 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**11 * np.cos(20 * np.pi * x[:-1]) * np.sin(18 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**9 * np.sin(16 * np.pi * x[:-2]) * np.cos(14 * np.pi * x[2:]) +
                              0.6 * (x[:-1] * x[1:])**4 * np.sin(12 * np.pi * x[:-1]) * np.cos(10 * np.pi * x[1:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and phase interactions
        corr_term = np.sum(np.sin(35 * np.pi * x) * np.cos(32 * np.pi * x) * 
                          np.sin(29 * np.pi * x) * np.cos(26 * np.pi * x) * 
                          np.sin(23 * np.pi * x) * np.cos(20 * np.pi * x) * 
                          np.sin(17 * np.pi * x) * np.cos(14 * np.pi * x) * 
                          np.sin(11 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.6 * x**2) * np.sin(22 * np.pi * x) * np.cos(20 * np.pi * x) * 
                         np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * np.sin(14 * np.pi * x) * 
                         np.cos(12 * np.pi * x) * np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Novel multi-scale chaotic modulation term for enhanced ruggedness
        mod_term = np.sum(np.sin(45 * np.pi * x) * np.cos(40 * np.pi * x) * 
                         np.sin(35 * np.pi * x) * np.cos(30 * np.pi * x) * 
                         np.sin(25 * np.pi * x) * np.cos(20 * np.pi * x) * 
                         np.sin(15 * np.pi * x) * np.cos(10 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.60 * chaotic_term + 0.12 * poly_term + 0.22 * coupling_term + 0.18 * corr_term + 0.28 * exp_term + 0.32 * mod_term + 4.2
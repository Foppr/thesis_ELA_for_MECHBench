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
        poly_term = np.sum(1.6 * x**18 - 12 * x**14 + 19 * x**12 - 17 * x**10 + 15 * x**8 - 13 * x**6 + 11 * x**4 - 8 * x**2 + 5 * x)
        
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
        
        # Combine all terms with optimized weights and add a global offset
        return 0.55 * chaotic_term + 0.12 * poly_term + 0.21 * coupling_term + 0.19 * corr_term + 0.23 * exp_term + 3.9
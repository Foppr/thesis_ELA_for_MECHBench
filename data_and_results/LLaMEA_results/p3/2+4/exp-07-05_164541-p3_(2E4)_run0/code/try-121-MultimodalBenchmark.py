import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal chaotic oscillations with varying frequencies and adaptive amplitudes
        fractal_term = np.sum(np.sin(64 * np.pi * x) * np.cos(58 * np.pi * x) * 
                             np.sin(52 * np.pi * x) * np.cos(46 * np.pi * x) * 
                             np.sin(40 * np.pi * x) * np.cos(34 * np.pi * x) * 
                             np.sin(28 * np.pi * x) * np.cos(22 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(10 * np.pi * x))
        
        # Adaptive polynomial coupling with dynamic exponents and memory-dependent coefficients
        poly_term = np.sum(2.0 * x**23 - 17 * x**21 + 25 * x**19 - 22 * x**17 + 19 * x**15 - 16 * x**13 + 13 * x**11 - 10 * x**9 + 7 * x**7 - 4 * x**5 + 2 * x**3)
        
        # Dynamic cross-dimensional coupling with time-varying phase shifts and scale-adaptive weights
        coupling_term = np.sum((x[:-1] - x[1:])**15 * np.sin(25 * np.pi * x[:-1]) * np.cos(23 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**13 * np.cos(21 * np.pi * x[:-1]) * np.sin(19 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**11 * np.sin(17 * np.pi * x[:-2]) * np.cos(15 * np.pi * x[2:]) +
                              (x[:-3] + x[3:])**9 * np.cos(13 * np.pi * x[:-3]) * np.sin(11 * np.pi * x[3:]))
        
        # Multi-scale chaotic correlation with complex amplitude modulation and phase interference
        corr_term = np.sum(np.sin(64 * np.pi * x) * np.cos(55 * np.pi * x) * 
                          np.sin(46 * np.pi * x) * np.cos(37 * np.pi * x) * 
                          np.sin(28 * np.pi * x) * np.cos(19 * np.pi * x) * 
                          np.sin(10 * np.pi * x) * np.cos(1 * np.pi * x) * 
                          np.sin(58 * np.pi * x) * np.cos(49 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                         np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * np.sin(17 * np.pi * x) * 
                         np.cos(15 * np.pi * x) * np.sin(13 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Memory-dependent chaotic modulation with dynamic scaling factors
        memory_term = np.sum(np.sin(32 * np.pi * x) * np.cos(30 * np.pi * x) * 
                           np.sin(28 * np.pi * x) * np.cos(26 * np.pi * x) * 
                           np.sin(24 * np.pi * x) * np.cos(22 * np.pi * x) * 
                           np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                           np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.7 * fractal_term + 0.15 * poly_term + 0.25 * coupling_term + 0.2 * corr_term + 0.2 * exp_term + 0.1 * memory_term + 5.0
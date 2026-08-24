import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal chaotic oscillations with varying frequencies and amplitude modulations
        fractal_term = np.sum(np.sin(64 * np.pi * x) * np.cos(56 * np.pi * x) * 
                             np.sin(48 * np.pi * x) * np.cos(40 * np.pi * x) * 
                             np.sin(32 * np.pi * x) * np.cos(24 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Adaptive polynomial coupling with dynamic exponents and memory-dependent interactions
        poly_term = np.sum(2.0 * x**19 - 15 * x**17 + 22 * x**15 - 20 * x**13 + 18 * x**11 - 16 * x**9 + 14 * x**7 - 12 * x**5 + 10 * x**3 - 7 * x**2 + 4 * x)
        
        # Dynamic cross-dimensional coupling with time-varying phase shifts and variable interaction strengths
        coupling_term = np.sum((x[:-1] - x[1:])**13 * np.sin(24 * np.pi * x[:-1]) * np.cos(20 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**11 * np.cos(20 * np.pi * x[:-1]) * np.sin(16 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**9 * np.sin(16 * np.pi * x[:-2]) * np.cos(12 * np.pi * x[2:]) +
                              (x[:-3] + x[3:])**7 * np.cos(12 * np.pi * x[:-3]) * np.sin(8 * np.pi * x[3:]))
        
        # High-dimensional correlation with multi-scale chaotic interference and varying coupling strengths
        corr_term = np.sum(np.sin(60 * np.pi * x) * np.cos(54 * np.pi * x) * 
                          np.sin(48 * np.pi * x) * np.cos(42 * np.pi * x) * 
                          np.sin(36 * np.pi * x) * np.cos(30 * np.pi * x) * 
                          np.sin(24 * np.pi * x) * np.cos(18 * np.pi * x) * 
                          np.sin(12 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Multi-scale exponential decay with complex oscillatory modulation and amplitude variations
        exp_term = np.sum(np.exp(-0.7 * x**2) * np.sin(24 * np.pi * x) * np.cos(20 * np.pi * x) * 
                         np.sin(16 * np.pi * x) * np.cos(12 * np.pi * x) * np.sin(8 * np.pi * x) * 
                         np.cos(4 * np.pi * x) * np.sin(2 * np.pi * x) * np.cos(1 * np.pi * x))
        
        # Enhanced multi-scale chaotic modulation with adaptive coupling and complex phase interactions
        multi_scale_term = np.sum(np.sin(128 * np.pi * x) * np.cos(116 * np.pi * x) * 
                                 np.sin(104 * np.pi * x) * np.cos(92 * np.pi * x) * 
                                 np.sin(80 * np.pi * x) * np.cos(68 * np.pi * x) * 
                                 np.sin(56 * np.pi * x) * np.cos(44 * np.pi * x) * 
                                 np.sin(32 * np.pi * x) * np.cos(20 * np.pi * x))
        
        # Add dynamic interaction weights and global offset for enhanced landscape complexity
        return 0.6 * fractal_term + 0.2 * poly_term + 0.3 * coupling_term + 0.25 * corr_term + 0.25 * exp_term + 0.35 * multi_scale_term + 5.0
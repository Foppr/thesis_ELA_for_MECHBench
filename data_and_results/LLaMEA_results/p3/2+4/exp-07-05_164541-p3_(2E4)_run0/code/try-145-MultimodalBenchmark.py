import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Ultra-high frequency chaotic oscillations with nested fractal patterns
        chaotic_term = np.sum(np.sin(256 * np.pi * x) * np.cos(240 * np.pi * x) * 
                             np.sin(224 * np.pi * x) * np.cos(208 * np.pi * x) * 
                             np.sin(192 * np.pi * x) * np.cos(176 * np.pi * x) * 
                             np.sin(160 * np.pi * x) * np.cos(144 * np.pi * x) * 
                             np.sin(128 * np.pi * x) * np.cos(112 * np.pi * x) * 
                             np.sin(96 * np.pi * x) * np.cos(80 * np.pi * x))
        
        # Modified polynomial with higher-order terms and dynamic coupling
        poly_term = np.sum(2.0 * x**23 - 18 * x**21 + 25 * x**19 - 22 * x**17 + 19 * x**15 - 16 * x**13 + 13 * x**11 - 10 * x**9 + 7 * x**7 - 4 * x**5 + 2 * x**3 - 1 * x)
        
        # Enhanced cross-dimensional nonlinear coupling with recursive phase interactions
        coupling_term = np.sum((x[:-1] - x[1:])**15 * np.sin(25 * np.pi * x[:-1]) * np.cos(23 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**13 * np.cos(23 * np.pi * x[:-1]) * np.sin(21 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**11 * np.sin(19 * np.pi * x[:-2]) * np.cos(17 * np.pi * x[2:]) +
                              (x[:-3] + x[3:])**9 * np.cos(15 * np.pi * x[:-3]) * np.sin(13 * np.pi * x[3:]))
        
        # Complex high-frequency correlation terms with multi-scale amplitude modulation
        corr_term = np.sum(np.sin(256 * np.pi * x) * np.cos(233 * np.pi * x) * 
                          np.sin(210 * np.pi * x) * np.cos(187 * np.pi * x) * 
                          np.sin(164 * np.pi * x) * np.cos(141 * np.pi * x) * 
                          np.sin(118 * np.pi * x) * np.cos(95 * np.pi * x) * 
                          np.sin(72 * np.pi * x) * np.cos(49 * np.pi * x) * 
                          np.sin(26 * np.pi * x) * np.cos(13 * np.pi * x))
        
        # Multi-scale exponential decay with ultra-high frequency oscillations
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                         np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * np.sin(17 * np.pi * x) * 
                         np.cos(15 * np.pi * x) * np.sin(13 * np.pi * x) * np.cos(11 * np.pi * x) * 
                         np.sin(9 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Ultra-high frequency multi-scale chaotic modulation with recursive scaling
        multi_scale_term = np.sum(np.sin(512 * np.pi * x) * np.cos(480 * np.pi * x) * 
                                 np.sin(448 * np.pi * x) * np.cos(416 * np.pi * x) * 
                                 np.sin(384 * np.pi * x) * np.cos(352 * np.pi * x) * 
                                 np.sin(320 * np.pi * x) * np.cos(288 * np.pi * x) * 
                                 np.sin(256 * np.pi * x) * np.cos(224 * np.pi * x) * 
                                 np.sin(192 * np.pi * x) * np.cos(160 * np.pi * x))
        
        # Nested fractal-like self-similarity with recursive scaling and ultra-high frequency interactions
        fractal_term = np.sum(np.sin(1024 * np.pi * x) * np.cos(960 * np.pi * x) * 
                             np.sin(896 * np.pi * x) * np.cos(832 * np.pi * x) * 
                             np.sin(768 * np.pi * x) * np.cos(704 * np.pi * x) * 
                             np.sin(640 * np.pi * x) * np.cos(576 * np.pi * x) * 
                             np.sin(512 * np.pi * x) * np.cos(448 * np.pi * x) * 
                             np.sin(384 * np.pi * x) * np.cos(320 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.6 * chaotic_term + 0.2 * poly_term + 0.3 * coupling_term + 0.25 * corr_term + 0.25 * exp_term + 0.35 * multi_scale_term + 0.3 * fractal_term + 5.0
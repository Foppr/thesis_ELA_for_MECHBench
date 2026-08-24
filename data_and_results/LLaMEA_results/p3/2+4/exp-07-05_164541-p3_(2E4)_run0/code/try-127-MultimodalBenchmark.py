import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with increased frequency modulation and amplitude scaling
        chaotic_term = np.sum(np.sin(64 * np.pi * x) * np.cos(60 * np.pi * x) * 
                             np.sin(56 * np.pi * x) * np.cos(52 * np.pi * x) * 
                             np.sin(48 * np.pi * x) * np.cos(44 * np.pi * x) * 
                             np.sin(40 * np.pi * x) * np.cos(36 * np.pi * x) * 
                             np.sin(32 * np.pi * x) * np.cos(28 * np.pi * x))
        
        # Stronger polynomial coupling with higher degrees and additional interaction terms
        poly_term = np.sum(2.0 * x**21 - 18 * x**19 + 25 * x**17 - 22 * x**15 + 20 * x**13 - 18 * x**11 + 16 * x**9 - 14 * x**7 + 12 * x**5 - 10 * x**3 + 8 * x**2 - 5 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, memory-dependent weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**15 * np.sin(25 * np.pi * x[:-1]) * np.cos(23 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**13 * np.cos(23 * np.pi * x[:-1]) * np.sin(21 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**11 * np.sin(19 * np.pi * x[:-2]) * np.cos(17 * np.pi * x[2:]) +
                              0.7 * (x[:-1] * x[1:])**5 * np.sin(15 * np.pi * x[:-1]) * np.cos(13 * np.pi * x[1:]) +
                              (x[:-3] + x[3:])**9 * np.cos(11 * np.pi * x[:-3]) * np.sin(9 * np.pi * x[3:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes, phase interactions and multi-scale modulations
        corr_term = np.sum(np.sin(64 * np.pi * x) * np.cos(59 * np.pi * x) * 
                          np.sin(54 * np.pi * x) * np.cos(49 * np.pi * x) * 
                          np.sin(44 * np.pi * x) * np.cos(39 * np.pi * x) * 
                          np.sin(34 * np.pi * x) * np.cos(29 * np.pi * x) * 
                          np.sin(24 * np.pi * x) * np.cos(19 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation, complex interaction and additional chaotic components
        exp_term = np.sum(np.exp(-0.7 * x**2) * np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                         np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * np.sin(17 * np.pi * x) * 
                         np.cos(15 * np.pi * x) * np.sin(13 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Novel multi-scale chaotic modulation term with increased complexity and enhanced ruggedness
        mod_term = np.sum(np.sin(80 * np.pi * x) * np.cos(75 * np.pi * x) * 
                         np.sin(70 * np.pi * x) * np.cos(65 * np.pi * x) * 
                         np.sin(60 * np.pi * x) * np.cos(55 * np.pi * x) * 
                         np.sin(50 * np.pi * x) * np.cos(45 * np.pi * x) * 
                         np.sin(40 * np.pi * x) * np.cos(35 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.65 * chaotic_term + 0.15 * poly_term + 0.25 * coupling_term + 0.20 * corr_term + 0.30 * exp_term + 0.35 * mod_term + 6.0
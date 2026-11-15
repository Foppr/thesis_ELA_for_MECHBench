import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with multiple sine and cosine components and higher frequency terms
        chaotic_term = np.sum(np.sin(30 * np.pi * x) * np.cos(28 * np.pi * x) * 
                             np.sin(26 * np.pi * x) * np.cos(24 * np.pi * x) * 
                             np.sin(22 * np.pi * x) * np.cos(20 * np.pi * x) * 
                             np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * 
                             np.sin(14 * np.pi * x) * np.cos(12 * np.pi * x))
        
        # Stronger polynomial coupling with higher-degree terms, mixed nonlinearities and additional interaction terms
        poly_term = np.sum(1.2 * x**15 - 11 * x**13 + 18 * x**11 - 15 * x**9 + 13 * x**7 - 10 * x**5 + 7 * x**3 - 4 * x**2 + 2 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**9 * np.sin(18 * np.pi * x[:-1]) * np.cos(16 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**7 * np.cos(16 * np.pi * x[:-1]) * np.sin(14 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**5 * np.sin(12 * np.pi * x[:-2]) * np.cos(10 * np.pi * x[2:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(30 * np.pi * x) * np.cos(27 * np.pi * x) * 
                          np.sin(24 * np.pi * x) * np.cos(21 * np.pi * x) * 
                          np.sin(18 * np.pi * x) * np.cos(15 * np.pi * x) * 
                          np.sin(12 * np.pi * x) * np.cos(9 * np.pi * x) * 
                          np.sin(6 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * 
                         np.sin(14 * np.pi * x) * np.cos(12 * np.pi * x) * np.sin(10 * np.pi * x) * 
                         np.cos(8 * np.pi * x) * np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.5 * chaotic_term + 0.09 * poly_term + 0.18 * coupling_term + 0.15 * corr_term + 0.25 * exp_term + 3.5
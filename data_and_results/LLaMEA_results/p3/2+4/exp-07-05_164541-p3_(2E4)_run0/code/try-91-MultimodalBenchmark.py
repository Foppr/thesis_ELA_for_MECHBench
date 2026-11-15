import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with multiple sine and cosine components and higher frequency terms
        chaotic_term = np.sum(np.sin(20 * np.pi * x) * np.cos(18 * np.pi * x) * 
                             np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * 
                             np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                             np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * 
                             np.sin(4 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Stronger polynomial coupling with higher-degree terms, mixed nonlinearities and additional interaction terms
        poly_term = np.sum(0.8 * x**13 - 9 * x**11 + 15 * x**9 - 12 * x**7 + 10 * x**5 - 8 * x**3 + 5 * x**2 - 2.5 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights and higher-order interactions
        coupling_term = np.sum((x[:-1] - x[1:])**7 * np.sin(15 * np.pi * x[:-1]) * np.cos(12 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**5 * np.cos(13 * np.pi * x[:-1]) * np.sin(11 * np.pi * x[1:]) +
                              (x[:-2] - x[2:])**3 * np.sin(9 * np.pi * x[:-2]) * np.cos(7 * np.pi * x[2:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and complex phase interactions
        corr_term = np.sum(np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                          np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * 
                          np.sin(17 * np.pi * x) * np.cos(15 * np.pi * x) * 
                          np.sin(13 * np.pi * x) * np.cos(11 * np.pi * x) * 
                          np.sin(9 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation and complex interaction
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(15 * np.pi * x) * np.cos(13 * np.pi * x) * 
                         np.sin(11 * np.pi * x) * np.cos(9 * np.pi * x) * np.sin(7 * np.pi * x) * 
                         np.cos(5 * np.pi * x) * np.sin(3 * np.pi * x) * np.cos(1 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.4 * chaotic_term + 0.07 * poly_term + 0.15 * coupling_term + 0.12 * corr_term + 0.2 * exp_term + 3.2
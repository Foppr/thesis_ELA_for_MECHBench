import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with multiple sine and cosine components
        chaotic_term = np.sum(np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) * 
                             np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x) * 
                             np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Stronger polynomial coupling with higher-degree terms and mixed nonlinearities
        poly_term = np.sum(0.7 * x**12 - 8 * x**10 + 14 * x**8 - 12 * x**6 + 8 * x**4 - 4 * x**2 + 2 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts and interaction weights
        coupling_term = np.sum((x[:-1] - x[1:])**6 * np.sin(11 * np.pi * x[:-1]) * np.cos(8 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**4 * np.cos(10 * np.pi * x[:-1]) * np.sin(6 * np.pi * x[1:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes
        corr_term = np.sum(np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * 
                          np.sin(14 * np.pi * x) * np.cos(12 * np.pi * x) * 
                          np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations and amplitude modulation
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                         np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * np.sin(4 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.35 * chaotic_term + 0.06 * poly_term + 0.12 * coupling_term + 0.09 * corr_term + 0.16 * exp_term + 2.2
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and amplitudes
        chaotic_term = np.sum(np.sin(13 * np.pi * x) * np.cos(11 * np.pi * x) * 
                             np.sin(9 * np.pi * x) * np.cos(7 * np.pi * x) * 
                             np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Modified polynomial coupling with altered exponents and coefficients
        poly_term = np.sum(0.7 * x**12 - 6.5 * x**10 + 11 * x**8 - 9 * x**6 + 5 * x**4 - 2.5 * x**2 + 1.2 * x)
        
        # Adjusted cross-dimensional nonlinear coupling with new interaction weights
        coupling_term = np.sum((x[:-1] - x[1:])**6 * np.sin(11 * np.pi * x[:-1]) * np.cos(8 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**4 * np.cos(10 * np.pi * x[:-1]) * np.sin(6 * np.pi * x[1:]))
        
        # Modified high-frequency chaotic correlation terms
        corr_term = np.sum(np.sin(16 * np.pi * x) * np.cos(14 * np.pi * x) * 
                          np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                          np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Modified exponential decay with different oscillation scales
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(11 * np.pi * x) * np.cos(9 * np.pi * x) * 
                         np.sin(7 * np.pi * x) * np.cos(5 * np.pi * x) * np.sin(3 * np.pi * x))
        
        # Combine all terms with updated weights and add a global offset
        return 0.35 * chaotic_term + 0.06 * poly_term + 0.12 * coupling_term + 0.09 * corr_term + 0.16 * exp_term + 2.2
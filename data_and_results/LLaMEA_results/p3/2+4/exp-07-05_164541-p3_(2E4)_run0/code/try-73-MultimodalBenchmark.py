import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with multiple sine and cosine components
        chaotic_term = np.sum(np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                             np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * 
                             np.sin(4 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Stronger polynomial coupling with higher degree terms and mixed nonlinearities
        poly_term = np.sum(0.6 * x**11 - 7 * x**9 + 12 * x**7 - 10 * x**5 + 6 * x**3 - 3 * x**2 + 1.5 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**6 * np.sin(10 * np.pi * x[:-1]) * np.cos(7 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**4 * np.cos(9 * np.pi * x[:-1]) * np.sin(5 * np.pi * x[1:]))
        
        # Additional high-frequency chaotic correlation terms between all dimensions
        corr_term = np.sum(np.sin(15 * np.pi * x) * np.cos(13 * np.pi * x) * 
                          np.sin(11 * np.pi * x) * np.cos(9 * np.pi * x) * 
                          np.sin(7 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Mixed exponential and trigonometric terms for added complexity
        exp_trig_term = np.sum(np.exp(-0.5 * x**2) * np.sin(14 * np.pi * x) * np.cos(12 * np.pi * x) + 
                              np.exp(-0.2 * x**3) * np.cos(11 * np.pi * x) * np.sin(9 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * chaotic_term + 0.05 * poly_term + 0.1 * coupling_term + 0.07 * corr_term + 0.15 * exp_trig_term + 2.1
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with multi-frequency sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.25 * x**2) * np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(2.5 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation and phase shifts
        trig_term = np.sum(np.sin(7 * np.pi * x) * np.cos(9 * np.pi * x) + 
                          np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x) + 
                          np.sin(4 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities and enhanced coupling
        poly_term = np.sum(0.35 * x**9 - 4.5 * x**7 + 7.5 * x**5 - 6.5 * x**3 + 3.5 * x**2 - 1.8 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**4 * np.sin(7 * np.pi * x[:-1]) * np.cos(4 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity
        corr_term = np.sum(np.sin(1.5 * np.pi * x) * np.cos(2.5 * np.pi * x) * np.sin(3.5 * np.pi * x) * np.cos(5.5 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.28 * exp_term + 0.22 * trig_term + 0.045 * poly_term + 0.09 * coupling_term + 0.065 * corr_term + 1.75
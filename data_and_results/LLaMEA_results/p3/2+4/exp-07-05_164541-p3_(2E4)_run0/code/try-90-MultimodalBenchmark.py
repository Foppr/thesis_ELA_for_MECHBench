import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with multi-frequency sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(5.5 * np.pi * x) * np.cos(3.5 * np.pi * x) * np.sin(2.8 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation and phase shifts
        trig_term = np.sum(np.sin(7.5 * np.pi * x) * np.cos(9.5 * np.pi * x) + 
                          np.sin(3.5 * np.pi * x) * np.cos(5.5 * np.pi * x) + 
                          np.sin(4.5 * np.pi * x) * np.cos(7.5 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities and enhanced coupling
        poly_term = np.sum(0.4 * x**9 - 4.8 * x**7 + 7.8 * x**5 - 6.8 * x**3 + 3.8 * x**2 - 2.0 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**4 * np.sin(7.5 * np.pi * x[:-1]) * np.cos(4.5 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity
        corr_term = np.sum(np.sin(1.8 * np.pi * x) * np.cos(2.8 * np.pi * x) * np.sin(3.8 * np.pi * x) * np.cos(5.8 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * exp_term + 0.25 * trig_term + 0.05 * poly_term + 0.1 * coupling_term + 0.07 * corr_term + 1.8
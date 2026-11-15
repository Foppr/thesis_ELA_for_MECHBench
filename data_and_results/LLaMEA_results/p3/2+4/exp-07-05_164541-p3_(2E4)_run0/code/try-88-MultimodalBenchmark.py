import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with multi-frequency sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x) * np.sin(3 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation and phase shifts
        trig_term = np.sum(np.sin(8 * np.pi * x) * np.cos(10 * np.pi * x) + 
                          np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities and enhanced coupling
        poly_term = np.sum(0.4 * x**10 - 5.0 * x**8 + 8.0 * x**6 - 7.0 * x**4 + 4.0 * x**2 - 2.0 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**5 * np.sin(8 * np.pi * x[:-1]) * np.cos(5 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity
        corr_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * exp_term + 0.25 * trig_term + 0.05 * poly_term + 0.1 * coupling_term + 0.07 * corr_term + 2.0
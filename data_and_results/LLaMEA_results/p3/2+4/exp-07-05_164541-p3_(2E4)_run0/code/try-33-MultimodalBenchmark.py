import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay with sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(2 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation
        trig_term = np.sum(np.sin(7 * np.pi * x) * np.cos(9 * np.pi * x) + 
                          np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x) + 
                          np.sin(4 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities
        poly_term = np.sum(0.3 * x**8 - 4 * x**6 + 7 * x**4 - 6 * x**2 + 3 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts
        coupling_term = np.sum((x[:-1] - x[1:])**3 * np.sin(7 * np.pi * x[:-1]) * np.cos(4 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions
        corr_term = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.2 * exp_term + 0.15 * trig_term + 0.03 * poly_term + 0.07 * coupling_term + 0.05 * corr_term + 2.0
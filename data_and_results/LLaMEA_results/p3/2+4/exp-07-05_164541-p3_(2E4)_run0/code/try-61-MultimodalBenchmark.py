import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(8 * np.pi * x) * np.cos(5 * np.pi * x) * np.sin(4 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation and higher harmonics
        trig_term = np.sum(np.sin(10 * np.pi * x) * np.cos(12 * np.pi * x) + 
                          np.sin(6 * np.pi * x) * np.cos(8 * np.pi * x) + 
                          np.sin(7 * np.pi * x) * np.cos(9 * np.pi * x) + 
                          np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities and additional terms
        poly_term = np.sum(0.6 * x**10 - 6 * x**8 + 10 * x**6 - 9 * x**4 + 5 * x**2 + 0.5 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts and enhanced interaction
        coupling_term = np.sum((x[:-1] - x[1:])**5 * np.sin(10 * np.pi * x[:-1]) * np.cos(6 * np.pi * x[1:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity
        corr_term = np.sum(np.sin(3 * np.pi * x) * np.cos(4 * np.pi * x) * np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x) * np.sin(6 * np.pi * x))
        
        # Additional chaotic interaction terms with fractional powers and enhanced chaos
        frac_term = np.sum(np.sin(np.pi * x**1.7) * np.cos(2 * np.pi * x**1.4) * np.sin(3 * np.pi * x**1.8) * np.cos(4 * np.pi * x**1.6))
        
        # Additional high-order polynomial coupling between dimensions
        high_order_term = np.sum((x**2 + x**3 + x**4)**2)
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * exp_term + 0.25 * trig_term + 0.05 * poly_term + 0.15 * coupling_term + 0.07 * corr_term + 0.06 * frac_term + 0.08 * high_order_term + 3.0
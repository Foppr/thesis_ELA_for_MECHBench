import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic exponential decay with multi-frequency sine modulation and varying decay rates
        exp_term = np.sum(np.exp(-0.4 * x**2) * np.sin(7 * np.pi * x) * np.cos(5 * np.pi * x) * np.sin(4 * np.pi * x))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation, phase shifts, and additional harmonics
        trig_term = np.sum(np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x) + 
                          np.sin(6 * np.pi * x) * np.cos(9 * np.pi * x) + 
                          np.sin(3 * np.pi * x) * np.cos(8 * np.pi * x))
        
        # High-degree polynomial interaction terms with mixed nonlinearities, enhanced coupling, and additional terms
        poly_term = np.sum(0.5 * x**10 - 6 * x**8 + 9 * x**6 - 8 * x**4 + 5 * x**3 - 3 * x**2 + 2 * x)
        
        # Cross-dimensional nonlinear coupling with chaotic phase shifts, enhanced interaction, and additional dimension pairs
        coupling_term = np.sum((x[:-1] - x[1:])**5 * np.sin(9 * np.pi * x[:-1]) * np.cos(6 * np.pi * x[1:]) + 
                              (x[:-2] - x[2:])**3 * np.cos(7 * np.pi * x[:-2]) * np.sin(5 * np.pi * x[2:]))
        
        # Additional chaotic correlation terms between all dimensions with increased complexity and higher-order interactions
        corr_term = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(4 * np.pi * x) * np.cos(7 * np.pi * x) * np.sin(3 * np.pi * x))
        
        # Additional high-frequency chaotic term to increase landscape complexity
        high_freq_term = np.sum(np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) * np.sin(10 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * exp_term + 0.25 * trig_term + 0.05 * poly_term + 0.1 * coupling_term + 0.07 * corr_term + 0.08 * high_freq_term + 2.1
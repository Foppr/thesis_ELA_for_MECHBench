import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with varying coefficients and higher-order interactions
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(4 * np.pi * x) * np.cos(3 * np.pi * x) + 
                         np.exp(-0.2 * x**4) * np.sin(2 * np.pi * x**2))
        
        # Enhanced trigonometric oscillations with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x) + 
                          np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x) + 
                          np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Enhanced polynomial interaction terms with higher degree and mixed coefficients
        poly_term = np.sum(0.3 * x**8 - 2.5 * x**6 + 4.2 * x**4 - 3.8 * x**2 + 1.5 * x)
        
        # Additional coupling terms between dimensions with non-linear interactions
        coupling_term = np.sum((x[:-1] - x[1:])**4 * np.sin(7 * np.pi * x[:-1]) * np.cos(3 * np.pi * x[1:]))
        
        # Cross-dimensional polynomial interactions
        cross_term = np.sum(x[:-1]**3 * x[1:]**2 * np.sin(4 * np.pi * x[:-1]) * np.cos(2 * np.pi * x[1:]))
        
        # Combine all terms with optimized weights
        return 0.2 * exp_term + 0.15 * trig_term + 0.03 * poly_term + 0.04 * coupling_term + 0.02 * cross_term + 2.0
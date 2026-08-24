import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay terms with varying coefficients
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Enhanced trigonometric oscillations with multiple frequencies
        trig_term = np.sum(np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x) + 
                          np.sin(2 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Enhanced polynomial interaction terms with higher degree and mixed coefficients
        poly_term = np.sum(0.5 * x**6 - 3 * x**4 + 5 * x**2 - 2 * x)
        
        # Additional coupling terms between dimensions
        coupling_term = np.sum((x[:-1] - x[1:])**2 * np.sin(5 * np.pi * x[:-1]))
        
        # Combine all terms with optimized weights
        return 0.15 * exp_term + 0.1 * trig_term + 0.02 * poly_term + 0.05 * coupling_term + 1.5
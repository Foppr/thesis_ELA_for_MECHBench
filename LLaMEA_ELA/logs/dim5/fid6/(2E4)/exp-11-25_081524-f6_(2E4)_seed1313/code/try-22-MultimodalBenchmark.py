import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying exponents
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with modified frequencies and amplitudes
        sinusoidal = 2.0 * np.sum(np.sin(5.0 * x)) + 0.8 * np.sum(np.sin(3.0 * x)**2) + 0.5 * np.sum(np.cos(4.0 * x))
        
        # Enhanced asymmetric cross-terms with non-linear coupling
        cross_terms = 0.2 * np.sum(x[:-1] * x[1:]**3) + 0.1 * np.sum(x[:-2] * x[2:]**2) + 0.05 * np.sum((x[:-1] + x[1:])**4)
        
        # Additional challenge through trigonometric coupling between variables
        trig_coupling = 0.3 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]))
        
        return polynomial + sinusoidal + cross_terms + trig_coupling
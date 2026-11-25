import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Higher-order polynomial terms with varying exponents
        poly_term = np.sum(x**8 + 0.5 * x**7 + 0.3 * x**6)
        
        # Enhanced sinusoidal oscillations with mixed frequencies and amplitudes
        sin_term = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.sin(0.5 * x) + 
                          0.5 * np.sin(3.0 * x) * np.cos(0.8 * x))
        
        # Novel cross-term interactions with exponential weighting
        cross_term = np.sum(np.exp(0.1 * x[:-1]) * x[1:]**4 + 
                            np.exp(0.05 * x[1:]) * x[:-1]**5)
        
        # Additional radial component with logarithmic scaling
        radial_term = np.log(np.sum(x**2) + 1.0)
        
        # Combined function with refined weights
        return 0.3 * poly_term + 0.4 * sin_term + 0.2 * cross_term + 0.1 * radial_term
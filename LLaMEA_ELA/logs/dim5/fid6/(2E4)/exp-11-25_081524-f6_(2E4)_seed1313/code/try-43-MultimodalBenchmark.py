import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillations to create multiple local minima
        sinusoidal = np.sum(np.sin(7.0 * x)) + 0.5 * np.sum(np.sin(3.0 * x)**2)
        
        # Additional challenge with enhanced asymmetric cross-terms and higher-order interactions
        cross_terms = 0.15 * np.sum(x[:-2] * x[2:]**2) + 0.08 * np.sum((x[:-1] + x[1:])**3) + 0.03 * np.sum(x**5)
        
        # Add a new fractal-like cross-term interaction for increased complexity
        fractal_cross = 0.07 * np.sum(np.sin(x[:-1] * x[1:] + 1.0))
        
        # Introduce a chaotic scaling factor to increase conditioning difficulty
        chaotic_factor = 1.0 + 0.2 * np.sin(13.0 * np.sum(x**2))
        
        return chaotic_factor * (polynomial + sinusoidal + cross_terms + fractal_cross)
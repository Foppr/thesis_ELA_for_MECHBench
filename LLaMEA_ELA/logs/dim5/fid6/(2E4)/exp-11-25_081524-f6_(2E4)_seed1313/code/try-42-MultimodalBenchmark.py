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
        
        # Add a new quadratic cross-term interaction for increased complexity
        quadratic_cross = 0.05 * np.sum(x[:-1] * x[1:]**2)
        
        # Fractal-like interaction term with modified frequency and scaling
        fractal_interaction = 0.07 * np.sum(np.sin(5.0 * x[:-1]) * np.cos(2.0 * x[1:]))
        
        # Asymmetric conditioning with exponential scaling
        asymmetric_conditioning = 0.04 * np.sum(np.exp(0.5 * x[:-1]) * x[1:]**2)
        
        return polynomial + sinusoidal + cross_terms + quadratic_cross + fractal_interaction + asymmetric_conditioning
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with increased complexity
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with varying frequencies for increased complexity
        sinusoidal = np.sum(np.sin(5.0 * x)) + 0.5 * np.sum(np.sin(3.0 * x)**2) + 0.3 * np.sum(np.cos(7.0 * x))
        
        # Enhanced cross-terms with modified interaction patterns
        cross_terms = 0.2 * np.sum(x[:-1]**2 * x[1:]) + 0.1 * np.sum(x[:-2] * x[1:-1] * x[2:]**2)
        
        # Increased nonlinearity with combined trigonometric and polynomial terms
        nonlinear = 0.3 * np.sum(np.sin(7.0 * x)**2) + 0.2 * np.sum(np.cos(4.0 * x)**3) + 0.05 * np.sum(x**8)
        
        # Additional challenge with exponential interaction terms
        exp_interaction = 0.1 * np.sum(np.exp(-x**2) * x**2)
        
        return polynomial + sinusoidal + cross_terms + nonlinear + exp_interaction
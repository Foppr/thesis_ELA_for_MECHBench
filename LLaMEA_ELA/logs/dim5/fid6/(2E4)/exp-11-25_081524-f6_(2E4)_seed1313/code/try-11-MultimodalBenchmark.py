import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher-order interactions
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with exponentially increasing frequencies
        sinusoidal = np.sum(np.sin(2**(np.arange(self.dim)) * x)) + 0.5 * np.sum(np.sin(3**(np.arange(self.dim)) * x)**2)
        
        # Cross-terms with asymmetric weighting
        cross_terms = 0.3 * np.sum(x[:-1] * x[1:]**3) + 0.2 * np.sum(x[:-2] * x[2:]**2)
        
        # Increased nonlinearity with exponential and trigonometric mix
        nonlinear = 0.1 * np.sum(np.exp(0.5 * x) - 1) + 0.4 * np.sum(np.cos(5.0 * x) - 1)
        
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.05 * np.sum(np.sin(np.pi * (x + 0.5) * np.exp(x))**2)
        
        return polynomial + sinusoidal + cross_terms + nonlinear + chaotic
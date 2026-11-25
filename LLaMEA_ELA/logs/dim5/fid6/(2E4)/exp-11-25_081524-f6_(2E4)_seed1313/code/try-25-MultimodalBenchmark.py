import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with exponential scaling
        polynomial = np.sum(x**2) + 0.1 * np.sum(np.exp(0.5 * x**2)) + 0.05 * np.sum(x**6)
        
        # Irregular sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(7.0 * x) * np.exp(-0.1 * x**2)) + 0.3 * np.sum(np.sin(3.0 * x)**3)
        
        # Highly skewed asymmetric cross-terms with exponential interactions
        cross_terms = 0.2 * np.sum(x[:-2] * np.exp(0.3 * x[2:]**2)) + \
                      0.1 * np.sum((x[:-1] * x[1:])**2.5) + \
                      0.05 * np.sum(np.exp(0.4 * x**3))
        
        # Additional irregular modulations to increase conditioning difficulty
        irregular = 0.03 * np.sum(np.sin(5.0 * x + np.cos(x))**2)
        
        return polynomial + sinusoidal + cross_terms + irregular
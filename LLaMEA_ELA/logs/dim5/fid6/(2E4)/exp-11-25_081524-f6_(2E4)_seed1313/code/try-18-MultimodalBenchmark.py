import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher-order interactions
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Modified sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = 2.0 * np.sum(np.sin(5.0 * x)) + 1.5 * np.sum(np.sin(3.0 * x)**2) + 0.8 * np.sum(np.cos(4.0 * x))
        
        # Novel cross-term interaction patterns with asymmetric coupling
        cross_terms = 0.2 * np.sum(x[:-1] * x[1:] * np.sin(2.0 * x[:-1])) + \
                      0.1 * np.sum((x[:-2] + x[2:]) * np.cos(1.5 * x[1:-1])) + \
                      0.05 * np.sum(x**3 * np.sin(0.5 * x))
        
        # Additional challenge with exponential modulation
        modulation = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(7.0 * x))
        
        return polynomial + sinusoidal + cross_terms + modulation
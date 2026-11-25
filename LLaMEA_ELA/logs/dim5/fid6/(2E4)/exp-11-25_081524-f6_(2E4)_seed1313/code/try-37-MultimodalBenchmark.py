import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with higher-order terms for conditioning
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(9.0 * x)) + 0.7 * np.sum(np.sin(5.0 * x)**2) + 0.3 * np.sum(np.sin(2.0 * x)**3)
        
        # Fractal-like cross-terms with exponentially increasing interactions
        cross_terms = 0.2 * np.sum(x[:-2] * x[2:]**3) + 0.1 * np.sum((x[:-1] + x[1:])**4) + 0.05 * np.sum(x**7)
        
        # Adaptive conditioning through dynamic scaling based on dimension
        adaptive_scaling = 0.02 * np.sum(np.abs(x[:-1] - x[1:])**(1 + self.dim/10))
        
        # Additional asymmetric interactions with exponential decay
        asymetric_cross = 0.1 * np.sum(np.exp(-x[:-2]**2) * x[2:]**2) + 0.05 * np.sum(np.tanh(x[:-1]) * x[1:]**3)
        
        return polynomial + sinusoidal + cross_terms + adaptive_scaling + asymetric_cross
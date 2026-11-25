import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with modified exponential decay
        f2 = 0.3 * np.sum(np.sin(9.0 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Additional high-frequency oscillations with altered decay
        f3 = 0.2 * np.sum(np.sin(18.0 * x) * np.exp(-0.15 * x**2))
        
        # Adaptive scaling based on dimensionality with a modified factor
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1)
        f4 = adaptive_scale * np.sum(np.cos(12.0 * x) * np.exp(-0.07 * np.abs(x)))
        
        # Complex cubic and quartic terms with altered coefficients
        f5 = 0.015 * np.sum(x**3 * np.sin(6.0 * x))
        f6 = 0.008 * np.sum(x**4 * np.cos(4.0 * x))
        
        # Add a chaotic perturbation term for increased deception
        f7 = 0.1 * np.sum(np.exp(-0.3 * (x - 1.5)**2) + np.exp(-0.3 * (x + 1.5)**2) - 1.0)
        
        # Introduce a new chaotic modulation term
        f8 = 0.05 * np.sum(np.sin(20.0 * x + np.sin(7.0 * x)) * np.exp(-0.1 * np.abs(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal terms with chaotic coupling
        f2 = 0.5 * np.sum(np.sin(20.0 * x) * np.cos(13.0 * x))
        
        # Exponential interaction terms for ridge structures
        f3 = 0.2 * np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2))
        
        # Chaotic polynomial interactions
        f4 = 0.15 * np.sum((x[:-2]**2 + x[1:-1]**2) * np.sin(7.0 * x[2:]))
        
        # Dynamic coupling with exponential decay
        f5 = 0.1 * np.sum(np.exp(-0.1 * np.abs(x[:-1])) * (x[1:]**3 + x[:-1]**3))
        
        # Irregular ridge terms with varying amplitudes
        f6 = 0.08 * np.sum(np.sin(5.0 * x) * np.cos(9.0 * x) * (1.0 + 0.5 * np.sin(2.0 * x)))
        
        # Higher-order mixed terms with chaotic modulation
        f7 = 0.05 * np.sum((x**4 + x**3 + x**2) * np.sin(11.0 * x))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Nested trigonometric components creating chaotic behavior
        f2 = 0.3 * np.sum(np.sin(np.sin(5.0 * x)) * np.cos(np.cos(3.0 * x)))
        
        # Radial saddle point structure with exponential decay
        f3 = 0.25 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.2 * np.sum(x**2)))
        
        # High-frequency oscillation with adaptive amplitude modulation
        f4 = 0.18 * np.sum(np.sin(13.0 * x) * np.cos(17.0 * x) * (1.0 + 0.5 * np.sin(2.0 * x)))
        
        # Cross-dimensional interaction terms with sinusoidal coupling
        f5 = 0.12 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) if self.dim > 1 else 0)
        
        # Cubic nonlinearity with chaotic modulation
        f6 = 0.07 * np.sum(x**3 * np.sin(7.0 * x) * np.cos(4.0 * x))
        
        # Asymmetric penalty term to increase difficulty
        f7 = 0.09 * np.sum(np.abs(x)**1.5 * np.exp(-0.1 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
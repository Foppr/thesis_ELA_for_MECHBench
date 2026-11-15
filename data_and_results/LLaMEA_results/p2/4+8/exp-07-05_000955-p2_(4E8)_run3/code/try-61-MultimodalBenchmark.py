import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sine-wave interactions with modified frequency modulation
        f2 = 0.4 * np.sum(np.sin(8.0 * x + np.sin(6.0 * x)) * np.cos(10.0 * x + np.sin(5.0 * x)))
        
        # Modified radial gradient with inverse exponential decay for deeper basins
        f3 = 0.25 * np.sum(np.exp(-0.4 * np.sum(x**2)) * np.sin(6.0 * np.sum(x**2)))
        
        # Cross-term interactions with cubic and quartic polynomial modulation
        f4 = 0.15 * np.sum((x**3) * np.sin(9.0 * x) * np.cos(5.0 * x) + (x**4) * np.sin(4.0 * x))
        
        # Multi-scale sinusoidal modulation with adaptive amplitude scaling
        f5 = 0.2 * np.sum(np.sin(13.0 * x) * np.sin(19.0 * x) * np.cos(7.0 * x))
        
        # Adaptive scaling with Gaussian-like decay and higher-order polynomial terms
        f6 = 0.1 * np.sum(np.exp(-0.15 * np.sum(x**2)) * x**5)
        
        # Additional coupling term to increase nonlinearity and complexity
        f7 = 0.05 * np.sum(np.sin(x) * np.cos(2.5 * x) * np.sin(3.5 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
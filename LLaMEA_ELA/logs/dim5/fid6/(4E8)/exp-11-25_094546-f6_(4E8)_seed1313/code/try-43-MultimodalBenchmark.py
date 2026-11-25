import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Higher-degree polynomial terms for increased curvature and complexity
        f1 = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3)
        
        # Multiple high-frequency trigonometric components with varying amplitudes for dense local optima
        f2 = np.sum(
            1.2 * np.sin(3 * np.pi * x_norm) +
            0.8 * np.sin(7 * np.pi * x_norm) +
            0.5 * np.sin(12 * np.pi * x_norm) +
            0.3 * np.sin(18 * np.pi * x_norm)
        )
        
        # Radial exponential terms with variable decay rates to create steep gradients and plateaus
        f3 = np.sum(np.exp(-2.0 * x_norm**2) - 0.5 * np.exp(-0.5 * x_norm**2) - 1.0)
        
        # Cross-dimensional interaction terms with non-linear coupling for increased complexity
        f4 = np.sum(
            x_norm[:-1] * x_norm[1:] * 
            (np.sin(3 * np.pi * x_norm[:-1]) + np.cos(3 * np.pi * x_norm[1:]))
        )
        
        # Additional harmonic terms to introduce chaotic behavior and further increase difficulty
        f5 = np.sum(
            0.4 * np.sin(10 * np.pi * x_norm**2) +
            0.2 * np.cos(15 * np.pi * x_norm**2)
        )
        
        # Combine all components with adaptive weights
        return 1.0 * f1 + 0.5 * f2 + 0.3 * f3 + 0.15 * f4 + 0.25 * f5
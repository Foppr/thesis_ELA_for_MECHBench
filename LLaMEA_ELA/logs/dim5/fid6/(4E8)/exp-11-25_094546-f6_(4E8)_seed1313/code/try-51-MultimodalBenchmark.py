import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Higher-degree polynomial terms for increased curvature and complexity
        f1 = np.sum(0.9 * x_norm**7 + 0.6 * x_norm**5 + 0.4 * x_norm**3 + 0.2 * x_norm**2)
        
        # Multiple high-frequency trigonometric components with varying amplitudes for dense local optima
        f2 = np.sum(
            1.3 * np.sin(4 * np.pi * x_norm) +
            0.9 * np.sin(8 * np.pi * x_norm) +
            0.6 * np.sin(15 * np.pi * x_norm) +
            0.4 * np.sin(20 * np.pi * x_norm)
        )
        
        # Radial exponential terms with variable decay rates to create steep gradients and plateaus
        f3 = np.sum(np.exp(-2.5 * x_norm**2) - 0.6 * np.exp(-0.7 * x_norm**2) - 1.2)
        
        # Cross-dimensional interaction terms with non-linear coupling for increased complexity
        f4 = np.sum(
            x_norm[:-1] * x_norm[1:] * 
            (np.sin(4 * np.pi * x_norm[:-1]) + np.cos(4 * np.pi * x_norm[1:]))
        )
        
        # Additional harmonic terms to introduce chaotic behavior and further increase difficulty
        f5 = np.sum(
            0.5 * np.sin(12 * np.pi * x_norm**2) +
            0.3 * np.cos(18 * np.pi * x_norm**2)
        )
        
        # Cross-dimensional coupling with exponential interaction
        f6 = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Combine all components with adaptive weights
        return 1.2 * f1 + 0.6 * f2 + 0.4 * f3 + 0.2 * f4 + 0.3 * f5 + 0.1 * f6
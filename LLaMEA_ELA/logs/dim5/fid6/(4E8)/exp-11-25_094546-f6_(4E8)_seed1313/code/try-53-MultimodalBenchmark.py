import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractional polynomial terms with non-integer exponents for irregular curvature
        f1 = np.sum(0.7 * np.abs(x_norm)**1.7 + 0.4 * np.abs(x_norm)**2.3 + 0.2 * np.abs(x_norm)**3.1)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(
            1.5 * np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) +
            0.9 * np.sin(11 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) +
            0.4 * np.sin(19 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm)
        )
        
        # Radial adaptive barrier terms with varying strength and decay
        f3 = np.sum(
            2.0 * np.exp(-0.5 * (x_norm**2)) * (1.0 + 0.3 * np.sin(10 * np.pi * x_norm**2)) +
            1.0 * np.exp(-2.0 * (x_norm**2)) * (1.0 + 0.2 * np.cos(15 * np.pi * x_norm**2))
        )
        
        # Cross-dimensional coupling with chaotic mixing through trigonometric products
        f4 = np.sum(
            np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * 
            (np.cos(2 * np.pi * x_norm[:-1]) + np.sin(2 * np.pi * x_norm[1:]))
        )
        
        # Chaotic oscillation terms with time-varying frequencies
        f5 = np.sum(
            0.6 * np.sin(8 * np.pi * x_norm**1.5) * np.cos(5 * np.pi * x_norm**1.3) +
            0.3 * np.sin(12 * np.pi * x_norm**2.1) * np.cos(9 * np.pi * x_norm**1.7)
        )
        
        # Combine all components with dynamically adjusted weights
        return 1.2 * f1 + 0.8 * f2 + 0.6 * f3 + 0.2 * f4 + 0.4 * f5
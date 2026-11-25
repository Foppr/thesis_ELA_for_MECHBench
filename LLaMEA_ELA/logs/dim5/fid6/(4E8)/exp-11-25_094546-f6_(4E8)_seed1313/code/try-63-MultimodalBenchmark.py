import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractional polynomial terms with non-integer exponents for irregular curvature
        f1 = np.sum(0.8 * np.abs(x_norm)**1.9 + 0.5 * np.abs(x_norm)**2.7 + 0.3 * np.abs(x_norm)**3.5)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(
            1.8 * np.sin(6 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) +
            1.1 * np.sin(13 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) +
            0.5 * np.sin(21 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm)
        )
        
        # Radial adaptive barrier terms with varying strength and decay
        f3 = np.sum(
            2.5 * np.exp(-0.3 * (x_norm**2)) * (1.0 + 0.4 * np.sin(12 * np.pi * x_norm**2)) +
            1.5 * np.exp(-1.5 * (x_norm**2)) * (1.0 + 0.3 * np.cos(18 * np.pi * x_norm**2))
        )
        
        # Cross-dimensional coupling with chaotic mixing through trigonometric products
        f4 = np.sum(
            np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * 
            (np.cos(2.5 * np.pi * x_norm[:-1]) + np.sin(2.5 * np.pi * x_norm[1:]))
        )
        
        # Chaotic oscillation terms with time-varying frequencies
        f5 = np.sum(
            0.7 * np.sin(9 * np.pi * x_norm**1.6) * np.cos(6 * np.pi * x_norm**1.4) +
            0.4 * np.sin(14 * np.pi * x_norm**2.3) * np.cos(10 * np.pi * x_norm**1.9)
        )
        
        # Additional chaotic mixing term to increase landscape irregularity
        f6 = np.sum(
            0.3 * np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) *
            np.exp(-0.1 * np.abs(x_norm))
        )
        
        # Combine all components with dynamically adjusted weights
        return 1.3 * f1 + 0.9 * f2 + 0.7 * f3 + 0.3 * f4 + 0.5 * f5 + 0.2 * f6
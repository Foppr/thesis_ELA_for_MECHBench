import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Add chaotic sine waves with varying frequencies and amplitudes
        f2 = 0.4 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Add higher-order polynomial terms with adaptive scaling
        f3 = 0.03 * np.sum(x_norm**4)
        f4 = 0.015 * np.sum(x_norm**6)
        
        # Add dynamic conditioning with exponential decay
        f5 = 0.02 * np.sum(np.exp(-x_norm**2) * x_norm**2)
        
        # Add cross-dimension interaction terms with varying coefficients
        f6 = 0.025 * np.sum(x_norm[:-1]**2 * x_norm[1:]**2)
        f7 = 0.01 * np.sum(x_norm[:-2]**3 * x_norm[2:]**3)
        
        # Add a complex trigonometric modulation with multiple frequencies
        f8 = 0.15 * np.sum(np.sin(10 * np.pi * x_norm) + np.cos(5 * np.pi * x_norm))
        
        # Add a term that creates sharp transitions and ruggedness
        f9 = 0.05 * np.sum(np.abs(x_norm)**1.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
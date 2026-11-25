import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with irrational frequency ratios
        f2 = np.sum(np.sin(3.14159 * x_norm) ** 2 + np.sin(2.71828 * x_norm) ** 2 + 
                   0.7 * np.sin(1.41421 * x_norm) ** 2)
        
        # High-frequency chaotic terms with varying amplitudes
        f3 = np.sum(np.sin(20 * np.pi * x_norm) ** 2 + 0.5 * np.sin(25 * np.pi * x_norm) ** 2 + 
                   0.3 * np.sin(30 * np.pi * x_norm) ** 2)
        
        # Exponential polynomial interaction terms with varying exponents
        f4 = np.sum(2.0 * np.exp(0.5 * x_norm**2) - 2.0 + 0.8 * np.exp(0.3 * x_norm**4) - 0.8)
        
        # Cross-dimensional coupling with chaotic interaction coefficients
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f5 += np.sin(x_norm[i] * x_norm[j] * 10.0) ** 2
        
        # Combined with a modified Gaussian-like term to create sharp valleys
        f6 = np.sum(np.exp(-0.5 * x_norm**2) - 0.5)
        
        # Combine all terms with carefully tuned weights
        return 0.5 * f1 + 0.3 * f2 + 0.1 * f3 + 0.05 * f4 + 0.03 * f5 - 0.08 * f6
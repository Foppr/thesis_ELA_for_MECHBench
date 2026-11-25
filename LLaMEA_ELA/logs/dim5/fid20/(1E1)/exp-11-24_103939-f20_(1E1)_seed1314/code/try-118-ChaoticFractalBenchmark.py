import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute delay indices for chaotic behavior
        self.delay_indices = np.arange(1, min(11, dim + 1))
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term with varying weights
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Fractal-like structure using recursive sine components
        f2 = 0.0
        for i in range(self.dim):
            val = x_norm[i]
            # Recursive sine application for fractal effect
            for _ in range(3):
                val = np.sin(val * np.pi)
            f2 += val**2
        
        # Time-delayed chaotic sinusoidal components
        f3 = 0.0
        for i in range(self.dim):
            delayed_val = x_norm[i]
            if i >= self.delay_indices[0]:
                delayed_val = x_norm[i - self.delay_indices[0]]
            f3 += np.sin(10 * x_norm[i] + 0.5 * np.sin(7 * delayed_val))**2
        
        # Multi-scale oscillation with non-uniform frequency scaling
        f4 = 0.0
        for i in range(self.dim):
            scale = (i + 1) / self.dim
            freq = 20 * scale + 5
            f4 += np.sin(freq * x_norm[i])**4
        
        # Asymmetric saddle with polynomial perturbation
        f5 = 0.0
        for i in range(self.dim):
            f5 += (x_norm[i]**3 - 0.3 * x_norm[i])**2
        
        # Boundary-sensitive fractal penalty
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.exp(5 * (1 - np.abs(x_norm[i]))) * np.sin(20 * x_norm[i])**2
        
        # Cross-dimensional coupling with exponential interaction
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                f7 += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(x_norm[i] * x_norm[j])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
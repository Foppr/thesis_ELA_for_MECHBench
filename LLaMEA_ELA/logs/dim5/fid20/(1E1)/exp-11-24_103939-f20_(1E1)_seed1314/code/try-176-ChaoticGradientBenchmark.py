import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Chaotic gradient component with exponential decay
        f1 = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(2 * np.pi * x_scaled))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        f2 = np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # Asymmetric basin structure with exponential potentials
        f3 = np.sum(np.exp(0.5 * (x_scaled**2)) * (x_scaled**2 - 1)**2)
        
        # Cross-dimensional interaction with chaotic coupling coefficients
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(i * j / self.dim) + 0.5 * np.cos(i + j)
                f4 += coupling * np.sin(x_scaled[i]) * np.cos(x_scaled[j])
        
        # Multi-scale oscillation with varying decay rates
        f5 = np.sum(np.sin(20 * x_scaled) * np.exp(-0.1 * np.abs(x_scaled)))
        
        # Boundary avoidance with asymmetric penalty
        f6 = 0.5 * np.sum((np.abs(x_scaled) - 1)**4 + (np.abs(x_scaled) - 0.5)**3)
        
        # Exponential decay interaction terms with random weights
        f7 = 0.0
        for i in range(self.dim):
            weight = 0.3 + 0.7 * np.sin(i * np.pi / self.dim)
            f7 += weight * np.exp(-0.5 * x_scaled[i]**2) * np.cos(15 * x_scaled[i])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7
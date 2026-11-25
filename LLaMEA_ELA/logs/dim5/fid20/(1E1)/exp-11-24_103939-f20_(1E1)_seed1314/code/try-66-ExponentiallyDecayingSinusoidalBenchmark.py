import numpy as np

class ExponentiallyDecayingSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        f1 = np.sum(x_scaled**2)
        
        # Exponentially decaying sinusoidal components with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Frequencies: 1, 2, 4, 8, 1, 2, 4, 8, ...
            decay = np.exp(-0.1 * i)
            f2 += decay * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-dimensional interaction with exponential weighting
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.05 * (i + j))
                f3 += weight * np.sin(x_scaled[i] * x_scaled[j]) * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Multi-modal structure with Gaussian peaks and varying heights
        f4 = 0.0
        num_peaks = min(8, self.dim)
        for k in range(num_peaks):
            center = np.sin(k) * 0.5
            height = 1.0 + 0.5 * np.cos(k)
            width = 0.3 + 0.2 * np.sin(k)
            f4 -= height * np.exp(-0.5 * ((x_scaled - center) / width)**2)
        
        # Asymmetric saddle point structure with increasing complexity
        f5 = 0.0
        for i in range(self.dim):
            f5 += (x_scaled[i]**3 - 0.5 * x_scaled[i])**2
        
        # Boundary avoidance penalty with dimensionality-dependent scaling
        f6 = 0.0
        for i in range(self.dim):
            f6 += 0.1 * np.abs(x_scaled[i])**3 + 0.05 * np.abs(x_scaled[i])**4
        
        return f1 + f2 + f3 + f4 + f5 + f6
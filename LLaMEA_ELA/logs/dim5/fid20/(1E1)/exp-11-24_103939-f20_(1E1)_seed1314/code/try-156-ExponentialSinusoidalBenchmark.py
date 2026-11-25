import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Exponentially decaying sinusoidal terms with nested frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2 ** (i + 1)
            f1 += np.exp(-0.1 * i) * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] / 2)
        
        # Quadratic interaction terms with exponentially weighted coefficients
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.05 * (i + j))
                f2 += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j])
        
        # Central attractive basin with Gaussian decay
        center_dist = np.sum(x_scaled**2)
        f3 = -np.exp(-0.5 * center_dist / self.dim)
        
        # Multi-scale harmonic modulation for increased complexity
        f4 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.5 * i)
            f4 += scale * np.sin(3 * x_scaled[i]) * np.cos(7 * x_scaled[i]) * np.sin(11 * x_scaled[i])
        
        # Asymmetric penalty for boundary avoidance with exponential scaling
        f5 = 0.0
        for i in range(self.dim):
            f5 += 2.0 * np.exp(2.0 * np.abs(x_scaled[i])) - 2.0
        
        return f1 + f2 + f3 + f4 + f5
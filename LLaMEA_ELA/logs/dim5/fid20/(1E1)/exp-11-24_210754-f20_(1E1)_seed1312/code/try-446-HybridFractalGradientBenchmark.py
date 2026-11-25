import numpy as np

class HybridFractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractional Brownian motion scaling factors
        self.brownian_scaling = np.array([1.0 / (2**i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with varying centers and widths
        centers = np.linspace(-4, 4, min(10, self.dim))
        if self.dim > 10:
            centers = np.concatenate([centers, np.random.uniform(-4, 4, self.dim - 10)])
        
        f1 = 0.0
        for i in range(min(10, self.dim)):
            center = centers[i]
            width = 0.5 + 0.5 * np.sin(i)  # Varying widths
            f1 += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Fractional Brownian motion noise component
        f2 = 0.0
        for i in range(self.dim):
            # Simulate fractional Brownian motion with Hurst parameter 0.3
            noise = np.random.normal(0, 1) * self.brownian_scaling[i % len(self.brownian_scaling)]
            f2 += noise * np.sin(2.0 * x[i])
        
        # Directional gradient modulation with implicit bias
        f3 = 0.0
        for i in range(self.dim):
            # Implicit bias towards first few dimensions
            bias_factor = 1.0 + 0.5 * np.sin(i * 0.5)
            f3 += bias_factor * x[i]**3
        
        # Multi-scale harmonic interference with varying amplitudes
        f4 = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            amp = 1.0 / (1.0 + i * 0.2)
            f4 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Fractal-like self-similarity with recursive modulation
        f5 = 0.0
        for i in range(self.dim):
            # Recursive modulation using sine of previous values
            if i > 0:
                mod = np.sin(x[i-1])
                f5 += x[i]**2 * mod
        
        # Combine all components with dynamic weights based on dimensionality
        weight1, weight2, weight3, weight4, weight5 = (
            0.3, 0.2, 0.25, 0.15, 0.1
        )
        
        return weight1 * f1 + weight2 * f2 + weight3 * f3 + weight4 * f4 + weight5 * f5
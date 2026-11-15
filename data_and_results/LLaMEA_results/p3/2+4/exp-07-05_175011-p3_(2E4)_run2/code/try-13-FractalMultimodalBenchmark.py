import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.scales = np.logspace(0, 2, num=min(5, dim), base=2, endpoint=True)
        self.frequencies = 2 * np.pi * (1 + np.arange(dim))
        self.radial_exponents = 1 + np.arange(dim) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Radial component with fractal scaling
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum((r**self.radial_exponents) * np.sin(self.frequencies * r))
        
        # Multi-scale sine-wave modulation
        modulated = 0.0
        for i, scale in enumerate(self.scales):
            if i < self.dim:
                modulated += np.sin(scale * self.frequencies[i] * x_norm[i]) * \
                            np.cos(scale * self.frequencies[i] * x_norm[i]**2)
        
        # Add fractal-like interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(self.frequencies[i] * x_norm[j]) * \
                              np.cos(self.frequencies[j] * x_norm[i]) * \
                              np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Quadratic basin for convergence guidance
        quadratic = np.sum(x_norm**2)
        
        # Add noise for ruggedness
        noise = 0.005 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        
        return radial + modulated + interaction + quadratic + noise
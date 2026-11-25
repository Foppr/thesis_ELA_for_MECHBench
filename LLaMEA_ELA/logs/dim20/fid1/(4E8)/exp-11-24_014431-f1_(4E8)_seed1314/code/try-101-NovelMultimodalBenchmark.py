import numpy as np

class NovelMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(2.0 * np.pi * x[i]) + 0.2 * np.cos(3.0 * np.pi * x[i]) + \
                     0.15 * np.sin(5.0 * np.pi * x[i]) + 0.1 * np.cos(7.0 * np.pi * x[i])
        
        # Add radial basis function components with varying centers and widths
        centers = np.linspace(-4.0, 4.0, self.dim)
        widths = np.logspace(-1, 1, self.dim)
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.5 * ((x[i] - centers[i]) / widths[i])**2)
        
        # Add cross-dimensional polynomial interactions with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j])**2)
        
        # Add a multi-scale harmonic interaction term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[j]) * (1 + 0.2 * np.sin(2.0 * (x[i] + x[j])))
        
        # Add a global sine modulation with varying frequency
        f_val += 0.25 * np.sin(0.3 * np.sum(x)**2) + 0.15 * np.cos(0.4 * np.sum(x)**3)
        
        # Add exponential penalty terms for boundary avoidance
        for i in range(self.dim):
            f_val += 0.3 * np.exp(-0.3 * (x[i] - 4.0)**2) + 0.2 * np.exp(-0.2 * (x[i] + 4.0)**2)
        
        # Add a conditioning term with varying polynomial degrees
        f_val += 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6) + 0.02 * np.sum(x**8)
        
        return f_val
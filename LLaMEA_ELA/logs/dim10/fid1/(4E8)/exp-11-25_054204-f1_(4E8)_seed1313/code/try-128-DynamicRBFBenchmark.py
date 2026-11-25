import numpy as np

class DynamicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic parameters for chaotic modulation
        self.params = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1)) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with dynamic exponents
        exponents = 2.0 + 2.0 * self.params
        f1 = np.sum(x**exponents)
        
        # Trigonometric coupling with adaptive frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * self.params[i]
            f2 += np.sin(freq * x[i])**2 + np.cos(freq * x[i])**2
        
        # Radial basis function component with dynamic centers
        f3 = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 1))
            sigma = 0.5 + 0.3 * self.params[i]
            f3 += np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Cross-dimensional polynomial interactions
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += (x[i]**3) * (x[i+1]**2) + (x[i]**2) * (x[i+1]**3)
        
        # Sine-cosine harmonic coupling
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(x[i]) * np.cos(2.0 * x[i]) * self.params[i]
        
        # Chaotic logistic modulation with dynamic parameter
        f6 = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.2 * self.params[i]
            chaotic_val = r * self.params[i] * (1 - self.params[i])
            f6 += np.sin(chaotic_val * x[i]) * np.cos(x[i])
        
        # Multi-modal polynomial with variable coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            f7 += coeff * x[i]**5
        
        # Exponential interaction term
        f8 = 0.0
        for i in range(self.dim - 1):
            f8 += np.exp(-0.5 * (x[i] - x[i+1])**2)
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)
import numpy as np

class RecursiveFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute recursive fractal scaling factors
        self.fractal_factors = np.power(0.5, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Recursive fractal component with exponential scaling
        f2 = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            f2 += scale * np.sin(np.pi * x[i] * np.exp(-scale * x[i]**2))
            
        # Dynamic exponential modulation with chaotic frequency
        f3 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(x[i] / (i + 1.0))  # Chaotic frequency modulation
            f3 += np.exp(-x[i]**2) * np.cos(freq * x[i])
            
        # Cross-dimensional recursive coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(x[i] * x[i+1]) * np.exp(-np.abs(x[i] - x[i+1]))
            
        # Fractal-like higher-order polynomial interactions
        f5 = 0.0
        for i in range(self.dim):
            f5 += (x[i]**5) * np.sin(2.0 * x[i]) * self.fractal_factors[i]
            
        # Adaptive exponential decay with sinusoidal modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.exp(-x[i]**2 / (i + 1.0)) * np.cos(3.0 * x[i])
            
        # Multi-scale fractal coupling with varying exponents
        f7 = 0.0
        for i in range(self.dim - 2):
            exp_factor = 1.5 + 0.5 * np.sin(i / (self.dim + 1.0))
            f7 += np.sin(x[i] * x[i+1] * x[i+2]) * np.exp(-x[i]**exp_factor)
            
        # Recursive harmonic component with diminishing weights
        f8 = 0.0
        for i in range(self.dim):
            weight = self.fractal_factors[i]
            f8 += weight * np.sin(4.0 * x[i] + np.cos(x[i]))
            
        # Complex exponential coupling with dynamic scaling
        f9 = 0.0
        for i in range(self.dim - 1):
            scale = 1.0 + 0.5 * np.cos(i / (self.dim + 2.0))
            f9 += np.exp(-x[i]**2) * np.sin(scale * x[i+1])
            
        # Sine-cosine hybrid with fractal frequency modulation
        f10 = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 1.5 * np.sin(np.log(i + 2.0))
            f10 += np.sin(freq_mod * x[i]) * np.cos(2.0 * x[i])
            
        # Multi-fractal interaction with recursive dimension scaling
        f11 = 0.0
        for i in range(self.dim - 1):
            dim_scale = self.dim / (i + 1.0)
            f11 += np.sin(x[i] * x[i+1] * dim_scale) * np.cos(x[i])
            
        # Recursive polynomial with exponential decay
        f12 = 0.0
        for i in range(self.dim):
            poly_term = (x[i]**6) * np.exp(-x[i]**2)
            f12 += poly_term
            
        # Combined scaling factor based on recursive fractal structure
        scale_factor = 1.0 + 0.5 * np.sum(self.fractal_factors)
        
        # Final function value with adjusted weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)
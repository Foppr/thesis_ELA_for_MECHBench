import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic base with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        base = 0.1 * r**2
        
        # Fractal-like trigonometric structure with recursive frequency modulation
        fractal = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + r / (self.dim + 1))
            amp = 1.0 + 0.5 * np.cos(0.2 * i)
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Nested harmonic layers with varying amplitudes
        nested = 0.0
        for layer in range(1, 4):
            for i in range(self.dim):
                freq = 3.0 * layer + 2.0 * np.sin(0.4 * i + layer * r / self.dim)
                nested += (1.0 / layer) * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point enhanced with radial symmetry
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    saddle += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning based on position
        cond = 1.0 + 0.3 * np.sin(r / 2.0) * np.cos(r / 3.0)
        
        # Logarithmic barrier with chaotic perturbations
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.25 * np.log(1.0 + 0.3 * np.abs(x[i]) + 0.1 * x[i]**2) * \
                      (1.0 + 0.2 * np.sin(5.0 * x[i]))
        
        # Multi-scale interaction terms
        multi_scale = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                multi_scale += 0.15 * np.sin(x[i]) * np.cos(x[i+1]) * \
                              np.exp(-0.02 * (x[i]**2 + x[i+1]**2)) * \
                              (1.0 + 0.1 * np.sin(3.0 * r))
        
        return cond * (base + fractal + nested + saddle + barrier + multi_scale)
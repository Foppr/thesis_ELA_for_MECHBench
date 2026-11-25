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
        for layer in range(1, 5):
            for i in range(self.dim):
                freq = 3.0 * layer + 2.0 * np.sin(0.4 * i + layer * r / self.dim)
                nested += (1.0 / layer**1.5) * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point enhanced with radial symmetry
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    saddle += 0.3 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning based on position
        cond = 1.0 + 0.4 * np.sin(r / 2.0) * np.cos(r / 3.0) + 0.1 * np.sin(7.0 * r)
        
        # Enhanced logarithmic barrier with chaotic perturbations
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.4 * np.log(1.0 + 0.5 * np.abs(x[i]) + 0.2 * x[i]**2) * \
                      (1.0 + 0.3 * np.sin(5.0 * x[i] + 0.6 * r))
        
        # Multi-scale interaction terms with enhanced complexity
        multi_scale = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                multi_scale += 0.3 * np.sin(x[i]) * np.cos(x[i+1]) * \
                              np.exp(-0.04 * (x[i]**2 + x[i+1]**2)) * \
                              (1.0 + 0.2 * np.sin(4.0 * r + 0.4 * i))
        
        # Additional chaotic cross-terms for increased complexity
        chaos_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_cross += 0.15 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                              np.exp(-0.015 * r) * (1.0 + 0.1 * np.sin(3.0 * x[i] + 2.0 * x[j]))
        
        # Add noise component for increased challenge
        noise = 0.05 * np.random.rand()
        
        return cond * (base + fractal + nested + saddle + barrier + multi_scale + chaos_cross) + noise
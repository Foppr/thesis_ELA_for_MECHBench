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
            freq = 2.5 + 2.0 * np.sin(0.35 * i + r / (self.dim + 1))
            amp = 1.2 + 0.6 * np.cos(0.25 * i)
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Nested harmonic layers with varying amplitudes
        nested = 0.0
        for layer in range(1, 6):
            for i in range(self.dim):
                freq = 3.5 * layer + 2.5 * np.sin(0.45 * i + layer * r / self.dim)
                nested += (1.0 / layer**1.7) * np.sin(freq * x[i]) * np.exp(-0.12 * x[i]**2)
        
        # Saddle-point enhanced with radial symmetry
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    saddle += 0.4 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning based on position
        cond = 1.0 + 0.5 * np.sin(r / 2.0) * np.cos(r / 3.0) + 0.15 * np.sin(7.0 * r)
        
        # Enhanced logarithmic barrier with chaotic perturbations
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.5 * np.log(1.0 + 0.6 * np.abs(x[i]) + 0.25 * x[i]**2) * \
                      (1.0 + 0.35 * np.sin(5.0 * x[i] + 0.6 * r))
        
        # Multi-scale interaction terms with enhanced complexity
        multi_scale = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                multi_scale += 0.4 * np.sin(x[i]) * np.cos(x[i+1]) * \
                              np.exp(-0.05 * (x[i]**2 + x[i+1]**2)) * \
                              (1.0 + 0.25 * np.sin(4.0 * r + 0.4 * i))
        
        # Additional chaotic cross-terms for increased complexity
        chaos_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_cross += 0.2 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                              np.exp(-0.02 * r) * (1.0 + 0.15 * np.sin(3.0 * x[i] + 2.0 * x[j]))
        
        # Add noise component for increased challenge
        noise = 0.06 * np.random.rand()
        
        return cond * (base + fractal + nested + saddle + barrier + multi_scale + chaos_cross) + noise
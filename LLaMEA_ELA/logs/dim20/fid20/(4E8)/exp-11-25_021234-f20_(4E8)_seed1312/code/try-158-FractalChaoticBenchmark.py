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
        
        # Fractal-like trigonometric structure with recursive frequency modulation and chaos injection
        fractal = 0.0
        for i in range(self.dim):
            freq = 3.5 + 2.5 * np.sin(0.4 * i + r / (self.dim + 1)) + 0.5 * np.random.rand()
            amp = 1.8 + 0.8 * np.cos(0.3 * i) + 0.25 * np.random.rand()
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Nested harmonic layers with varying amplitudes and chaotic modulation
        nested = 0.0
        for layer in range(1, 8):
            for i in range(self.dim):
                freq = 4.5 * layer + 3.5 * np.sin(0.5 * i + layer * r / self.dim) + 0.35 * np.random.rand()
                nested += (1.0 / layer**2.2) * np.sin(freq * x[i]) * np.exp(-0.18 * x[i]**2)
        
        # Saddle-point enhanced with radial symmetry and chaotic perturbations
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    saddle += 0.35 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.09 * (x[i]**2 + x[j]**2)) * \
                             (1.0 + 0.2 * np.sin(4.0 * x[i] + 3.0 * x[j]))
        
        # Adaptive conditioning based on position with chaotic modulation
        cond = 1.0 + 0.45 * np.sin(r / 2.0) * np.cos(r / 3.8) + 0.1 * np.random.rand()
        
        # Logarithmic barrier with chaotic perturbations and multi-scale noise
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.4 * np.log(1.0 + 0.5 * np.abs(x[i]) + 0.2 * x[i]**2) * \
                      (1.0 + 0.35 * np.sin(6.0 * x[i]) + 0.25 * np.random.rand())
        
        # Multi-scale interaction terms with fractal-like recursive structure
        multi_scale = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                multi_scale += 0.3 * np.sin(x[i]) * np.cos(x[i+1]) * \
                              np.exp(-0.04 * (x[i]**2 + x[i+1]**2)) * \
                              (1.0 + 0.2 * np.sin(4.0 * r) + 0.1 * np.random.rand())
        
        # Add chaotic cross-dimensional coupling terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.2 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                                np.exp(-0.05 * (x[i]**2 + x[j]**2)) * \
                                (1.0 + 0.3 * np.sin(3.0 * r))
        
        # Add fractal-like self-similarity with chaotic scaling
        fractal_self = 0.0
        for i in range(self.dim):
            fractal_self += 0.1 * np.sin(5.5 * x[i] + 0.6 * r) * np.cos(3.5 * x[i]) * \
                           np.exp(-0.02 * x[i]**2) * (1.0 + 0.35 * np.random.rand())
        
        # Add chaotic noise with varying intensity based on dimensionality
        noise = 0.07 * np.sum(np.random.rand(self.dim)) * (1.0 + 0.15 * r / self.dim)
        
        return cond * (base + fractal + nested + saddle + barrier + multi_scale + cross_coupling + fractal_self) + noise
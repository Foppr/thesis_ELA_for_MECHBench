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
            freq = 2.5 + 1.8 * np.sin(0.35 * i + r / (self.dim + 1)) + 0.35 * np.random.rand()
            amp = 1.2 + 0.6 * np.cos(0.25 * i) + 0.15 * np.random.rand()
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Nested harmonic layers with varying amplitudes and chaotic modulation
        nested = 0.0
        for layer in range(1, 6):
            for i in range(self.dim):
                freq = 3.5 * layer + 2.5 * np.sin(0.45 * i + layer * r / self.dim) + 0.25 * np.random.rand()
                nested += (1.0 / layer**1.7) * np.sin(freq * x[i]) * np.exp(-0.12 * x[i]**2)
        
        # Saddle-point enhanced with radial symmetry and chaotic perturbations
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                if j < self.dim:
                    saddle += 0.25 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2)) * \
                             (1.0 + 0.12 * np.sin(3.5 * x[i] + 2.5 * x[j]))
        
        # Adaptive conditioning based on position with chaotic modulation
        cond = 1.0 + 0.35 * np.sin(r / 2.0) * np.cos(r / 3.0) + 0.06 * np.random.rand()
        
        # Logarithmic barrier with chaotic perturbations and multi-scale noise
        barrier = 0.0
        for i in range(self.dim):
            barrier += 0.3 * np.log(1.0 + 0.35 * np.abs(x[i]) + 0.12 * x[i]**2) * \
                      (1.0 + 0.25 * np.sin(5.5 * x[i]) + 0.15 * np.random.rand())
        
        # Multi-scale interaction terms with fractal-like recursive structure
        multi_scale = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                multi_scale += 0.2 * np.sin(x[i]) * np.cos(x[i+1]) * \
                              np.exp(-0.025 * (x[i]**2 + x[i+1]**2)) * \
                              (1.0 + 0.12 * np.sin(3.5 * r) + 0.06 * np.random.rand())
        
        # Add chaotic cross-dimensional coupling terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.12 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                                np.exp(-0.035 * (x[i]**2 + x[j]**2)) * \
                                (1.0 + 0.2 * np.sin(2.5 * r))
        
        # Add fractal-like self-similarity with chaotic scaling
        fractal_self = 0.0
        for i in range(self.dim):
            fractal_self += 0.06 * np.sin(4.5 * x[i] + 0.55 * r) * np.cos(2.5 * x[i]) * \
                           np.exp(-0.012 * x[i]**2) * (1.0 + 0.25 * np.random.rand())
        
        return cond * (base + fractal + nested + saddle + barrier + multi_scale + cross_coupling + fractal_self)
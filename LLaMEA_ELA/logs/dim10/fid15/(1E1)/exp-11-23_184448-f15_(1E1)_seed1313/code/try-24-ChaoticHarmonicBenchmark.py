import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with dynamic scaling
        base_term = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x**2) / self.dim))
        
        # Nested chaotic harmonic oscillations with fractal-like frequency modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            # Fractal frequency modulation based on position and dimension
            freq = 3.0 + 2.0 * np.sin(x[i] * 0.5) + 1.0 * np.cos(x[i] * 0.3)
            amp = 2.0 + 1.5 * np.sin(i * np.pi / self.dim) * np.cos(x[i] * 0.7)
            
            # Multi-scale chaotic modulation
            chaos_mod = 0.4 * np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 3.0)
            freq_mod = freq * (1.0 + 0.3 * chaos_mod)
            amp_mod = amp * (1.0 + 0.2 * np.sin(x[i] * np.pi / 4.0))
            
            # Exponentially decaying harmonic with fractal decay rate
            decay = np.exp(-0.15 * np.abs(x[i]) * (1.0 + 0.1 * np.sin(x[i] * 0.5)))
            harmonic_term += amp_mod * np.sin(freq_mod * x[i]) * decay
        
        # Dynamic cross-dimensional coupling with chaotic interaction patterns
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both dimensions and position
                coupling_strength = 0.6 + 0.4 * np.sin(i * j * np.pi / (self.dim + 3)) * \
                                  np.cos((x[i] + x[j]) * 0.5)
                # Fractal coupling interaction
                coupling_term += coupling_strength * np.sin(x[i] * x[j]) * \
                                (np.abs(x[i]) + np.abs(x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Self-adaptive basin structures with chaotic center positions and depths
        basin_term = 0.0
        for i in range(self.dim):
            # Chaotic basin centers with nested fractal structure
            center = 3.0 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(x[i] * 0.3)
            depth = 0.8 + 0.4 * np.sin(i * np.pi / self.dim) * np.cos(x[i] * 0.7)
            
            # Fractal basin penalty with multi-scale exponential decay
            distance = np.abs(x[i] - center)
            basin_term += depth * (distance**2) * np.exp(-0.3 * distance) * \
                         (1.0 + 0.2 * np.sin(distance * 2.0))
        
        # Multi-scale chaotic perturbation with fractal scaling
        perturbation_term = 0.0
        scales = [1.0, 0.5, 0.25, 0.125]
        for scale in scales:
            scale_factor = 1.0 + 0.3 * np.sin(np.log(scale) * 3.0)
            for i in range(self.dim):
                perturbation_term += scale_factor * scale * \
                                  (np.sin(x[i] / scale) * np.cos(x[i] * scale) + 
                                   0.5 * np.sin(x[i] * scale * 2.0))
        
        # Dimensionality-dependent scaling with chaotic modulation
        dim_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1)) * np.cos(self.dim * 0.1)
        
        return dim_scale * (base_term + 0.5 * harmonic_term + 0.3 * coupling_term + 
                           0.4 * basin_term + 0.25 * perturbation_term)
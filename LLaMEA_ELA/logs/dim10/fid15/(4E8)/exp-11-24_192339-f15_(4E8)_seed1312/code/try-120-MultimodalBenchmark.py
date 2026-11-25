import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial basis components with fractal-like scaling
        rb_func = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            rb_func += np.exp(-scale * np.abs(x[i] - np.sin(i * np.pi / self.dim))**2)
        
        # Trigonometric coupling with fractal frequency modulation
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 2))
                freq_j = 1.0 + 0.5 * np.cos(j * np.pi / (self.dim + 2))
                trig_coupling += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Self-similar fractal structure with multi-scale interactions
        fractal_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 0.5 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                fractal_term += scale_factor * np.abs(x[i] - x[j])**3
        
        # Multi-hierarchical sinusoidal modulation with dynamic phase shifts
        hier_modulation = 0
        for i in range(self.dim):
            phase_shift = 0.2 * np.sin(i * np.pi / self.dim)
            hier_modulation += np.sin(2 * np.pi * x[i] + phase_shift) * np.cos(4 * np.pi * x[i] + 2 * phase_shift)
        
        # Global scaling and shifting
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        shift = 0.05 * np.sum(np.abs(x))
        
        # Combine all components with dynamic weighting
        return scale_factor * (0.4 * rb_func + 0.3 * trig_coupling + 0.2 * fractal_term + 0.1 * hier_modulation) + shift
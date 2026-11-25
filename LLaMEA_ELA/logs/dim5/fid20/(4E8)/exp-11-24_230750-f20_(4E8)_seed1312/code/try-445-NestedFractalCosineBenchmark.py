import numpy as np

class NestedFractalCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for sine modulation
        self.sine_freqs = np.random.uniform(1.0, 5.0, dim)
        self.sine_phases = np.random.uniform(0.0, 2*np.pi, dim)
        self.cosine_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.fractal_scaling = np.random.uniform(0.1, 0.9, dim)
        # Nested fractal parameters
        self.nested_levels = min(3, max(1, int(np.log2(dim))))
        self.nested_centers = np.random.uniform(-3.0, 3.0, (self.nested_levels, dim))
        self.nested_widths = np.random.uniform(0.5, 2.0, (self.nested_levels, dim))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal peaks with multi-level structure
        nested_fractal = 0.0
        for level in range(self.nested_levels):
            level_sum = 0.0
            for i in range(self.dim):
                center = self.nested_centers[level, i]
                sigma = self.nested_widths[level, i]
                # Fractal scaling with nesting
                scale_factor = np.power(self.fractal_scaling[level], 1.0 + 0.5 * level)
                level_sum += np.exp(-0.5 * ((x[i] - center) / (sigma * scale_factor))**2)
            nested_fractal += level_sum / (level + 1.0)
        
        # Dynamic cosine modulations with chaotic behavior
        cosine_mod = 0.0
        for i in range(self.dim):
            freq = self.sine_freqs[i]
            phase = self.sine_phases[i]
            amp = self.cosine_amplitudes[i]
            # Chaotic modulation using sine of position
            chaotic_mod = np.sin(2 * np.pi * x[i] + 0.3 * np.sin(x[i]**2))
            cosine_mod += amp * np.cos(freq * x[i] + phase) * chaotic_mod
        
        # Adaptive conditioning with nested structure
        conditioning = 0.0
        for i in range(self.dim):
            # Position-dependent conditioning factor
            pos_factor = 1.0 + 0.3 * np.sin(0.5 * x[i])
            # Multi-level fractal conditioning
            fractal_cond = 1.0
            for level in range(self.nested_levels):
                fractal_cond *= (1.0 + 0.2 * np.cos(self.fractal_scaling[level] * x[i]))
            conditioning += pos_factor * fractal_cond
        
        # Deceptive gradient with multiple local optima
        deceptive = 0.0
        for i in range(self.dim):
            # Multiple cosine components with different frequencies
            deceptive += (np.cos(2 * np.pi * x[i]) + 
                         0.5 * np.cos(4 * np.pi * x[i]) + 
                         0.2 * np.cos(8 * np.pi * x[i]))
        
        # Cross-dimensional quadratic couplings with nested weights
        quadratic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Nested weight based on fractal levels
                weight = 1.0 + 0.4 * np.sin(self.fractal_scaling[0] * x[i])
                quadratic_coupling += weight * (x[i]**2 - x[j]**2) * np.sin(0.3 * (x[i] + x[j]))
        
        # Combine all components with dynamic scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim)
        return (0.25 * nested_fractal + 0.30 * cosine_mod + 
                0.20 * conditioning + 0.15 * deceptive + 0.10 * quadratic_coupling) * dim_factor
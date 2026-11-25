import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(5, max(2, dim // 3))
        self.adaptivity_factor = 0.3 + 0.4 * (dim / 10.0)
        
    def f(self, x):
        # Normalize input to [-1, 1] for fractal generation
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal component using recursive self-similarity
        fractal_value = 0.0
        for i in range(self.fractal_depth):
            scale = 2 ** i
            period = 2 * np.pi / scale
            fractal_value += np.sum(np.sin(x_norm * scale * period) ** 2)
        
        # Adaptive gradient field with dimension-dependent modulation
        grad_field = 0.0
        for i in range(self.dim):
            # Dynamic modulation based on position and dimension
            mod_freq = 1 + self.adaptivity_factor * np.sin(i * 0.5)
            mod_amp = 1 + 0.5 * np.cos(i * 0.3)
            grad_field += mod_amp * np.sin(x[i] * mod_freq) * np.cos(x[i] * mod_freq**2)
        
        # Multi-scale harmonic interference
        harmonic_sum = 0.0
        for i in range(self.dim):
            for k in range(1, min(6, self.dim + 1)):
                harmonic_sum += (1/k) * np.sin(k * x[i]) * np.cos(k * x[i] * 0.7)
        
        # Asymmetric potential wells with varying depth
        potential_well = 0.0
        for i in range(self.dim):
            # Create asymmetric basins using polynomial and exponential terms
            well_term = (x[i]**3 + 0.5 * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
            potential_well += well_term
        
        # Global scaling factor with fractal dimension influence
        dim_scaling = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components
        total_value = dim_scaling * (0.3 * fractal_value + 0.4 * grad_field + 
                                   0.15 * harmonic_sum + 0.15 * potential_well)
        
        return total_value
import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(6, max(3, dim // 2))
        self.adaptivity_factor = 0.4 + 0.3 * (dim / 15.0)
        
    def f(self, x):
        # Normalize input to [-1, 1] for fractal generation
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal component using recursive self-similarity with enhanced complexity
        fractal_value = 0.0
        for i in range(self.fractal_depth):
            scale = 2 ** (i + 1)
            period = 2 * np.pi / scale
            fractal_value += np.sum(np.sin(x_norm * scale * period) ** 3)
        
        # Adaptive gradient field with enhanced dimensionality modulation
        grad_field = 0.0
        for i in range(self.dim):
            mod_freq = 1 + self.adaptivity_factor * np.sin(i * 0.7)
            mod_amp = 1 + 0.6 * np.cos(i * 0.4)
            grad_field += mod_amp * np.sin(x[i] * mod_freq) * np.cos(x[i] * mod_freq**1.5)
        
        # Multi-scale harmonic interference with improved weighting
        harmonic_sum = 0.0
        for i in range(self.dim):
            for k in range(1, min(8, self.dim + 3)):
                harmonic_sum += (1/k**1.2) * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
        
        # Asymmetric potential wells with improved depth and smoother transitions
        potential_well = 0.0
        for i in range(self.dim):
            # Create asymmetric basins using polynomial and exponential terms with better balance
            well_term = (x[i]**4 + 0.3 * x[i]**3) * np.exp(-0.15 * np.abs(x[i]))
            potential_well += well_term
        
        # Global scaling factor with improved fractal dimension influence
        dim_scaling = 1.0 + 0.15 * np.log(self.dim + 2)
        
        # Combine all components with adjusted weights for better balance
        total_value = dim_scaling * (0.25 * fractal_value + 0.35 * grad_field + 
                                   0.2 * harmonic_sum + 0.2 * potential_well)
        
        return total_value
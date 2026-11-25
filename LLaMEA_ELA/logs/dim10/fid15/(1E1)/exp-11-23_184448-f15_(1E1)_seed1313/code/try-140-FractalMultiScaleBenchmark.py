import numpy as np

class FractalMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial potential with varying degrees
        poly_term = np.sum(x**4 + 0.5 * x**2)
        
        # Multi-scale sinusoidal modulation with fractal-like scaling
        scale_factor = 1.0
        sin_term = 0.0
        for i in range(self.dim):
            # Apply multiple scales
            for scale in [0.5, 1.0, 2.0, 4.0]:
                freq = scale * (i + 1) * np.pi / (self.dim + 1)
                sin_term += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5) * np.exp(-scale * 0.1)
        
        # Self-similar fractal structure with recursive scaling
        fractal_term = 0.0
        for level in range(3):
            level_scale = 2.0 ** level
            for i in range(self.dim):
                if i % (level + 1) == 0:
                    fractal_term += np.sin(x[i] * level_scale) * np.cos(x[i] * level_scale * 0.7)
        
        # Coupling between dimensions with distance-dependent weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-dist * 0.5) / (dist + 1e-8)
                coupling_term += weight * (x[i]**2 + x[j]**2)
        
        # Polynomial landscape with variable exponents
        exponent_term = 0.0
        for i in range(self.dim):
            exp_val = 2 + 3 * np.sin(i * np.pi / (self.dim + 1))
            exponent_term += np.abs(x[i])**exp_val
        
        # Add noise-like irregularities with chaotic scaling
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.sin(x[i] * (i + 1) * np.pi / (self.dim + 1)) * \
                         np.cos(x[i] * (i + 2) * np.pi / (self.dim + 2)) * \
                         np.tan(x[i] * (i + 3) * np.pi / (self.dim + 3))
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (0.3 * poly_term + 0.25 * sin_term + 
                            0.2 * fractal_term + 0.15 * coupling_term + 
                            0.05 * exponent_term + 0.05 * noise_term)
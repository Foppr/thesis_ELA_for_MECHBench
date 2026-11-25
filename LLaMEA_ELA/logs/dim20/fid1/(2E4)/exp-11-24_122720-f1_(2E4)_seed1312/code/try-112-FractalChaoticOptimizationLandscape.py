import numpy as np

class FractalChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal constants for different dimensions
        self.fractal_constants = np.array([np.sin(i * np.pi / (dim + 1)) * np.cos(i * np.pi / (dim + 2)) 
                                          for i in range(dim)])
        
    def f(self, x):
        # Ensure bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometric component using self-similar patterns
        fractal_sum = 0
        for i in range(self.dim):
            # Self-similar scaling with dimension-dependent base
            base = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            scale = np.power(base, i + 1)
            fractal_sum += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale**0.5)
        
        # Chaotic attractor dynamics component
        chaotic_sum = 0
        for i in range(self.dim):
            # Logistic map based chaotic sequence
            r = 3.9 + 0.1 * np.sin(i * np.pi / (self.dim + 4))
            x_prev = x[i] if i == 0 else x[i-1]
            chaotic_term = r * x_prev * (1 - x_prev)
            chaotic_sum += chaotic_term * np.exp(-0.5 * x[i]**2) * np.sin(x[i])
        
        # Adaptive dimensionality scaling with fractal influence
        dim_scaling = np.sum(self.fractal_constants * np.abs(x)) / self.dim
        
        # Multi-scale harmonic modulation
        harmonic_sum = 0
        for i in range(self.dim):
            freq1 = 2.0 + np.sin(i * np.pi / (self.dim + 5))
            freq2 = 1.0 + np.cos(i * np.pi / (self.dim + 6))
            harmonic_sum += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.1 * dim_scaling)
        
        # Cross-dimensional coupling with fractal weights
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = self.fractal_constants[i] * self.fractal_constants[j]
                coupling_sum += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Final scaling and combination
        total = (0.3 * fractal_sum + 
                0.25 * chaotic_sum + 
                0.25 * harmonic_sum + 
                0.2 * coupling_sum)
        
        # Add dimensionality-dependent penalty for large values
        penalty = 0.1 * np.sum(np.abs(x)**3) / self.dim
        
        return total + penalty
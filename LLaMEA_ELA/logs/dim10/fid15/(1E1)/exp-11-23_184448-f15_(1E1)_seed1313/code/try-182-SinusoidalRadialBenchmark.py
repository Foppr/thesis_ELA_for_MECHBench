import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Radial component with exponential decay
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Sinusoidal oscillations in each dimension
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            sin_term += np.sin(x[i] * freq) * np.cos(x[i] * freq)
        
        # Radial symmetry with multiple peaks
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += np.sin(r_squared * 0.5 + i * np.pi / self.dim) * np.cos(r_squared * 0.3 + i * np.pi / (self.dim + 2))
        
        # Cross-terms creating interaction between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Local minima landscape with varying depths
        local_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / self.dim)
            depth = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            local_term += depth * (x[i] - center)**2 * np.exp(-0.5 * (x[i] - center)**2)
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (0.3 * radial_term + 0.3 * sin_term + 
                            0.2 * symmetry_term + 0.15 * cross_term + 
                            0.05 * local_term)
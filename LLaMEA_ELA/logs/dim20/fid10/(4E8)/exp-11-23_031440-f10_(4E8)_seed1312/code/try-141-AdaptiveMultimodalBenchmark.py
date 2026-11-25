import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with chaotic coefficient modulation and varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)  # Varying degrees from 2 to 5
            coeff = 1.0 + 0.5 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            poly_term += coeff * (x_norm[i] ** degree)
        
        # Trigonometric component with chaotic frequency modulation and multi-scale interference
        trig_term = 0.0
        frequencies = [1, 2, 3, 4, 5]
        for i in range(self.dim):
            for j, freq in enumerate(frequencies):
                amp = 1.0 / (j + 1) * np.sin(j * np.pi / self.dim)
                phase = np.pi * i * (j + 1) / self.dim + 0.5 * np.sin(i * np.pi / (self.dim + 2))
                trig_term += amp * np.sin(freq * np.pi * x_norm[i] + phase) * \
                            np.cos(freq * np.pi * x_norm[i] + phase)
        
        # Radial basis function component with chaotic center placement and adaptive widths
        rbf_term = 0.0
        num_centers = min(7, self.dim)
        for i in range(num_centers):
            center = np.sin(i * np.pi / num_centers) * 0.5 + 0.2 * np.cos(i * np.pi / (num_centers + 1))
            width = 0.3 + 0.7 * np.cos(i * np.pi / num_centers) * np.sin(i * np.pi / (self.dim + 3))
            rbf_term += np.exp(-0.5 * ((x_norm[i % self.dim] - center) / width) ** 2)
        
        # Cross-dimensional coupling with chaotic strength modulation and multi-scale interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = 0.3 + 0.7 * np.sin((i + j) * np.pi / self.dim) * \
                                  np.cos((i - j) * np.pi / (self.dim + 1))
                cross_term += coupling_strength * np.sin(5 * np.pi * dist) * \
                             np.cos(3 * np.pi * dist) * (dist + 0.1)
        
        # Chaotic conditioning based on distance from origin and chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 3.0 * np.exp(-0.5 * r**2) * np.sin(6 * np.pi * r) * \
                          np.cos(4 * np.pi * r)
        
        # Multi-scale dimensionality-dependent scaling with chaotic modulation
        dim_scaling = 1.0 + 0.2 * self.dim + 0.1 * np.cos(self.dim * np.pi / 3) * \
                     np.sin(self.dim * np.pi / 5)
        
        # Add chaotic noise component to increase landscape complexity
        noise = 0.05 * np.sum(np.sin(x_norm * np.pi * 7) * np.cos(x_norm * np.pi * 5))
        
        # Combine all terms with adaptive weights and chaotic modulation
        total = (0.35 * poly_term + 0.25 * trig_term + 0.2 * rbf_term + 0.15 * cross_term + noise) * \
                condition_factor * dim_scaling
        
        return total
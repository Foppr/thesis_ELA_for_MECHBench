import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees and adaptive coefficients
        poly_term = 0.0
        for i in range(self.dim):
            degree = 3 + (i % 3)  # Varying degrees from 3 to 5
            coeff = 1.0 + 0.4 * np.cos(i * np.pi / self.dim)
            poly_term += coeff * (x_norm[i] ** degree)
        
        # Trigonometric component with multiple frequencies and amplitudes
        trig_term = 0.0
        frequencies = [2, 3, 4, 5, 6]
        for i in range(self.dim):
            for j, freq in enumerate(frequencies):
                amp = 1.5 / (j + 1)
                phase = np.pi * i * (j + 2) / self.dim
                trig_term += amp * np.sin(freq * np.pi * x_norm[i] + phase) * \
                            np.cos(freq * np.pi * x_norm[i] + phase)
        
        # Radial basis function component with adaptive centers and widths
        rbf_term = 0.0
        num_centers = min(4, self.dim)
        for i in range(num_centers):
            center = np.cos(i * np.pi / num_centers) * 0.6
            width = 0.3 + 0.7 * np.sin(i * np.pi / num_centers)
            rbf_term += np.exp(-0.5 * ((x_norm[i % self.dim] - center) / width) ** 2)
        
        # Cross-dimensional coupling with adaptive strength based on dimension
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = 0.3 + 0.7 * np.cos((i + j) * np.pi / self.dim)
                cross_term += coupling_strength * np.sin(4 * np.pi * dist) * \
                             np.cos(3 * np.pi * dist) * (dist + 0.15)
        
        # Adaptive conditioning based on distance from origin and dimensionality
        r = np.sqrt(np.sum(x_norm**2))
        condition_factor = 1.0 + 3.0 * np.exp(-0.3 * r**2) * np.cos(5 * np.pi * r)
        
        # Dimensionality-dependent scaling
        dim_scaling = 1.0 + 0.15 * self.dim + 0.08 * np.sin(self.dim * np.pi / 3)
        
        # Combine all terms with adaptive weights
        total = (0.35 * poly_term + 0.35 * trig_term + 0.2 * rbf_term + 0.1 * cross_term) * \
                condition_factor * dim_scaling
        
        return total
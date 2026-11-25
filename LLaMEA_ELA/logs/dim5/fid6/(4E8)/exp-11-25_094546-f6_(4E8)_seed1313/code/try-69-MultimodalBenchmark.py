import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        theta = np.pi / 4
        self.rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with varying degrees
        poly_terms = np.sum((x_norm ** np.arange(1, self.dim + 1)) * np.random.uniform(0.5, 2.0, self.dim))
        
        # Radial basis function component with adaptive width
        rbfs = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i * np.pi / 5)
            rbfs += np.exp(-0.5 * ((x_norm - center) / width) ** 2)
        
        # Multi-scale harmonic modulation
        harmonics = 0.0
        for i in range(1, min(6, self.dim + 1)):
            harmonics += np.sin(i * np.pi * x_norm) * np.cos(i * np.pi * x_norm / 2)
            
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Rotation-invariant term
        rot_term = 0.0
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                if i + 1 < self.dim:
                    xi, yi = x_norm[i], x_norm[i+1]
                    rot_term += (xi**2 + yi**2) * np.sin(4 * np.arctan2(yi, xi))
        
        # Combine all components
        return dim_factor * (poly_terms + 0.5 * rbfs + 0.3 * harmonics + 0.2 * rot_term)
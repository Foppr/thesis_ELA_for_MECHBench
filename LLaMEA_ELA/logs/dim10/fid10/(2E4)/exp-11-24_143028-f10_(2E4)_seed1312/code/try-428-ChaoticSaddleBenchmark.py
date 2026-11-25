import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Elliptic basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, dim)
        self.elliptic_axes = np.random.uniform(1.0, 5.0, dim)
        # Chaotic saddle parameters
        self.saddle_points = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        # Adaptive noise injection
        self.noise_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.noise_frequencies = np.random.uniform(0.5, 2.0, dim)
        # Rotation matrices for each dimension
        self.rotation_matrices = []
        for _ in range(dim):
            angle = np.random.uniform(0, 2*np.pi)
            rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            self.rotation_matrices.append(rotation)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        fitness = 0.0
        
        for i in range(self.dim):
            # Elliptic basin term
            center = self.basin_centers[i]
            radius = self.basin_radii[i]
            axis = self.elliptic_axes[i]
            
            # Apply rotation if dimension > 1
            if self.dim > 1:
                rotated_x = np.zeros(self.dim)
                if i < len(self.rotation_matrices):
                    rotated_x[i] = x[i]
                    if i + 1 < self.dim:
                        rotated_x[i+1] = x[i+1]
                        # Simple 2D rotation
                        rot_matrix = self.rotation_matrices[i % len(self.rotation_matrices)]
                        rotated_coords = rot_matrix @ np.array([x[i], x[i+1]])
                        rotated_x[i] = rotated_coords[0]
                        rotated_x[i+1] = rotated_coords[1]
                else:
                    rotated_x = x
            else:
                rotated_x = x
            
            # Elliptic basin contribution (modified)
            basin_contribution = ((rotated_x[i] - center)**2) / (radius**2 + 0.1) + \
                                axis * np.sin(0.5 * (rotated_x[i] - center))**2
            
            # Chaotic saddle term with adaptive strength
            saddle_contribution = 0.0
            for j in range(3):
                saddle_point = self.saddle_points[i, j]
                strength = self.saddle_strengths[i]
                saddle_contribution += strength * np.exp(-((rotated_x[i] - saddle_point)**2) / (2 * 0.5**2))
            
            # Adaptive noise injection
            noise_injection = self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * rotated_x[i])
            
            # Combine terms with modified interaction
            fitness += basin_contribution + saddle_contribution + noise_injection
            
        # Normalize and add global scaling
        fitness = fitness / self.dim
        return fitness
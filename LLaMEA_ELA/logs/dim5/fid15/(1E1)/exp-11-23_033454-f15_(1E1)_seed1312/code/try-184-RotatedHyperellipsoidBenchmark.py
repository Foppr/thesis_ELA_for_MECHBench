import numpy as np

class RotatedHyperellipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute rotation matrices for each dimension
        self.rotation_matrices = []
        for i in range(dim):
            angle = np.pi * np.random.rand() / 4.0
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            if dim == 1:
                rot_mat = np.array([[1.0]])
            else:
                rot_mat = np.eye(dim)
                rot_mat[i % dim, i % dim] = cos_a
                rot_mat[(i+1) % dim, (i+1) % dim] = cos_a
                rot_mat[i % dim, (i+1) % dim] = -sin_a
                rot_mat[(i+1) % dim, i % dim] = sin_a
            self.rotation_matrices.append(rot_mat)
        
        # Adaptive condition numbers for each dimension
        self.condition_numbers = 10.0 + 90.0 * np.random.rand(dim)
        
        # Dynamic noise parameters
        self.noise_amplitude = 2.0 + 3.0 * np.random.rand()
        self.noise_frequency = 0.5 + 2.0 * np.random.rand()
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and compute hyperellipsoid terms
        result = 0.0
        for i in range(self.dim):
            # Rotate the input vector using precomputed rotation matrix
            rotated_x = x.copy()
            if self.dim > 1:
                rotated_x = self.rotation_matrices[i] @ x
            
            # Hyperellipsoid term with adaptive condition number
            term = np.sum((rotated_x[:i+1])**2 * self.condition_numbers[:i+1])
            result += term
        
        # Add dynamic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_amplitude * np.sin(self.noise_frequency * x[i] + i) * \
                     np.cos(self.noise_frequency * x[i] * 0.5 + i * 0.7)
        
        # Add penalty for distance from origin (to encourage convergence to global minimum)
        penalty = 0.1 * np.sum(x**2)
        
        return result + noise + penalty
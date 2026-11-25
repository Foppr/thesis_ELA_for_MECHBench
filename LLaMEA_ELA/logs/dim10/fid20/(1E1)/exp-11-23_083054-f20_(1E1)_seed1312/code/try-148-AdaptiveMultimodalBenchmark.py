import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive scaling factors
        self.scaling_factors = np.array([1.0 + 0.5 * np.sin(0.3 * i) for i in range(dim)])
        # Precompute rotation matrix for directional correlations
        angle = np.pi / 4.0
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        if dim > 2:
            self.rotation_matrix = np.eye(dim)
            for i in range(0, dim-1, 2):
                if i+1 < dim:
                    rot_block = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
                    self.rotation_matrix[i:i+2, i:i+2] = rot_block
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.2 * i)
            amp = 1.5 + 0.5 * np.cos(0.4 * i)
            f1 += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Polynomial penalty component with adaptive exponents
        f2 = 0.0
        for i in range(self.dim):
            exp = 2.0 + 2.0 * np.sin(0.3 * i)
            f2 += (x_norm[i] ** exp) * np.exp(-0.5 * x_norm[i]**2)
        
        # Spherical component with adaptive radii
        f3 = 0.0
        for i in range(self.dim):
            radius = 1.0 + 0.8 * np.cos(0.5 * i)
            f3 += (x_norm[i] / radius) ** 2
        
        # Cross-dimensional interaction with rotation
        f4 = 0.0
        rotated_x = self.rotation_matrix @ x_norm
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += rotated_x[i] * rotated_x[j] * np.sin(0.5 * (i + j))
        
        # Adaptive weighted combination
        weights = [0.25 + 0.05 * np.sin(0.4 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4
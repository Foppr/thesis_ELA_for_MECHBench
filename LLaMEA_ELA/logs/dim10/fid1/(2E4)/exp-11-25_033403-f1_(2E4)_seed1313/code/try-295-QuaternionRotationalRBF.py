import numpy as np

class QuaternionRotationalRBF:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis functions with varying widths and centers
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 10)
        # Initialize quaternion-inspired rotational components
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim//2 if dim % 2 == 0 else (dim//2 + 1))
        self.rotation_axes = np.random.randn(dim, dim//2 if dim % 2 == 0 else (dim//2 + 1))
        # Initialize dynamic noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(1.0, 3.0, dim)
        # Initialize saddle-point attraction parameters
        self.saddle_centers = np.random.uniform(-3.0, 3.0, (3, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, 3)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            dist_sq = np.sum((x - self.rbf_centers[i])**2)
            rbf_sum += self.rbf_weights[i] * np.exp(-0.5 * dist_sq / (self.rbf_widths[i]**2))
        
        # Apply quaternion-inspired rotational transformation
        rotated_x = x.copy()
        if self.dim >= 2:
            for i in range(0, self.dim - 1, 2):
                if i + 1 < self.dim:
                    angle = self.rotation_angles[i//2]
                    cos_a, sin_a = np.cos(angle), np.sin(angle)
                    # 2D rotation matrix
                    rot_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
                    xy = np.array([x[i], x[i+1]])
                    rotated_xy = rot_matrix @ xy
                    rotated_x[i], rotated_x[i+1] = rotated_xy[0], rotated_xy[1]
        
        # Add dynamic noise component
        noise = 0.0
        for j in range(self.dim):
            noise += self.noise_amplitudes[j] * np.sin(self.noise_frequencies[j] * x[j])
        
        # Add saddle-point attraction mechanisms
        saddle_attraction = 0.0
        for i in range(3):
            dist_sq = np.sum((x - self.saddle_centers[i])**2)
            saddle_attraction += self.saddle_strengths[i] / (1.0 + dist_sq)
        
        # Combine all components
        total = rbf_sum + 0.5 * noise + 0.3 * saddle_attraction
        
        return total
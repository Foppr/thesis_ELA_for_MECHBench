import numpy as np

class QuaternionRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function components
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 10)
        # Initialize quaternion-inspired rotational symmetries
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim//2 if dim % 2 == 0 else (dim-1)//2)
        self.rotation_axes = np.random.randn(dim, dim//2 if dim % 2 == 0 else (dim-1)//2)
        # Initialize adaptive noise parameters
        self.noise_magnitude = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequency = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Apply quaternion-inspired rotational symmetries
        if self.dim % 2 == 0:
            rotated_x = x.copy()
            for i in range(0, self.dim, 2):
                angle = self.rotation_angles[i//2]
                cos_a, sin_a = np.cos(angle), np.sin(angle)
                # 2D rotation matrix
                rot_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
                xy = np.array([x[i], x[i+1]])
                rotated_x[i:i+2] = rot_matrix @ xy
        else:
            rotated_x = x.copy()
            for i in range(0, self.dim-1, 2):
                angle = self.rotation_angles[i//2]
                cos_a, sin_a = np.cos(angle), np.sin(angle)
                rot_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
                xy = np.array([x[i], x[i+1]])
                rotated_x[i:i+2] = rot_matrix @ xy
            # Keep last dimension unchanged
        
        # Compute radial basis function potential
        rbf_potential = 0.0
        for i in range(10):
            dist_sq = np.sum((rotated_x - self.rbf_centers[i])**2)
            rbf_potential += self.rbf_weights[i] * np.exp(-0.5 * dist_sq / (self.rbf_widths[i]**2))
        
        # Add adaptive noise injection
        noise_terms = 0.0
        for j in range(self.dim):
            noise_terms += self.noise_magnitude[j] * np.sin(self.noise_frequency[j] * rotated_x[j])
        
        # Combine components with dynamic scaling
        total = 0.7 * rbf_potential + 0.3 * noise_terms
        
        return total
import numpy as np

class QuaternionRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quaternion rotation parameters
        self.quat_params = np.random.rand(dim, 4) * 2.0 - 1.0
        self.quat_params = self.quat_params / np.linalg.norm(self.quat_params, axis=1, keepdims=True)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = 0.5 + np.random.rand(dim) * 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-based rotation component
        rot_term = 0.0
        for i in range(self.dim):
            # Construct rotation matrix from quaternion
            q = self.quat_params[i]
            rot_matrix = np.array([
                [1 - 2*(q[2]**2 + q[3]**2), 2*(q[1]*q[2] - q[0]*q[3]), 2*(q[1]*q[3] + q[0]*q[2])],
                [2*(q[1]*q[2] + q[0]*q[3]), 1 - 2*(q[1]**2 + q[3]**2), 2*(q[2]*q[3] - q[0]*q[1])],
                [2*(q[1]*q[3] - q[0]*q[2]), 2*(q[2]*q[3] + q[0]*q[1]), 1 - 2*(q[1]**2 + q[2]**2)]
            ])
            
            # Apply rotation to x vector
            x_rot = np.dot(rot_matrix, x)
            
            # Add contribution from rotated coordinates
            rot_term += np.sum(x_rot**2) * (0.5 + 0.5 * np.sin(i * 0.7))
        
        # Radial basis function component
        rbf_term = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x - center
            rbf_term += np.exp(-0.5 * np.sum((diff / width)**2))
        
        # Cross-dimensional coupling with sine modulation
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            cross_term += np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) * \
                         np.exp(-0.1 * (x[k]**2 + x[i]**2)) * \
                         (1.0 + 0.3 * np.sin(i * 0.5))
        
        # Asymmetric polynomial component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**5 - 10*x[i]**3 + 25*x[i]) * (1.0 + 0.2 * np.cos(i * 0.4))
        
        # Combine all components with adaptive weights
        result = 0.2 * rot_term + 0.3 * rbf_term + 0.25 * cross_term + 0.25 * poly_term
        
        return result
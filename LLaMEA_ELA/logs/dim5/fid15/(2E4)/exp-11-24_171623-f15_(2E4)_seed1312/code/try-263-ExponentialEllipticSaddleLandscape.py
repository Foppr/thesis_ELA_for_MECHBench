import numpy as np

class ExponentialEllipticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.rbf_widths = 0.5 + 1.5 * np.random.rand(dim)
        # Elliptic contour parameters
        self.elliptic_axes = 1.0 + 2.0 * np.random.rand(dim)
        self.elliptic_angles = np.random.uniform(0, np.pi, dim)
        # Saddle-point inducing cross-terms
        self.saddle_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Adaptive scaling factors
        self.scaling_factors = 1.0 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x_norm - center
            rbf_val = np.exp(-np.sum(diff**2) / (2 * width**2))
            rbf_sum += rbf_val
        
        # Adaptive elliptic contour component
        ellip_sum = 0.0
        for i in range(self.dim):
            axis = self.elliptic_axes[i]
            angle = self.elliptic_angles[i]
            # Rotate coordinates
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            x_rot = x_norm[i] * cos_a + x_norm[(i+1) % self.dim] * sin_a
            y_rot = -x_norm[i] * sin_a + x_norm[(i+1) % self.dim] * cos_a
            ellip_val = (x_rot**2 / axis**2 + y_rot**2 / axis**2)
            ellip_sum += ellip_val
        
        # Saddle-point inducing cross-terms
        saddle_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = self.saddle_weights[i, j]
                    saddle_val = weight * x_norm[i] * x_norm[j] * (x_norm[i]**2 + x_norm[j]**2)
                    saddle_sum += saddle_val
        
        # Combined landscape with adaptive scaling
        result = 0.3 * rbf_sum + 0.4 * ellip_sum + 0.3 * saddle_sum
        
        # Adaptive conditioning and global penalty
        condition_factor = 1.0
        for i in range(self.dim):
            scale = self.scaling_factors[i]
            cond_val = 1.0 + 0.5 * np.abs(x_norm[i]) * scale
            condition_factor *= cond_val
            
        # Global penalty with quartic terms
        penalty = 0.1 * np.sum(x_norm**4)
        
        return result * condition_factor + penalty + 0.02 * np.sum(np.abs(x_norm)**7)
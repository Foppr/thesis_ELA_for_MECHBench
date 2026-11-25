import numpy as np

class NestedEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
        # Define nested elliptic structures with varying eccentricity
        self.elliptic_axes = np.random.uniform(1.0, 3.0, (dim, dim))
        self.elliptic_angles = np.random.uniform(0, np.pi, (dim, dim))
        
        # Adaptive conditioning factors per dimension
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Nested elliptic valley components with varying eccentricity
        for i in range(self.dim):
            # Elliptic quadratic form with adaptive axes and rotation
            ellipse_term = 0.0
            for j in range(self.dim):
                # Rotation matrix for elliptical structure
                cos_angle = np.cos(self.elliptic_angles[i, j])
                sin_angle = np.sin(self.elliptic_angles[i, j])
                
                # Rotated coordinates
                x_rot = x_norm[j] * cos_angle - x_norm[i] * sin_angle
                y_rot = x_norm[j] * sin_angle + x_norm[i] * cos_angle
                
                # Elliptical quadratic term with adaptive axis ratio
                ellipse_term += (x_rot / self.elliptic_axes[i, j])**2 + (y_rot / self.elliptic_axes[i, j])**2
            
            # Nested scaling with exponential decay
            f_val += np.exp(-0.5 * ellipse_term) * np.sin(2 * np.pi * x_norm[i])**2
        
        # Radial basis function interactions between dimensions
        rbf_sum = 0.0
        for i in range(10):
            rbf_term = 0.0
            for j in range(self.dim):
                diff = x_norm[j] - self.rbf_centers[j, i]
                rbf_term += diff**2
            rbf_sum += np.exp(-self.rbf_widths[i] * rbf_term)
        
        f_val += 0.5 * rbf_sum
        
        # Adaptive conditioning with piecewise linear transformation
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            if x_norm[i] < -0.3:
                f_val += 0.3 * cond_factor * (x_norm[i] + 0.3)**2
            elif x_norm[i] > 0.3:
                f_val += 0.3 * cond_factor * (x_norm[i] - 0.3)**2
            else:
                f_val += 0.1 * cond_factor * x_norm[i]**4
        
        # Multi-scale harmonic components with varying frequencies (modified)
        for scale in [0.3, 0.7, 1.5]:  # Changed scales
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 5 * np.pi * x_norm[i]) * np.cos(scale * 4 * np.pi * x_norm[i])  # Increased frequencies
            f_val += 0.15 * harmonic_sum**2  # Increased weight
        
        # Cross-dimensional coupling with exponential interaction (modified)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * np.sin(4 * np.pi * (x_norm[i] + x_norm[j]))  # Increased coupling strength and frequency
                f_val += 0.25 * coupling  # Increased weight
        
        # Add noise-like perturbations for increased complexity (modified)
        noise = 0.08 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))  # Increased frequencies and weight
        f_val += noise
        
        return f_val
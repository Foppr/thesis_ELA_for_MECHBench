import numpy as np

class PolynomialRBFQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        poly_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Use third-order Hermite polynomial terms with modified coefficients
            poly_component += (xi**3 - 3*xi) * (1 + 0.3 * np.sin(2*i))
        
        # Radial basis function with multiquadric kernels and varying centers
        rbf_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Varying shape parameters based on dimension index with different base
            shape_param = 0.3 + 0.2 * np.sin(i * np.pi / self.dim)
            # Center positions distributed in a spiral pattern with different scaling
            center_angle = i * np.pi / (self.dim + 1)
            center_x = np.cos(center_angle) * 0.4
            center_y = np.sin(center_angle) * 0.4
            rbf_component += np.sqrt((xi - center_x)**2 + (xi - center_y)**2 + shape_param**2)
        
        # Quaternion-based rotational symmetry component with altered frequency
        quat_component = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x_norm[i]
                yi = x_norm[i+1]
                # Create rotational invariance using quaternion-like terms with different frequency
                angle = np.arctan2(yi, xi)
                radius = np.sqrt(xi**2 + yi**2)
                quat_component += (radius * np.cos(4 * angle) + 
                                 radius**2 * np.sin(5 * angle)) * (1 + 0.15 * np.cos(i))
        
        # Cross-dimensional coupling with tensor products and trigonometric interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Tensor product interaction with varying weights - modified weights
                weight = (i + 2) * (j + 2)
                cross_coupling += weight * np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[j])
        
        # Asymmetric exponential decay with dimension-dependent parameters
        exp_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Exponential terms with varying decay rates - different base rates
            decay_rate = 0.6 + 0.4 * np.cos(i * np.pi / self.dim)
            exp_component += np.exp(-decay_rate * abs(xi)) * (1 + 0.2 * np.sin(3*i))
        
        # Multi-scale sinusoidal modulation with fractal-like behavior
        multi_scale = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequency components - different frequencies
            freqs = [3, 5, 9]
            scale_factor = 1.0 / (i + 2) if i > 0 else 1.0
            for f in freqs:
                multi_scale += np.sin(f * xi) * scale_factor
        
        # Combine all components with modified weights
        result = 1.2 * poly_component + 0.9 * rbf_component + 1.0 * quat_component + \
                0.7 * cross_coupling + 1.0 * exp_component + 0.8 * multi_scale
        
        # Add controlled noise for robustness - reduced noise level
        noise = np.random.normal(0, 0.002)
        
        return result + noise
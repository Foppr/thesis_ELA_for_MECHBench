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
            # Use third-order Hermite polynomial terms
            poly_component += (xi**3 - 3*xi) * (1 + 0.2 * np.sin(2*i))
        
        # Radial basis function with multiquadric kernels and varying centers
        rbf_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Varying shape parameters based on dimension index
            shape_param = 0.2 + 0.3 * np.sin(i * np.pi / self.dim)
            # Center positions distributed in a spiral pattern
            center_angle = i * np.pi / self.dim
            center_x = np.cos(center_angle) * 0.5
            center_y = np.sin(center_angle) * 0.5
            rbf_component += np.sqrt((xi - center_x)**2 + (xi - center_y)**2 + shape_param**2)
        
        # Quaternion-based rotational symmetry component
        quat_component = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x_norm[i]
                yi = x_norm[i+1]
                # Create rotational invariance using quaternion-like terms
                angle = np.arctan2(yi, xi)
                radius = np.sqrt(xi**2 + yi**2)
                quat_component += (radius * np.cos(3 * angle) + 
                                 radius**2 * np.sin(4 * angle)) * (1 + 0.1 * np.cos(i))
        
        # Cross-dimensional coupling with tensor products and trigonometric interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Tensor product interaction with varying weights (slightly modified)
                weight = (i + 1) * (j + 1) * 0.8
                cross_coupling += weight * np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[j])
        
        # Asymmetric exponential decay with dimension-dependent parameters
        exp_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Exponential terms with varying decay rates
            decay_rate = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)
            exp_component += np.exp(-decay_rate * abs(xi)) * (1 + 0.3 * np.sin(3*i))
        
        # Multi-scale sinusoidal modulation with fractal-like behavior
        multi_scale = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequency components
            freqs = [2, 4, 8]
            scale_factor = 1.0 / (i + 1) if i > 0 else 1.0
            for f in freqs:
                multi_scale += np.sin(f * xi) * scale_factor
        
        # Combine all components with adaptive weights (slightly modified)
        result = 1.0 * poly_component + 0.8 * rbf_component + 1.2 * quat_component + \
                0.5 * cross_coupling + 1.1 * exp_component + 0.9 * multi_scale
        
        # Add controlled noise for robustness (slightly reduced)
        noise = np.random.normal(0, 0.003)
        
        return result + noise
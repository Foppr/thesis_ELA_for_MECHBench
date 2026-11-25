import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for stability
        self.constants = {
            'rbf_width': 0.5,
            'phase_freq': 2.0 * np.pi,
            'chaos_factor': 3.14159,
            'polynomial_degree': 4
        }
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Polynomial chaos component with dynamic exponents
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic polynomial with varying degree based on dimension and position
            poly_term = np.sum([(xi**d) * np.sin(d * self.constants['chaos_factor'] * xi) 
                               for d in range(2, self.constants['polynomial_degree'] + 1)])
            
            # Radial basis function component
            rbf_sum = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = abs(xi - x_norm[j])
                    rbf_value = np.exp(-0.5 * (distance / self.constants['rbf_width'])**2)
                    rbf_sum += rbf_value * np.cos(self.constants['phase_freq'] * (xi + x_norm[j]))
            
            # Phase interference term
            phase_interference = np.sin(self.constants['phase_freq'] * xi) * np.cos(self.constants['phase_freq'] * xi**2)
            
            # Combined chaotic contribution
            chaotic_contribution = poly_term + rbf_sum + phase_interference
            
            # Apply dimension-specific scaling
            dim_scale = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(i * 0.5)
            
            result += dim_scale * chaotic_contribution**2
        
        # Global coupling term with multi-scale interference
        global_coupling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale phase modulation
            scale1 = np.sin(2 * self.constants['phase_freq'] * xi)
            scale2 = np.cos(3 * self.constants['phase_freq'] * xi**2)
            scale3 = np.sin(5 * self.constants['phase_freq'] * xi**0.5)
            
            global_coupling += (scale1 + scale2 + scale3) * np.exp(-0.1 * abs(xi))
        
        # Global scaling factor with fractal-like behavior
        global_scale = 1.0 + 0.4 * np.sin(self.constants['chaos_factor'] * np.log(self.dim + 1)) * \
                      np.cos(self.constants['chaos_factor'] * np.sqrt(self.dim + 1))
        
        # Final computation
        return global_scale * (result / self.dim + 0.1 * global_coupling)
import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chebyshev_coeffs = np.random.randn(dim, 3)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.tent_map_r = 3.9 + 0.1 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Tent map chaotic component
        tent_value = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            for _ in range(10):
                if xi < 0.5:
                    xi = self.tent_map_r * xi
                else:
                    xi = self.tent_map_r * (1 - xi)
            tent_value += xi
            
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x_norm - center
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * width**2))
            
        # Chebyshev polynomial component for higher-order interactions
        cheb_poly = 0.0
        for i in range(self.dim):
            for j in range(3):
                Tn = np.cos(j * np.arccos(np.clip(x_norm[i], -1, 1)))
                cheb_poly += self.chebyshev_coeffs[i, j] * Tn
                
        # Directional coupling with gradient-based terms
        grad_coupling = 0.0
        for i in range(self.dim):
            grad_coupling += (x_norm[i]**3 + 0.5 * x_norm[i] * x_norm[(i+1) % self.dim])
            
        # Combine all components with varying weights
        return 0.4 * tent_value + 0.3 * rbf_sum + 0.2 * cheb_poly + 0.1 * grad_coupling + 1.0
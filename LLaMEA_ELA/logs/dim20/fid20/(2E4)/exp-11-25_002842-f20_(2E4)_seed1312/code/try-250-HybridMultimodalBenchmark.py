import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 6))
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 20))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, 20))
        # Saddle-node bifurcation parameters
        self.bifurcation_params = np.random.uniform(-2.0, 2.0, dim)
        # Cross-dimensional coupling weights
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Noise parameters
        self.noise_levels = np.random.uniform(0.01, 0.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(6):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            result += poly_term
            
        # Radial basis function network component
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_inner_sum = 0.0
            for j in range(20):
                rbf_inner_sum += np.exp(-((x[i] - self.rbf_centers[i, j]) ** 2) / (2 * (self.rbf_widths[i, j] ** 2)))
            rbf_sum += rbf_inner_sum
            
        # Saddle-node bifurcation dynamics
        bifurcation_sum = 0.0
        for i in range(self.dim):
            # Bifurcation term with cubic nonlinearity
            bifurcation_term = self.bifurcation_params[i] * (x[i] ** 3 - x[i])
            # Add noise to bifurcation
            noise = np.random.normal(0, self.noise_levels[i])
            bifurcation_sum += bifurcation_term + noise
            
        # Cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_weights[i, j] * np.sin(x[i] - x[j])
                    
        # Combine all components with different weights
        total = 0.4 * result + 0.3 * rbf_sum + 0.2 * bifurcation_sum + 0.1 * coupling_sum
        
        # Add a global scaling factor based on the norm of x
        norm_x = np.linalg.norm(x)
        total *= (1.0 + 0.1 * np.sin(norm_x))
        
        return total
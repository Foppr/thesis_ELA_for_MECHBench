import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths with hyperbolic tangent modulation
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 15))
        self.rbf_widths = np.random.uniform(0.3, 1.8, (15,))
        # Initialize polynomial chaos expansion coefficients with quartic terms
        self.pce_coeffs = np.random.normal(0.0, 1.0, (dim, 7))
        # Initialize hyperbolic tangent modulation parameters
        self.tanh_freq = np.random.uniform(2.0, 5.0, dim)
        self.tanh_amp = np.random.uniform(1.0, 2.5, dim)
        # Initialize coupling matrix for dimension interactions with quartic terms
        self.coupling_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        # Add multi-modal RBF component
        self.multi_rbf_centers = np.random.uniform(-4.5, 4.5, (dim, 8))
        self.multi_rbf_widths = np.random.uniform(0.4, 2.2, (8,))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multi-modal enhancement
        rbf_sum = 0
        for i in range(15):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[j, i]
                rbf_term += diff**2
            rbf_sum += np.exp(-0.5 * rbf_term / (self.rbf_widths[i]**2))
        
        # Multi-modal RBF component
        multi_rbf_sum = 0
        for i in range(8):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.multi_rbf_centers[j, i]
                rbf_term += diff**2
            multi_rbf_sum += np.exp(-0.5 * rbf_term / (self.multi_rbf_widths[i]**2))
        
        # Polynomial chaos expansion component with quartic terms
        pce_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            pce_term = (self.pce_coeffs[i, 0] + 
                       self.pce_coeffs[i, 1] * x_i + 
                       self.pce_coeffs[i, 2] * x_i**2 + 
                       self.pce_coeffs[i, 3] * x_i**3 +
                       self.pce_coeffs[i, 4] * x_i**4 +
                       self.pce_coeffs[i, 5] * x_i**5 +
                       self.pce_coeffs[i, 6] * x_i**6)
            pce_sum += pce_term
        
        # Hyperbolic tangent modulation component
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += self.tanh_amp[i] * np.tanh(self.tanh_freq[i] * x[i])
        
        # Cross-dimension coupling with quartic interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * x[i]**4 * x[j]
        
        # Combine all components with different weights
        result = (1.2 * rbf_sum + 
                 0.9 * pce_sum + 
                 0.7 * tanh_mod + 
                 0.5 * coupling +
                 0.3 * multi_rbf_sum)
        
        return result
import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (10,))
        # Initialize polynomial chaos expansion coefficients
        self.pce_coeffs = np.random.normal(0.0, 1.0, (dim, 5))
        # Initialize chaotic modulation parameters
        self.chaos_freq = np.random.uniform(1.0, 3.0, dim)
        self.chaos_amp = np.random.uniform(0.5, 1.5, dim)
        # Initialize coupling matrix for dimension interactions with altered weights
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(10):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[j, i]
                rbf_term += diff**2
            rbf_sum += np.exp(-0.5 * rbf_term / (self.rbf_widths[i]**2))
        
        # Polynomial chaos expansion component with quadratic terms
        pce_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            pce_term = (self.pce_coeffs[i, 0] + 
                       self.pce_coeffs[i, 1] * x_i + 
                       self.pce_coeffs[i, 2] * x_i**2)
            pce_sum += pce_term
        
        # Chaotic modulation component
        chaos_mod = 0
        for i in range(self.dim):
            chaos_mod += self.chaos_amp[i] * np.sin(self.chaos_freq[i] * x[i]) * np.cos(self.chaos_freq[i] * x[i])
        
        # Cross-dimension coupling with quadratic interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * x[i]**2 * x[j]
        
        # Combine all components with different weights
        result = (1.0 * rbf_sum + 
                 0.8 * pce_sum + 
                 0.6 * chaos_mod + 
                 0.4 * coupling)
        
        return result
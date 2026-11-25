import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (10,))
        # Initialize polynomial chaos expansion coefficients
        self.pce_coeffs = np.random.normal(0.0, 1.0, (dim, 5))
        # Initialize gradient modulation parameters
        self.grad_modulation = np.random.uniform(0.5, 2.0, dim)
        # Initialize coupling matrix for dimension interactions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        # Add logarithmic barrier terms for enhanced multimodality
        self.barrier_centers = np.random.uniform(-4.0, 4.0, dim)
        self.barrier_strength = np.random.uniform(1.0, 3.0, dim)
        
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
        
        # Polynomial chaos expansion component
        pce_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            pce_term = (self.pce_coeffs[i, 0] + 
                       self.pce_coeffs[i, 1] * x_i + 
                       self.pce_coeffs[i, 2] * x_i**2 + 
                       self.pce_coeffs[i, 3] * x_i**3 + 
                       self.pce_coeffs[i, 4] * x_i**4)
            pce_sum += pce_term
        
        # Gradient modulation component
        grad_mod = 0
        for i in range(self.dim):
            grad_mod += self.grad_modulation[i] * np.sin(x[i])
        
        # Cross-dimension coupling with polynomial interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Add logarithmic barrier terms to increase multimodality
        barrier = 0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.barrier_centers[i])
            if dist < 0.1:
                barrier += self.barrier_strength[i] * (1.0 / (dist + 1e-8))
            else:
                barrier += self.barrier_strength[i] * np.log(dist + 1.0)
        
        # Combine all components with different weights
        result = (1.0 * rbf_sum + 
                 0.8 * pce_sum + 
                 0.6 * grad_mod + 
                 0.4 * coupling + 
                 0.3 * barrier)
        
        return result
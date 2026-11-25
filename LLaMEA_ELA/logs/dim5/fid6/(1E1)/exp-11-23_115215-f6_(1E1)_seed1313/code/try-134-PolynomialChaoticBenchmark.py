import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients and radial centers
        self.poly_coeffs = np.random.randn(dim, 4)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        self.coupling_weights = np.random.randn(dim, dim) * 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with mixed terms
        f_val = 0.0
        for i in range(self.dim):
            poly_term = np.sum(self.poly_coeffs[i] * 
                              np.array([1, x[i], x[i]**2, x[i]**3]))
            f_val += 0.5 * poly_term**2
        
        # Radial basis functions with multi-dimensional centers
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(3):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
            f_val += 0.3 * rbf_sum
        
        # Cross-dimensional coupling with varying strength
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x[i] * x[j])
                    f_val += 0.1 * coupling
        
        # Asymmetric polynomial interactions with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                asym_term = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * 0.5)
                f_val += 0.2 * asym_term
        
        # Multi-scale oscillatory components
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * 0.7)
            osc_term = scale_factor * np.sin(x[i] * 3.0) * np.cos(x[i] * 2.0)
            f_val += 0.15 * osc_term
        
        # Global conditioning term with exponential decay
        global_cond = np.exp(-0.1 * np.sum(np.abs(x)))
        f_val *= (1.0 + 0.3 * global_cond)
        
        # Add noise-like perturbations
        noise = np.sum(np.sin(x * np.pi) * np.cos(x * np.pi * 0.5))
        f_val += 0.05 * noise
        
        return f_val
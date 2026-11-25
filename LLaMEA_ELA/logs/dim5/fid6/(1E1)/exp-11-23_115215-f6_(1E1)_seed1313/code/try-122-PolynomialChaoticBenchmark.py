import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients and radial centers
        self.poly_coeffs = np.random.normal(0, 1, (dim, 4))
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        self.coupling_strengths = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial chaos expansion
        f_val = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(4):
                poly_term += self.poly_coeffs[i, j] * (x[i] ** j)
            f_val += poly_term
        
        # Radial basis functions with multi-scale widths and centers
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(3):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            f_val += 0.5 * rbf_sum
        
        # Dynamic coupling terms with varying strengths
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                coupling += self.coupling_strengths[i] * np.exp(-dist) * np.sin(x[i] * x[j])
            f_val += coupling
        
        # Multi-scale harmonic components
        for i in range(self.dim):
            f_val += 0.3 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + \
                     0.2 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + \
                     0.1 * np.sin(11.0 * x[i])
        
        # Asymmetric polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_interaction = (x[i]**2 + x[j]**3) * np.exp(-0.1 * np.abs(x[i] - x[j]))
                f_val += 0.15 * asym_interaction
        
        # Global conditioning with exponential scaling
        global_condition = np.exp(0.05 * np.sum(np.abs(x)))
        f_val *= global_condition
        
        # Add noise term with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2))
        f_val += noise
        
        return f_val
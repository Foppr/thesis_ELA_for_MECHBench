import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))  # 4th degree polynomials
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, dim))
        # Interference pattern parameters
        self.interference_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        self.interference_frequencies = np.random.randint(1, 8, (dim, dim))
        # Conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(4):
                poly_term += self.poly_coeffs[i][d] * (xi ** d)
            poly_sum += poly_term
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                width = self.rbf_widths[i][j]
                rbf_term += np.exp(-0.5 * ((xi - center) / width) ** 2)
            rbf_sum += rbf_term
        
        # Interference pattern component
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    amplitude = self.interference_amplitudes[i][j]
                    frequency = self.interference_frequencies[i][j]
                    interference_term += amplitude * np.sin(frequency * xi) * np.cos(frequency * x[j])
            interference_sum += interference_term
        
        # Combine all components with conditioning
        result = (0.5 * poly_sum + 
                 1.2 * rbf_sum + 
                 0.7 * interference_sum) * np.prod(self.conditioning_factors)
        
        return result
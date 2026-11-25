import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion parameters
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(0.1, 2.0, dim)
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, dim))
        self.rbf_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Cross-dimensional interference patterns
        self.interference_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        self.interference_frequencies = np.random.randint(2, 8, (dim, dim))
        self.interference_phase_shifts = np.random.uniform(0, 2*np.pi, (dim, dim))
        # Conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = self.poly_coefficients[i] * (xi ** self.poly_degrees[i])
            poly_sum += poly_term
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                width = self.rbf_widths[i][j]
                weight = self.rbf_weights[i][j]
                rbf_term = weight * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
                rbf_sum += rbf_term
        
        # Cross-dimensional interference component
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    amplitude = self.interference_amplitudes[i][j]
                    frequency = self.interference_frequencies[i][j]
                    phase = self.interference_phase_shifts[i][j]
                    interference_term += amplitude * np.sin(frequency * xi + phase) * x[j]
            interference_sum += interference_term
        
        # Conditioning component
        conditioning_sum = 0
        for i in range(self.dim):
            conditioning_sum += self.conditioning_factors[i] * (x[i] ** 2)
        
        # Combine all components with dynamic scaling
        result = (0.3 * poly_sum + 
                 0.4 * rbf_sum + 
                 0.5 * interference_sum + 
                 0.2 * conditioning_sum)
        
        return result
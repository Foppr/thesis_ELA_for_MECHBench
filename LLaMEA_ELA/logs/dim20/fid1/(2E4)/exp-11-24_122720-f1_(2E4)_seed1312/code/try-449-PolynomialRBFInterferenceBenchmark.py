import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion parameters with enhanced non-linearity
        self.poly_degrees = np.random.randint(4, 12, dim)
        self.poly_coefficients = np.random.uniform(0.5, 5.0, dim)
        self.poly_exponents = np.random.uniform(0.3, 6.0, dim)
        # Radial basis function parameters with increased diversity
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.2, 3.5, (dim, dim))
        self.rbf_weights = np.random.uniform(-4.0, 4.0, (dim, dim))
        # Cross-dimensional interference patterns with chaotic coupling
        self.interference_amplitudes = np.random.uniform(0.5, 6.0, (dim, dim))
        self.interference_frequencies = np.random.randint(2, 10, (dim, dim))
        self.interference_phase_shifts = np.random.uniform(0, 3*np.pi, (dim, dim))
        # Enhanced dynamic conditioning factors
        self.conditioning_factors = np.random.uniform(0.02, 7.0, dim)
        # Additional chaotic sine-wave modulation component
        self.sine_amplitudes = np.random.uniform(0.2, 2.0, dim)
        self.sine_frequencies = np.random.randint(4, 15, dim)
        self.sine_shifts = np.random.uniform(-1.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with enhanced non-linearity
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = self.poly_coefficients[i] * (xi ** self.poly_degrees[i]) * np.exp(-self.poly_exponents[i] * abs(xi))
            poly_sum += poly_term
        
        # Radial basis function component with increased complexity
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                distance = abs(xi - self.rbf_centers[i][j])
                rbf_term += self.rbf_weights[i][j] * np.exp(-0.5 * (distance / self.rbf_widths[i][j]) ** 2)
            rbf_sum += rbf_term
        
        # Cross-dimensional interference component with chaotic coupling
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    interference_term += (self.interference_amplitudes[i][j] * 
                                       np.sin(self.interference_frequencies[i][j] * xi + self.interference_phase_shifts[i][j]) *
                                       np.cos(self.interference_frequencies[i][j] * x[j] + self.interference_phase_shifts[i][j]))
            interference_sum += interference_term
        
        # Additional chaotic sine-wave modulation component
        sine_sum = 0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x[i] + self.sine_shifts[i])
        
        # Combine all components with enhanced dynamic conditioning
        result = (0.8 * poly_sum + 
                 1.5 * rbf_sum + 
                 1.6 * interference_sum + 
                 0.7 * sine_sum) * self.conditioning_factors[np.random.randint(0, self.dim)]
        
        return result
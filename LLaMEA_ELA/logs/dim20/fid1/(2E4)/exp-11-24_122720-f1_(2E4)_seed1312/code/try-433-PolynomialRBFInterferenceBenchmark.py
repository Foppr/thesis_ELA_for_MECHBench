import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))  # 5th degree polynomials
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, (dim, dim))
        # Interference pattern parameters
        self.interference_amplitudes = np.random.uniform(0.3, 2.5, (dim, dim))
        self.interference_frequencies = np.random.randint(2, 10, (dim, dim))
        # Conditioning factors
        self.conditioning_factors = np.random.uniform(0.5, 8.0, dim)
        # Additional noise component for increased complexity
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component (5th degree)
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(5):
                poly_term += self.poly_coeffs[i][d] * (xi ** d)
            poly_sum += poly_term
        
        # Radial basis function component with modified kernel
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                width = self.rbf_widths[i][j]
                # Modified RBF with different scaling
                rbf_term += np.exp(-((xi - center) ** 2) / (2 * width ** 2))
            rbf_sum += rbf_term
        
        # Interference pattern component with enhanced coupling
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    amplitude = self.interference_amplitudes[i][j]
                    frequency = self.interference_frequencies[i][j]
                    # Enhanced interference with product of trigonometric functions
                    interference_term += amplitude * np.sin(frequency * xi) * np.cos(frequency * x[j])
            interference_sum += interference_term
        
        # Add noise component for increased complexity
        noise_sum = 0
        for i in range(self.dim):
            noise_sum += self.noise_amplitude[i] * np.sin(x[i] * (i + 1))
        
        # Combine all components with conditioning and normalize
        result = (0.6 * poly_sum + 
                 1.0 * rbf_sum + 
                 0.8 * interference_sum + 
                 0.2 * noise_sum) * np.prod(self.conditioning_factors)
        
        return result
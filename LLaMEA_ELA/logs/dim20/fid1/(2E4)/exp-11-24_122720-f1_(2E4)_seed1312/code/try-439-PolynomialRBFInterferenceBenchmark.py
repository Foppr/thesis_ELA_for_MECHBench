import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients (higher order terms)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 6))  # 5th degree polynomials
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, dim))
        # Interference pattern parameters
        self.interference_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        self.interference_frequencies = np.random.randint(1, 8, (dim, dim))
        # Conditioning factors with more variation
        self.conditioning_factors = np.random.uniform(0.01, 20.0, dim)
        # Additional cosine modulation for increased complexity
        self.cosine_amplitudes = np.random.uniform(0.1, 0.8, (dim, dim))
        self.cosine_frequencies = np.random.randint(2, 8, (dim, dim))
        # Cross-dimensional coupling strength
        self.coupling_strength = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with higher order terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(6):
                poly_term += self.poly_coeffs[i][d] * (xi ** d)
            poly_sum += poly_term * self.coupling_strength[i]
        
        # Radial basis function component with adaptive weights
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                width = self.rbf_widths[i][j]
                rbf_term += np.exp(-0.5 * ((xi - center) / width) ** 2)
            rbf_sum += rbf_term * (1.0 + 0.1 * np.sin(i))  # Adaptive weighting
        
        # Interference pattern component with enhanced nonlinearity
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    amplitude = self.interference_amplitudes[i][j]
                    frequency = self.interference_frequencies[i][j]
                    # Enhanced interaction with nonlinear terms
                    interaction = amplitude * np.sin(frequency * xi) * np.cos(frequency * x[j])
                    interaction += amplitude * np.cos(frequency * xi) * np.sin(frequency * x[j])
                    # Add cosine modulation
                    cos_amplitude = self.cosine_amplitudes[i][j]
                    cos_frequency = self.cosine_frequencies[i][j]
                    interaction += cos_amplitude * np.cos(cos_frequency * xi) * np.cos(cos_frequency * x[j])
                    interference_term += interaction
            interference_sum += interference_term
        
        # Combine all components with improved conditioning
        result = (0.3 * poly_sum + 
                 1.5 * rbf_sum + 
                 0.8 * interference_sum) * np.prod(self.conditioning_factors)
        
        return result
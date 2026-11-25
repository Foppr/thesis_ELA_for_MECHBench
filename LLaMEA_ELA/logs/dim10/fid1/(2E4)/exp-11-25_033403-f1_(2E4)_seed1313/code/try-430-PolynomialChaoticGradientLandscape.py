import numpy as np

class PolynomialChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial coefficients for each dimension
        self.poly_degrees = np.random.randint(3, 7, dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 4))
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize gradient modulation factors
        self.grad_modulation = np.random.uniform(0.5, 2.0, dim)
        # Initialize dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.1, 1.0, dim)
        # Initialize coupling weights between dimensions
        self.coupling_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Add fractional Brownian motion parameters
        self.hurst_exponent = np.random.uniform(0.1, 0.9, dim)
        self.fbm_scale = np.random.uniform(0.01, 0.1, dim)
        # Add noise parameters for increased complexity
        self.noise_amplitude = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial components
        poly_terms = np.zeros(self.dim)
        for j in range(self.dim):
            power = self.poly_degrees[j]
            for i in range(4):
                poly_terms[j] += self.poly_coeffs[j, i] * (x[j] ** (power - i))
        
        # Compute chaotic logistic map components
        logistic_terms = np.zeros(self.dim)
        for j in range(self.dim):
            # Update logistic map
            self.logistic_x[j] = self.logistic_r[j] * self.logistic_x[j] * (1.0 - self.logistic_x[j])
            logistic_terms[j] = self.logistic_x[j]
        
        # Compute gradient modulation terms
        grad_terms = np.zeros(self.dim)
        for j in range(self.dim):
            grad_terms[j] = self.grad_modulation[j] * np.sin(x[j]) * np.cos(x[j])
        
        # Compute dynamic scaling terms
        scale_terms = np.zeros(self.dim)
        for j in range(self.dim):
            scale_terms[j] = self.scaling_factors[j] * (x[j]**2 + 1.0)
        
        # Compute cross-dimensional coupling terms
        coupling_terms = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms[i] += self.coupling_weights[i, j] * x[j]
        
        # Add fractional Brownian motion component
        fbm_terms = np.zeros(self.dim)
        for j in range(self.dim):
            # Simplified fractional Brownian motion approximation
            fbm_terms[j] = self.fbm_scale[j] * np.sin(x[j] * (j + 1) * 0.5) * (1.0 + self.hurst_exponent[j])
        
        # Add noise component
        noise_terms = np.random.normal(0, 1, self.dim) * self.noise_amplitude
        
        # Combine all components with appropriate weights
        total = 0.0
        for j in range(self.dim):
            total += (poly_terms[j] * logistic_terms[j] + 
                     grad_terms[j] * scale_terms[j] + 
                     coupling_terms[j] + 
                     fbm_terms[j] + 
                     noise_terms[j])
        
        return total
import numpy as np

class PolynomialChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial terms with varying degrees and coefficients
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize gradient modulation factors
        self.grad_modulation = np.random.uniform(0.5, 2.0, dim)
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 1.0, dim)
        # Initialize cross-dimensional coupling matrix with stronger interactions
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Initialize chaotic phase shifts
        self.chaotic_phase = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial components
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
            poly_terms += poly_term
        
        # Compute chaotic logistic map components
        logistic_terms = 0.0
        for j in range(self.dim):
            self.logistic_x[j] = self.logistic_r[j] * self.logistic_x[j] * (1 - self.logistic_x[j])
            logistic_terms += self.logistic_x[j] * np.sin(x[j] + self.chaotic_phase[j])
        
        # Compute gradient modulation terms
        grad_terms = 0.0
        for j in range(self.dim):
            grad_term = self.grad_modulation[j] * np.cos(x[j]) * (1.0 + 0.3 * np.sin(2.0 * x[j]))
            grad_terms += grad_term
        
        # Compute adaptive conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_factors[j] * (x[j]**4) * np.exp(-0.1 * abs(x[j]))
        
        # Compute cross-dimensional coupling terms with higher coupling strength
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j] * np.cos(0.5 * (x[i] + x[j]))
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * logistic_terms + 0.6 * grad_terms + 0.4 * cond_terms + 0.3 * coupling_terms
        
        return total
import numpy as np

class PolynomialChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial terms with varying degrees and coefficients
        self.poly_degrees = np.random.randint(2, 8, dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.6, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize gradient modulation factors
        self.grad_modulation = np.random.uniform(0.3, 2.5, dim)
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.05, 1.5, dim)
        # Initialize cross-dimensional coupling matrix with stronger interactions
        self.coupling_matrix = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Initialize chaotic phase shifts
        self.chaotic_phase = np.random.uniform(0, 2*np.pi, dim)
        # Initialize hybrid coupling coefficients
        self.hybrid_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize nonlinear modulation parameters
        self.nonlinear_mod = np.random.uniform(0.1, 1.0, dim)
        # Add additional complexity with sine-cosine coupling and exponential decay
        self.sine_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.exp_decay = np.random.uniform(0.01, 0.2, dim)
        
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
        
        # Compute hybrid coupling terms
        hybrid_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    hybrid_terms += self.hybrid_coupling[i, j] * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Compute nonlinear modulation terms
        nonlinear_terms = 0.0
        for j in range(self.dim):
            nonlinear_terms += self.nonlinear_mod[j] * np.sin(3.0 * x[j]) * np.exp(-0.01 * x[j]**2)
        
        # Add sine-cosine coupling and exponential decay terms for additional complexity
        sc_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    sc_coupling += self.sine_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        exp_decay_terms = 0.0
        for j in range(self.dim):
            exp_decay_terms += self.exp_decay[j] * np.exp(-0.5 * x[j]**2)
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * logistic_terms + 0.6 * grad_terms + 0.4 * cond_terms + 0.3 * coupling_terms + 0.2 * hybrid_terms + 0.1 * nonlinear_terms + 0.15 * sc_coupling + 0.05 * exp_decay_terms
        
        return total
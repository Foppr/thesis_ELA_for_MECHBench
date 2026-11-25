import numpy as np

class PolynomialChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial terms with varying degrees and coefficients
        self.poly_degrees = np.random.randint(2, 10, dim)
        self.poly_coeffs = np.random.uniform(-4.0, 4.0, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize gradient modulation factors
        self.grad_modulation = np.random.uniform(0.2, 3.0, dim)
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.02, 2.0, dim)
        # Initialize cross-dimensional coupling matrix with stronger interactions
        self.coupling_matrix = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Initialize chaotic phase shifts
        self.chaotic_phase = np.random.uniform(0, 2*np.pi, dim)
        # Initialize hybrid coupling coefficients
        self.hybrid_coupling = np.random.uniform(-0.6, 0.6, (dim, dim))
        # Initialize nonlinear modulation parameters
        self.nonlinear_mod = np.random.uniform(0.05, 1.2, dim)
        # Add additional complexity with hyperbolic tangent smoothing and resonance
        self.tanh_smoothing = np.random.uniform(0.1, 0.5, dim)
        self.resonance_freq = np.random.uniform(0.5, 2.0, (dim, dim))
        # Add adaptive noise injection
        self.noise_amplitude = np.random.uniform(0.01, 0.1, dim)
        self.noise_frequency = np.random.uniform(1.0, 5.0, dim)
        
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
        
        # Add hyperbolic tangent smoothing and resonance terms for additional complexity
        tanh_terms = 0.0
        for j in range(self.dim):
            tanh_terms += self.tanh_smoothing[j] * np.tanh(2.0 * x[j]) * np.exp(-0.05 * x[j]**2)
        
        resonance_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    resonance_terms += self.resonance_freq[i, j] * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add adaptive noise injection
        noise_terms = 0.0
        for j in range(self.dim):
            noise_terms += self.noise_amplitude[j] * np.sin(self.noise_frequency[j] * x[j]) * np.exp(-0.02 * x[j]**2)
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * logistic_terms + 0.6 * grad_terms + 0.4 * cond_terms + 0.3 * coupling_terms + 0.2 * hybrid_terms + 0.1 * nonlinear_terms + 0.15 * tanh_terms + 0.1 * resonance_terms + 0.05 * noise_terms
        
        return total
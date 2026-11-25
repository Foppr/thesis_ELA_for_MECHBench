import numpy as np

class PolynomialChaoticHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial coefficients with random values
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (4, dim))
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        # Initialize harmonic coupling weights
        self.harmonic_weights = np.random.uniform(0.5, 2.0, dim)
        # Initialize cross-dimensional interaction matrix
        self.interaction_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Initialize chaotic phase shifts
        self.chaotic_phase = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = 0.0
            for i in range(4):
                poly_term += self.poly_coeffs[i, j] * (x[j] ** (i + 1))
            poly_terms += poly_term
        
        # Compute chaotic logistic map components
        chaotic_terms = 0.0
        for j in range(self.dim):
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            x_scaled = (x[j] + 5.0) / 10.0  # Scale to [0, 1]
            chaotic_val = self.logistic_r[j] * x_scaled * (1.0 - x_scaled)
            chaotic_terms += chaotic_val * np.sin(self.chaotic_phase[j])
        
        # Compute harmonic coupling terms
        harmonic_terms = 0.0
        for j in range(self.dim):
            harmonic_term = 0.0
            for k in range(self.dim):
                if j != k:
                    harmonic_term += self.interaction_matrix[j, k] * np.sin(x[j] + x[k])
            harmonic_terms += harmonic_term * self.harmonic_weights[j]
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * chaotic_terms + 0.4 * harmonic_terms
        
        return total
import numpy as np

class PolynomialChaoticConditionalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial exponents and coefficients
        self.poly_exponents = np.random.uniform(2.0, 6.0, dim)
        self.poly_coeffs = np.random.uniform(0.5, 2.5, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize harmonic coupling strengths
        self.harmonic_couplings = np.random.uniform(0.5, 2.0, (dim, dim))
        # Initialize dynamic conditioning factors
        self.conditioning_weights = np.random.uniform(0.1, 0.8, dim)
        # Initialize frequency modulation parameters
        self.freq_modulation = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += self.poly_coeffs[j] * (x[j] ** self.poly_exponents[j])
        
        # Compute chaotic logistic map components
        logistic_terms = 0.0
        for j in range(self.dim):
            # Update logistic map
            self.logistic_x[j] = self.logistic_r[j] * self.logistic_x[j] * (1.0 - self.logistic_x[j])
            logistic_terms += self.logistic_x[j] * np.sin(x[j])
        
        # Compute harmonic coupling terms
        harmonic_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    harmonic_terms += self.harmonic_couplings[i, j] * np.sin(x[i] + x[j])
        
        # Compute dynamic conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_weights[j] * (x[j]**2) * (1.0 + 0.3 * np.cos(2.0 * x[j]))
        
        # Compute frequency modulation effects
        freq_mod_terms = 0.0
        for j in range(self.dim):
            freq_mod_terms += self.freq_modulation[j] * np.sin(x[j] * (1.0 + 0.2 * np.sin(3.0 * x[j])))
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * logistic_terms + 0.4 * harmonic_terms + 0.3 * cond_terms + 0.2 * freq_mod_terms
        
        return total
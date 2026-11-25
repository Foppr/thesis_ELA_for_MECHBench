import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients with varying degrees and weights
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 6))
        # Radial basis function centers with clustered and dispersed distributions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 20))
        # RBF widths with exponential scaling and chaotic variation
        self.rbf_widths = np.random.uniform(0.5, 3.0, 20) ** np.random.uniform(1.2, 2.5, 20)
        # Dynamic dimensionality scaling factors with periodic modulation
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        # Chaotic coupling coefficients between dimensions with time-varying strength
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Polynomial interaction terms with sparse connectivity and varying exponents
        self.poly_interactions = np.random.uniform(-0.5, 0.5, (dim, dim, dim))
        # Multi-scale harmonic components with frequency modulation
        self.harmonic_freqs = np.random.uniform(1.0, 10.0, dim)
        # Nonlinear transformation parameters with chaotic feedback
        self.transform_params = np.random.uniform(0.1, 3.0, dim)
        # Dynamic penalty coefficients with varying exponents and chaotic modulation
        self.penalty_coeffs = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component with varying degrees
        poly_energy = 0.0
        for i in range(self.dim):
            term = 0.0
            for j in range(6):
                term += self.poly_coeffs[i, j] * (x[i] ** (j + 1))
            poly_energy += term ** 2
            
        # Radial basis function component with multiple centers and varying widths
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(20):
                dist = np.sum((x[i] - self.rbf_centers[i, j]) ** 2)
                rbf_sum += np.exp(-dist / (2 * self.rbf_widths[j] ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Dynamic dimensionality scaling with periodic modulation
        scaling_energy = 0.0
        for i in range(self.dim):
            scaling_energy += self.scaling_factors[i] * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            
        # Chaotic coupling between dimensions with sparse connectivity
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.7:
                    coupling_energy += self.coupling_coeffs[i, j] * x[i] * x[j]
                    
        # Sparse polynomial interactions between dimensions
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and np.random.rand() > 0.8:
                        interaction_energy += self.poly_interactions[i, j, k] * x[i] * x[j] * x[k]
                        
        # Multi-scale harmonic components with frequency modulation
        harmonic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.harmonic_freqs[i] * x[i])
            freq_term += 0.5 * np.sin(2 * self.harmonic_freqs[i] * x[i])
            freq_term += 0.3 * np.sin(4 * self.harmonic_freqs[i] * x[i])
            harmonic_energy += freq_term ** 2
            
        # Nonlinear transformation with chaotic feedback
        transform_energy = 0.0
        for i in range(self.dim):
            trans = np.tanh(self.transform_params[i] * x[i])
            trans += 0.3 * np.sin(3 * self.transform_params[i] * x[i])
            transform_energy += trans ** 2
            
        # Dynamic penalty mechanism with varying exponents
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_coeffs[i] * (np.abs(x[i]) - 2.5) ** 4
            
        # Combine all components with carefully tuned weights
        total = 0.3 * poly_energy + 0.25 * rbf_energy + 0.15 * scaling_energy + 0.1 * coupling_energy + 0.08 * interaction_energy + 0.07 * harmonic_energy + 0.03 * transform_energy + 0.02 * penalty_energy
        
        return total
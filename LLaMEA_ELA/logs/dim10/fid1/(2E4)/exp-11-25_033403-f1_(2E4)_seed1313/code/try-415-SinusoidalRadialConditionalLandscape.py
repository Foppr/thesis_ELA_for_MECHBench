import numpy as np

class SinusoidalRadialConditionalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize sinusoidal parameters with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 6.0, dim)
        self.sin_amp = np.random.uniform(0.5, 2.5, dim)
        # Initialize radial basis functions with random centers and variances
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (3, dim))
        self.rbf_vars = np.random.uniform(0.5, 2.0, (3, dim))
        self.rbf_weights = np.random.uniform(1.0, 3.0, 3)
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 0.8, dim)
        # Initialize cross-dimensional coupling matrix
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize phase shifts for sinusoidal components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute sinusoidal components
        sin_terms = 0.0
        for j in range(self.dim):
            sin_term = self.sin_amp[j] * np.sin(self.sin_freq[j] * x[j] + self.phase_shifts[j])
            sin_terms += sin_term
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(3):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute adaptive conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(3.0 * x[j]))
        
        # Compute cross-dimensional coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Combine all components with appropriate weights
        total = 0.8 * sin_terms + 0.6 * rbf_terms + 0.4 * cond_terms + 0.3 * coupling_terms
        
        return total
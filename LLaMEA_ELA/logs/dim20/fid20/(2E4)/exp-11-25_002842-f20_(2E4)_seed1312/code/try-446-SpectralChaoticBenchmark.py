import numpy as np

class SpectralChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients for each dimension
        self.poly_chaos_coeffs = np.random.uniform(-2.0, 2.0, (dim, 6))
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 15))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, 15))
        # Spectral decomposition components for multi-scale structure
        self.spectral_basis = np.random.randn(dim, dim)
        self.spectral_freqs = np.random.uniform(0.1, 5.0, dim)
        # Cross-dimension coupling with harmonic interactions
        self.harmonic_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Variable conditioning factors with exponential scaling
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        # Multi-modal Gaussian components for complex landscape structure
        self.gauss_means = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.gauss_vars = np.random.uniform(0.2, 1.5, (dim, 10))
        self.gauss_weights = np.random.dirichlet(np.ones(10), dim)
        # Nonlinear transformation parameters
        self.transform_params = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_value = 0.0
            for j in range(6):
                poly_value += self.poly_chaos_coeffs[i, j] * np.polynomial.hermite.hermval(x[i], [0]*j + [1])
            result += poly_value ** 2
            
        # Radial basis function component
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(15):
                rbf_sum += self.rbf_widths[i, j] * np.exp(-0.5 * ((x[i] - self.rbf_centers[i, j]) ** 2) / (self.rbf_widths[i, j] ** 2))
            rbf_energy += rbf_sum
            
        # Spectral decomposition component with multi-scale oscillations
        spectral_energy = 0.0
        for i in range(self.dim):
            spec_value = np.dot(self.spectral_basis[i, :], x)
            spectral_energy += self.spectral_freqs[i] * np.sin(spec_value) + self.spectral_freqs[i] * np.cos(spec_value)
            
        # Harmonic coupling between dimensions
        harmonic_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    harmonic_energy += self.harmonic_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Variable conditioning with exponential scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning_factors[i] * (np.exp(x[i] ** 2) - 1)
            
        # Multi-modal Gaussian mixture component
        gaussian_energy = 0.0
        for i in range(self.dim):
            gauss_sum = 0.0
            for k in range(10):
                gauss_sum += self.gauss_weights[i, k] * np.exp(-0.5 * ((x[i] - self.gauss_means[i, k]) ** 2) / (self.gauss_vars[i, k] ** 2))
            gaussian_energy += -np.log(gauss_sum)
            
        # Nonlinear transformation component
        transform_energy = 0.0
        for i in range(self.dim):
            transform_energy += self.transform_params[i] * np.sin(x[i]) ** 3 + self.transform_params[i] * np.cos(x[i]) ** 3
            
        # Combine all components with weighted sum
        total = 0.15 * result + 0.20 * rbf_energy + 0.15 * spectral_energy + 0.15 * harmonic_energy + 0.10 * conditioning_energy + 0.15 * gaussian_energy + 0.10 * transform_energy
        
        return total
import numpy as np

class RadialSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers distributed in a hypersphere
        self.centers = np.random.uniform(-4.0, 4.0, (dim, 10))
        # Adaptive shape parameters for each RBF
        self.shape_params = np.random.uniform(0.5, 2.0, 10)
        # Spectral mixing coefficients for frequency domain
        self.spectral_coeffs = np.random.normal(0, 1, (dim, 15))
        # Cross-dimensional coupling weights
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Polynomial modulation terms
        self.poly_modulation = np.random.randint(2, 6, dim)
        # Adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.5, dim)
        # Frequency components for spectral mixing
        self.frequencies = np.random.uniform(0.1, 3.0, 15)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function component with adaptive shape
        rbf_energy = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[:, i]) ** 2)
            rbf_energy += np.exp(-self.shape_params[i] * dist)
            
        # Spectral mixing component using Fourier-like approach
        spectral_energy = 0.0
        for i in range(self.dim):
            for j in range(15):
                spectral_energy += self.spectral_coeffs[i, j] * np.sin(self.frequencies[j] * x[i])
                
        # Cross-dimensional coupling with weighted interactions
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_weights[i, j] * x[i] * x[j]
                    
        # Polynomial modulation for nonlinearity
        poly_energy = 0.0
        for i in range(self.dim):
            poly_energy += self.scaling_factors[i] * (x[i] ** self.poly_modulation[i])
            
        # Combine all components with dynamic weights
        total = 0.4 * rbf_energy + 0.3 * spectral_energy + 0.2 * coupling_energy + 0.1 * poly_energy
        
        return -total  # Negative because we want to minimize
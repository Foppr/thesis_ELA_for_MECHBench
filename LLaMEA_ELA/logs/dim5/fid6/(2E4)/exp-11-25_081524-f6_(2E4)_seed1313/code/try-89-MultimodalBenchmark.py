import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonics coefficients
        self.sph_harm_coeffs = np.random.randn(3, dim)
        # Precompute Gaussian mixture parameters
        self.gauss_means = np.random.uniform(-5.0, 5.0, (5, dim))
        self.gauss_covs = [np.eye(dim) * (0.5 + np.random.rand()) for _ in range(5)]
        self.gauss_weights = np.random.rand(5)
        self.gauss_weights /= np.sum(self.gauss_weights)
        # Precompute evolutionary fitness landscape parameters
        self.evolve_params = np.random.randn(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonics component
        sph_harm = 0.0
        for i in range(self.dim):
            sph_harm += self.sph_harm_coeffs[0, i] * np.sin(x[i]) + \
                       self.sph_harm_coeffs[1, i] * np.cos(x[i]) + \
                       self.sph_harm_coeffs[2, i] * np.sin(2 * x[i])
        
        # Gaussian mixture model component
        gauss_mixture = 0.0
        for i in range(5):
            diff = x - self.gauss_means[i]
            exp_term = np.exp(-0.5 * np.dot(diff, np.dot(np.linalg.inv(self.gauss_covs[i]), diff)))
            gauss_mixture += self.gauss_weights[i] * exp_term
            
        # Evolutionary fitness landscape with adaptive parameters
        evolve_fitness = 0.0
        for i in range(self.dim):
            evolve_fitness += (self.evolve_params[i] * x[i]**3 + 
                              np.sin(self.evolve_params[i] * x[i]) * 
                              np.cos(self.evolve_params[i] * x[i]))
        
        # Cross-dimensional coupling with radial basis functions
        rbf_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                rbf_coupling += np.exp(-dist**2 / (2 * (0.5 + np.random.rand())))
        
        # Dynamic scaling based on position
        dynamic_scale = 1.0 + 0.5 * np.sin(np.sum(x**2) * 0.2)
        
        # Combine all components
        result = dynamic_scale * (sph_harm + gauss_mixture + evolve_fitness + rbf_coupling)
        
        return result
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for Gaussian mixture components
        self.n_components = 5
        self.means = np.random.uniform(-3, 3, (self.n_components, dim))
        self.covariances = [np.eye(dim) * np.random.uniform(0.5, 2.0) for _ in range(self.n_components)]
        # Polynomial chaos expansion parameters
        self.poly_degree = 4
        self.noise_level = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture model component
        gm_value = 0
        for i in range(self.n_components):
            diff = x - self.means[i]
            cov_inv = np.linalg.inv(self.covariances[i])
            det_cov = np.linalg.det(self.covariances[i])
            exponent = -0.5 * np.dot(np.dot(diff, cov_inv), diff)
            weight = 1.0 / (np.sqrt(2 * np.pi * det_cov))
            gm_value += weight * np.exp(exponent)
        
        # Polynomial chaos expansion component
        pce_value = 0
        for i in range(self.dim):
            # Use Legendre polynomials up to degree 4
            poly_vals = [1, x[i]]
            if self.poly_degree > 1:
                poly_vals.append((1/2) * (3 * x[i]**2 - 1))
            if self.poly_degree > 2:
                poly_vals.append((1/2) * (5 * x[i]**3 - 3 * x[i]))
            if self.poly_degree > 3:
                poly_vals.append((1/8) * (35 * x[i]**4 - 30 * x[i]**2 + 3))
            
            # Random coefficients for each polynomial term
            coeffs = np.random.uniform(-1, 1, len(poly_vals))
            pce_value += np.dot(coeffs, poly_vals)
        
        # Adaptive noise injection based on input magnitude
        noise = np.random.normal(0, self.noise_level * (1 + np.linalg.norm(x)**2 / 25.0), 1)[0]
        
        # Dynamic scaling factor that changes with dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5)
        
        return scale_factor * (gm_value + pce_value) + noise
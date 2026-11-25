import numpy as np

class PolynomialGaussianAdaptiveLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.normal(0, 1, (dim, 4))
        # Gaussian mixture model parameters
        self.gmm_means = np.random.uniform(-4.0, 4.0, (3, dim))
        self.gmm_covs = np.array([np.eye(dim) * (0.5 + 0.3 * np.sin(0.5 * np.pi * i)) for i in range(3)])
        self.gmm_weights = np.array([0.3, 0.4, 0.3])
        # Adaptive gradient modulation parameters
        self.adaptive_factors = np.array([1.0 + 0.2 * np.cos(0.7 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = self.poly_coeffs[i, 0] + \
                       self.poly_coeffs[i, 1] * x_i + \
                       self.poly_coeffs[i, 2] * x_i**2 + \
                       self.poly_coeffs[i, 3] * x_i**3
            poly_component += poly_term * np.exp(-0.1 * x_i**2)
        poly_component /= self.dim
        
        # Gaussian mixture model component
        gmm_component = 0.0
        for i in range(3):
            diff = x - self.gmm_means[i]
            exp_arg = -0.5 * np.dot(diff, np.linalg.solve(self.gmm_covs[i], diff))
            gmm_component += self.gmm_weights[i] * np.exp(exp_arg)
        gmm_component /= 3.0
        
        # Adaptive gradient modulation component
        grad_modulation = 0.0
        for i in range(self.dim):
            mod_factor = self.adaptive_factors[i] * (1.0 + 0.1 * np.sin(0.8 * np.pi * i + 0.3 * np.sum(x)))
            grad_modulation += mod_factor * x[i]**4 * np.exp(-0.05 * x[i]**2)
        grad_modulation /= self.dim
        
        # Cross-dimensional correlation with polynomial coupling
        cross_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.3 * np.cos(0.6 * np.pi * (i - j) + 0.2 * np.sum(x))
                cross_corr += coupling * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_corr /= (self.dim * (self.dim - 1) / 2.0)
        
        # Dynamic conditioning with time-like parameter
        dynamic_cond = 0.0
        time_param = np.sum(x) * 0.1
        for i in range(self.dim):
            cond_factor = 1.0 + 0.25 * np.sin(0.5 * np.pi * i + time_param)
            dynamic_cond += cond_factor * x[i]**3 * np.exp(-0.08 * x[i]**2)
        dynamic_cond /= self.dim
        
        # Combine all components with adaptive weighting
        result = 0.25 * poly_component + 0.3 * gmm_component + 0.15 * grad_modulation + \
                 0.15 * cross_corr + 0.15 * dynamic_cond
        
        return result
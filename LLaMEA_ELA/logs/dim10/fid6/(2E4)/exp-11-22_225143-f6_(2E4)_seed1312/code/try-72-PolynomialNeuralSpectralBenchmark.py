import numpy as np

class PolynomialNeuralSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos coefficients for each dimension
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 4))
        # Neural network inspired coupling weights
        self.weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Spectral filtering parameters
        self.filter_freqs = np.random.uniform(0.5, 3.0, dim)
        self.filter_ampls = np.random.uniform(0.5, 2.0, dim)
        # Mixed convexity control
        self.convexity_params = np.random.uniform(0.1, 1.0, dim)
        # Local basin parameters
        self.basin_centers = np.random.uniform(-5.0, 5.0, (3, dim))
        self.basin_radii = np.random.uniform(0.5, 2.0, 3)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Polynomial chaos component with mixed degree terms
        for i in range(self.dim):
            poly_sum = 0.0
            for d in range(4):
                poly_sum += self.poly_coeffs[i, d] * (x_norm[i]**d)
            f_val += 0.3 * (poly_sum**2 + 0.1 * poly_sum**3)
        
        # Neural network inspired couplings with sigmoidal interactions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.weights[i, j] * np.tanh(x_norm[i] * x_norm[j])
            f_val += 0.25 * (coupling_sum**2 + 0.05 * coupling_sum**4)
        
        # Spectral filtering with frequency-dependent components
        for i in range(self.dim):
            spec_term = 0.0
            for k in range(10):
                spec_term += self.filter_ampls[i] * np.sin(self.filter_freqs[i] * (k + 1) * x_norm[i])
            f_val += 0.2 * (spec_term**2 + 0.03 * spec_term**3)
        
        # Mixed convexity control with varying curvature
        for i in range(self.dim):
            convex_term = self.convexity_params[i] * (x_norm[i]**2) + (1 - self.convexity_params[i]) * (x_norm[i]**4)
            f_val += 0.15 * convex_term
        
        # Local basin attraction terms
        for k in range(3):
            dist = np.sum((x_norm - self.basin_centers[k])**2)
            if dist < self.basin_radii[k]**2:
                f_val += 0.3 * np.exp(-dist / (2 * self.basin_radii[k]**2))
        
        # Add ruggedness with high-frequency oscillations
        rugged_term = 0.0
        for i in range(self.dim):
            rugged_term += np.sin(10.0 * x_norm[i]) * np.cos(7.0 * x_norm[i])
        f_val += 0.25 * rugged_term**2
        
        # Add conditioning complexity with variable scaling
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += (i + 1) * (x_norm[i]**2)
        f_val += 0.1 * cond_term
        
        return f_val
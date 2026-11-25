import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        poly_term = 0
        for i in range(self.dim):
            # Hermite polynomial H_3(x) = 8x^3 - 12x
            h3_val = 8 * (x_norm[i]**3) - 12 * x_norm[i]
            poly_term += h3_val * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial basis function interactions with multiquadric kernels
        rbf_term = 0
        centers = np.random.uniform(-1, 1, (self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                dist = np.linalg.norm(x_norm - centers[i])
                # Multiquadric RBF: sqrt(dist^2 + epsilon^2)
                rbf_term += np.exp(-dist**2 / 0.1) * np.sin(5 * x_norm[j])
        
        # Spectral decomposition component with frequency domain filtering
        spec_term = 0
        for i in range(self.dim):
            # Apply discrete cosine transform-like weighting
            weight = 1.0 / (1 + 0.1 * i)
            spec_term += weight * np.cos(3 * x_norm[i]) * np.sin(7 * x_norm[i])
        
        # Cross-dimensional coupling with polynomial interaction terms
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial coupling with varying degrees
                coupling_degree = 2 + (i % 3)
                cross_term += (x_norm[i]**coupling_degree) * (x_norm[j]**(coupling_degree + 1)) * \
                             np.cos(2 * x_norm[i] + x_norm[j])
        
        # Nonlinear frequency modulation component
        freq_term = 0
        for i in range(self.dim):
            mod_freq = 2 + 3 * np.sin(x_norm[i])
            freq_term += np.sin(mod_freq * x_norm[i]) * np.cos(4 * x_norm[i])
        
        # Add noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        # Combine all terms with optimized weights
        result = 1.5 * poly_term + 1.2 * rbf_term + 1.0 * spec_term + 1.3 * cross_term + 0.8 * freq_term
        
        return result + noise
import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different degrees
        self.poly_coeffs = np.random.randn(5, dim) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with mixed terms
        poly_expansion = 0.0
        for i in range(5):
            term = 1.0
            for j in range(self.dim):
                term *= np.power(x_norm[j], i) * self.poly_coeffs[i, j]
            poly_expansion += term
        
        # Radial basis function component with multi-scale centers
        rbf_sum = 0.0
        centers = np.random.randn(10, self.dim) * 2.0
        for center in centers:
            distance = np.sqrt(np.sum((x_norm - center)**2))
            rbf_sum += np.exp(-distance**2 / 0.5) * np.sin(distance * 3)
        
        # Stochastic perturbation with temporal correlation
        stochastic_pert = 0.0
        for i in range(self.dim):
            stochastic_pert += np.sin(x_norm[i] * 10 + np.random.randn() * 0.1) * \
                              np.cos(x_norm[i] * 7 + np.random.randn() * 0.1)
        
        # Cross-dimensional coupling with trigonometric interaction
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling += np.sin(x_norm[i] * x_norm[j] * 5) * np.cos(x_norm[i] - x_norm[j])
        
        # Asymmetric basin with multiple local minima
        basin = 0.0
        for i in range(3):
            center = np.random.randn(self.dim) * 0.5
            dist = np.sqrt(np.sum((x_norm - center)**2))
            basin += (dist**2 + 0.1 * np.sin(dist * 20)) * np.exp(-dist**2 / 2)
        
        # Combined function with adaptive weights and noise injection
        return 0.3 * poly_expansion + 0.4 * rbf_sum + 0.2 * stochastic_pert + \
               0.1 * coupling + 0.05 * basin + 0.02 * np.random.randn()
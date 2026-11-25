import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and RBF components
        self.poly_degree = 4
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 15)
        self.weights = np.random.normal(0, 1, 15)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(1, self.poly_degree + 1):
            poly_term += np.sum(x_norm**i) * np.sin(i * np.pi * x_norm[0]) * np.cos(i * np.pi * x_norm[-1])
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.weights[i]
            distance = np.sum((x_norm - center)**2)
            rbf_sum += weight * np.exp(-distance / (2 * width**2))
        
        # Add interaction terms between dimensions
        interaction_term = 0.0
        for i in range(self.dim - 1):
            interaction_term += (x_norm[i] - x_norm[i+1])**4 + \
                              np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i+1])
        
        # Combine all components with adaptive scaling
        total_energy = 0.5 * poly_term**2 + 0.3 * rbf_sum + 0.2 * interaction_term
        
        # Add noise for ruggedness
        noise = 0.01 * np.random.rand()
        
        # Introduce dimensionality-dependent bias penalty
        penalty = 0.05 * self.dim * np.std(x_norm)**2
        
        return total_energy + noise + penalty
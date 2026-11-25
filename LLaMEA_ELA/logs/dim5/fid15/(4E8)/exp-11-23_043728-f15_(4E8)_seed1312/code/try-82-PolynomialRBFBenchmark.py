import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and RBF components
        self.poly_degree = 4
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.weights = np.random.normal(0, 1, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Polynomial chaos expansion component
        poly_term = np.sum([np.sum(x_norm**i) for i in range(1, self.poly_degree + 1)])
        
        # Radial basis function component
        rbf_values = []
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.weights[i]
            distance = np.sum((x_norm - center)**2)
            rbf_value = weight * np.exp(-distance / (2 * width**2))
            rbf_values.append(rbf_value)
        rbf_term = np.sum(rbf_values)
        
        # Gradient-based attraction field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x_norm[i] - np.sin(x_norm[i]))**2
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i] - x_norm[j])**4
        
        # Combine all components with adaptive scaling
        total_energy = poly_term + rbf_term + 0.5 * grad_field + 0.3 * interaction
        
        # Add noise for ruggedness
        noise = 0.01 * np.random.rand()
        
        # Introduce basin-like structure through sigmoidal transformation
        basin_structure = np.sum(1 / (1 + np.exp(-10 * (x_norm - np.mean(x_norm)))))
        
        # Apply dimensionality-dependent scaling
        scale_factor = 1.0 + 0.02 * self.dim + 0.001 * self.dim**2
        
        return scale_factor * (total_energy + noise + 0.1 * basin_structure)
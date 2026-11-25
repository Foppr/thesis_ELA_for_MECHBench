import numpy as np

class PolynomialRBFGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion parameters
        self.poly_degrees = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        # Radial basis function parameters with adaptive widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=10)
        # Adaptive gradient modulation parameters
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_direction = np.random.uniform(-np.pi, np.pi, size=dim)
        self.adaptation_rate = np.random.uniform(0.1, 0.9, size=dim)
        # Correlation structure parameters
        self.correlation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.correlation_matrix = np.dot(self.correlation_matrix, self.correlation_matrix.T)
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Dynamic fitness scaling parameters
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        self.dynamic_shift = np.random.uniform(-1.0, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            x_i = x[i]
            poly_val = 0.0
            for j in range(self.poly_degrees[i]):
                poly_val += self.poly_coeffs[i, j] * (x_i ** (j + 1))
            poly_component += poly_val * self.scaling_factors[i]
        
        # Radial basis function component with adaptive widths
        rbf_component = 0.0
        for i in range(10):
            distance = np.sum((x - self.rbf_centers[:, i]) ** 2)
            rbf_value = np.exp(-distance / (2 * (self.rbf_widths[i] ** 2)))
            rbf_component += self.rbf_weights[i] * rbf_value
            
        # Adaptive gradient modulation
        grad_component = 0.0
        for i in range(self.dim):
            direction = np.cos(self.gradient_direction[i]) * x[i] + np.sin(self.gradient_direction[i])
            grad_component += self.gradient_magnitude[i] * np.sin(direction) * np.exp(-0.1 * x[i]**2)
        
        # Correlation-based interaction
        corr_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_component += self.correlation_matrix[i, j] * x[i] * x[j]
        
        # Dynamic fitness scaling with shifting and adaptive factors
        scale_component = 0.0
        for i in range(self.dim):
            shift = self.dynamic_shift[i] * np.sin(0.5 * x[i])
            scale_component += (x[i] + shift) ** 2 * self.scaling_factors[i]
        
        # Combined fitness function with varying weights
        return (1.5 * poly_component + 
                2.0 * rbf_component + 
                1.2 * grad_component + 
                0.8 * corr_component + 
                1.0 * scale_component)
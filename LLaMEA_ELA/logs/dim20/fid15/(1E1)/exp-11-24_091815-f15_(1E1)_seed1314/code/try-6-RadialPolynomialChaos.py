import numpy as np

class RadialPolynomialChaos:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Generate random centers and weights for radial basis functions
        np.random.seed(42)  # For reproducibility
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            distance = np.sum((x - self.centers[i]) ** 2)
            rbf_sum += self.weights[i] * np.exp(-distance / (2 * 0.5**2))
        
        # Polynomial chaos expansion component (using Hermite polynomials)
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            # Use third-order Hermite polynomial components
            poly_term += (2 * xi**3 - 3 * xi) * np.sin((i + 1) * np.pi * xi)
        
        # Add a global quadratic term to ensure a unique minimum
        quadratic_term = 0.5 * np.sum(x**2)
        
        # Combine all terms with different scaling factors
        return rbf_sum + 0.5 * poly_term + 0.1 * quadratic_term
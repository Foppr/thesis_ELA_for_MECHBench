import numpy as np

class SinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal frequencies and polynomial coefficients
        np.random.seed(42)
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (3, dim))
        self.rb_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rb_weights = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies
        sinusoidal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequencies[i]
            sinusoidal_sum += np.sin(freq * xi) * np.cos(freq * xi) + 0.5 * np.sin(2 * freq * xi)
        
        # Polynomial conditioning component
        polynomial_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0.0
            for j in range(3):
                poly_term += self.poly_coeffs[j, i] * (xi ** (j + 1))
            polynomial_sum += poly_term ** 2
        
        # Radial basis function component
        rb_sum = 0.0
        for i in range(10):
            center = self.rb_centers[i]
            weight = self.rb_weights[i]
            distance = np.sum((x - center) ** 2)
            rb_sum += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x[i] ** 2) * x[j] * np.sin(x[i] + x[j])
        
        # Combine all components
        result = 0.4 * sinusoidal_sum + 0.3 * polynomial_sum + 0.2 * rb_sum + 0.1 * cross_interaction
        
        return result
import numpy as np

class RadialPolynomialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random centers for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        # Random polynomial coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Asymmetric gradient weights
        self.gradient_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(len(self.centers)):
            center = self.centers[i]
            distance = np.sum((x - center)**2)
            rbf_sum += np.exp(-distance / (2 * 0.5**2))
        
        # Polynomial chaos expansion component
        poly_sum = 0.0
        for i in range(self.dim):
            for j in range(5):
                poly_sum += self.poly_coeffs[i, j] * (x[i]**j)
        
        # Asymmetric gradient field component
        grad_sum = 0.0
        for i in range(self.dim):
            grad_sum += self.gradient_weights[i] * (x[i]**3) * np.cos(x[i])
        
        # Cross-dimensional interaction terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross_sum += (x[i]**2) * (x[j]**2) * np.sin(x[i] + x[j])
        
        # Non-convexity modifier with sine modulation
        modulator = 1.0 + 0.5 * np.sin(np.sum(x**2) * 0.1)
        
        # Combine all components
        f_val = rbf_sum + poly_sum + grad_sum + cross_sum * modulator
        
        # Add noise and scaling
        noise = np.random.normal(0, 0.01)
        return f_val * (1.0 + noise) - 10.0  # Shift to ensure global minimum is not at zero
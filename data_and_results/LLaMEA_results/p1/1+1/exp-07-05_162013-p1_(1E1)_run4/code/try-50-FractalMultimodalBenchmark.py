import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal constants
        self.fractal_dim = 2 * np.pi / dim
        self.coefficients = np.random.uniform(-1, 1, dim)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal cosine component
        for i in range(self.dim):
            cos_term = np.cos(self.fractal_dim * x[i] * (i + 1))
            result += self.coefficients[i] * cos_term
            
        # Polynomial chaos expansion
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(1, 6):
                poly_term += (x[i] ** j) / (j * (j + 1))
            result += 0.1 * poly_term
            
        # Radial basis function penalties
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                diff = x - self.rbf_centers[i, j]
                rbf_sum += np.exp(-0.5 * (diff / self.rbf_widths[i]) ** 2)
            result += 0.2 * rbf_sum
            
        # Non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.05 * interaction
                
        # Scale-invariant fractal component
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += np.sin(10 * x[i]) * np.cos(10 * x[i])
        result += 0.15 * fractal_sum
        
        # Add global minimum attractor
        result += 0.05 * np.sum(x**2)
        
        return result
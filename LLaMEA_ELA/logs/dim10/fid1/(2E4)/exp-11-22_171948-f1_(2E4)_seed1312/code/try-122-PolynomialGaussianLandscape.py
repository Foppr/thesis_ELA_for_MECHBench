import numpy as np

class PolynomialGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial potential terms with varying degrees
        for i in range(self.dim):
            # Higher degree polynomial terms for increased complexity
            poly_term = (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i])
            result += 0.25 * poly_term**2
        
        # Gaussian ridge structures with varying widths and heights
        for i in range(self.dim):
            ridge_sum = 0.0
            for j in range(1, 6):  # 5 different Gaussian components
                width = 0.5 + 0.2 * j
                height = 1.0 / (j * (j + 1))
                ridge_sum += height * np.exp(-0.5 * ((x[i] - j) / width)**2)
            result += 0.3 * ridge_sum**2
        
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j]))
                result += 0.15 * coupling**2
        
        # Asymmetric noise injection with dimension-dependent scaling
        noise_scale = 0.1 + 0.05 * np.sin(self.dim)
        for i in range(self.dim):
            noise = np.random.normal(0, noise_scale) if np.random.rand() < 0.3 else 0
            result += 0.08 * (x[i] + noise)**2
        
        # Adaptive conditioning based on local gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(4*x[i]**3 + 1.5*x[i]**2 + 0.4*x[i] + 0.1)
        conditioning = 1.0 + 0.2 * np.tanh(grad_magnitude / self.dim)
        result *= conditioning
        
        # Multi-scale fractal-like structure with varying amplitude
        fractal_sum = 0.0
        for i in range(self.dim):
            for freq in [2, 4, 8]:
                fractal_sum += np.sin(freq * x[i]) * np.exp(-0.1 * (freq - 4)**2)
        result += 0.25 * fractal_sum**2
        
        # Final normalization and bias term
        result /= self.dim
        result += 0.02 * np.sum(np.abs(x))
        
        return result
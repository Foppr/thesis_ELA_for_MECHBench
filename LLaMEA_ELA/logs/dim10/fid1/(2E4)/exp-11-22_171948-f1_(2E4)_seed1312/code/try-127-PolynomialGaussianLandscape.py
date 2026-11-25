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
        
        # Cross-dimensional coupling with modified weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**2 + x[j]**2) * np.sin(0.7 * (x[i] - x[j]))  # Increased frequency
                result += 0.18 * coupling**2  # Slightly increased coupling strength
        
        # Asymmetric noise injection with dimension-dependent scaling
        noise_scale = 0.12 + 0.03 * np.sin(self.dim)  # Slight increase in noise scale
        for i in range(self.dim):
            noise = np.random.normal(0, noise_scale) if np.random.rand() < 0.35 else 0  # Slightly higher noise probability
            result += 0.09 * (x[i] + noise)**2
        
        # Adaptive conditioning based on local gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(4*x[i]**3 + 1.5*x[i]**2 + 0.4*x[i] + 0.1)
        conditioning = 1.0 + 0.25 * np.tanh(grad_magnitude / self.dim)  # Increased conditioning factor
        result *= conditioning
        
        # Enhanced fractal-like structure with modified amplitude and frequency
        fractal_sum = 0.0
        for i in range(self.dim):
            for freq in [1, 3, 6, 12]:  # Changed frequencies for more complexity
                fractal_sum += np.sin(freq * x[i]) * np.exp(-0.15 * (freq - 6)**2)  # Modified decay rate
        result += 0.3 * fractal_sum**2  # Increased fractal contribution
        
        # Final normalization and bias term
        result /= self.dim
        result += 0.025 * np.sum(np.abs(x))  # Slightly increased bias
        
        return result